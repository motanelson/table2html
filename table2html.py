import os 
import copy
print("\033[47;31m\ngive me a txt to convert to html ? \n")
a=input().strip()
b=a
aaa=a.find(".")
if aaa>-1:
    b=copy.copy(a[:aaa])
heads="<html><head><title>$1</title><style>\nbody \n{\n  color: #ff0000;\n}\n</style>\n</head><body><table border=1><tr><td>".replace("$1",copy.copy(b))
ends="</td></tr></table></body></html>"
b=b+".html"
f1=open(a,"r")
ff=f1.read()
f1.close()
ff=ff.replace("<","«")
ff=ff.replace(">","»")
ff=ff.replace("\r\n","</th></tr><tr><th>")
ff=ff.replace("\n","</th></tr><tr><th>")
ff=ff.replace("|","</th><th>")


ends=ff+ends
heads=heads+ends
f1=open(b,"w")
f1.write(heads)
f1.close()

