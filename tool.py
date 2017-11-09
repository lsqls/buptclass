#coding:utf-8
import re
def delspace(string):
    pattern=re.compile(r'\s')
    string=re.sub(pattern,'',string)
    return string
def html(campuses):
    tabels=u''
    for campus in campuses:
        trs=u''
        for  item in  campus[2]:#timetable
            contents=u''
            i=0
            for bulding in item[1]:
                varible_rooms=item[2][i]
                info=u'''<div>\n
                %s %s</div>\n
                 '''%(bulding,varible_rooms)
                i=i+1
                contents=contents+info
            tr = u'''<tr>\n
                         <tr>\n
                         <th>\n		
             				%s\n
             				</th>\n
             				<tr>\n
             				<td>\n
             				%s\n
             				</td>\n
             				</tr>\n
                         ''' % (item[0],contents)
            trs=trs+tr
        tabel=u'''<table>\n
        <tbody>\n
        <b>%s %s</b>\n
        %s
        </tbody>\n
        </table>\n
        '''%(campus[0],campus[1],trs)
        tabels=tabels+tabel
    page = u'''
       <!DOCTYPE html>\n
<html lang="zh-CN">\n
  <head>\n
    <meta charset="utf-8">\n
    <meta http-equiv="X-UA-Compatible" content="IE=edge">\n
    <meta name="viewport" content="width=device-width, initial-scale=1">\n
    <!-- 上述3个meta标签*必须*放在最前面，任何其他内容都*必须*跟随其后！ -->\n
   <title >北邮空教室</title>\n

    <!-- Bootstrap -->\n
    <link href="css/bootstrap.min.css" rel="stylesheet">\n

    <!-- HTML5 shim and Respond.js for IE8 support of HTML5 elements and media queries -->\n
    <!-- WARNING: Respond.js doesn't work if you view the page via file:// -->\n
    <!--[if lt IE 9]>
      <script src="https://cdn.bootcss.com/html5shiv/3.7.3/html5shiv.min.js"></script>\n
      <script src="https://cdn.bootcss.com/respond.js/1.4.2/respond.min.js"></script>\n
    <![endif]-->\n
</head>\n
       <body>\n
       %s
       </body>\n
       </html>\n
       '''%tabels
    page=page.encode("utf-8")
    with open("index.html","wb") as f:
        f.write(page)
        f.close()