#coding:utf-8
import re
import tool
import requests
import json
from bs4 import  BeautifulSoup
import ftplib
import time
def get_info(url,decode=0):
    table=[]
    if decode==1:
        page=BeautifulSoup(requests.get(url).content.decode("GBK").encode("utf-8"),"lxml")
    else:
        page = BeautifulSoup(requests.get(url).content, "lxml")
    b=page.find(name='b')
    date=b.contents[0].strip()
    campus=unicode(page.find('font',attrs={"color":"red"}).contents[0])
    time_tds=page.find_all('td',attrs={"class":"sortable"})
    timetable=[]
    for time in time_tds:
        buildingss=[]
        variable_classroomss=[]
        buildings=time.next_sibling.next_sibling.find_all("font")
        for building in buildings:
            buildingss.append(building.string.strip())
            variable_classroom=building.next_element.next_element
            variable_classroomss.append(tool.delspace(variable_classroom.strip()))
        timetable.append([time.string.strip(),buildingss,variable_classroomss])
    return [campus,date,timetable]
def upload(filenames):
    ftp = ftplib.FTP()
    host = "yourhost"
    port = 21
    ftp.connect(host, port)
    try:
        ftp.login("ftpusername", "password")
        ftp.cwd('/buptclass')
        for filename in filenames:
            file=open(filename,"rb")
            ftp.storbinary("STOR "+filename,file)
            print ("upload %s success"%filename)
        ftp.close()
    except:
        print ("failed to login")
def run():
    BenBu=get_info("http://jwxt.bupt.edu.cn/zxqDtKxJas.jsp")
    ShaHe=get_info("http://jwxt.bupt.edu.cn/shxqDtKxJas.jsp",1)
    HongFu=get_info("http://jwxt.bupt.edu.cn/hfxqDtKxJas.jsp",1)
    tool.html([BenBu,ShaHe,HongFu])
    upload(["index.html"])
if __name__ == '__main__':
    run()
    time.sleep(30)
