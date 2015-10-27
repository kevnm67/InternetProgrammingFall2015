#!c:/python34/python.exe
#!/usr/bin/python3
__author__ = 'bsetzer'

import os

print("Content-Type: text/html; charset=UTF-8")

print()

#print(os.environ)

# for (k,v) in os.environ.items():
#     print(k, "  ", v)




print("<p>")
print("<a href='{}'>{}</a>".format( "/index.html", "Home page"))
print("<p>")
print("<a href='{}'>{}</a>".format( "printenv.py", "print-env"))
print("<p>")
print("<a href='{}'>{}</a>".format( "/cgi-bin/printenv.py", "print-env"))

print("<table>")
for k in sorted(os.environ.keys()):
    print("<tr>")
    print("<td>",k, "</td><td>",os.environ[k],"</td>")
    print("</tr>")
print("</table>")