from  c import  conver2html
import  os
fp = open('doclist')
root = '/Users/jialaizhu/Documents/缠论资料/《缠中说禅》学习笔记20.01 Word版压缩包/'
for a in fp.readlines():
    a = a.replace('\n','')
    filename = os.path.join(root,a)
    conver2html(filename,None)

import createindex
createindex.create()
import sys
sys.system("cp -r README.md _sidebar.md")
