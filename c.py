from pydocx import PyDocX
import sys
import  os
# filename  = sys.argv[1]
filename ='/Users/jialaizhu/Documents/缠论资料/《缠中说禅》学习笔记20.01 Word版压缩包/教你炒股票24：MACD对背弛的辅助判断.docx'
def conver2html(filename,outputfold="/Users/jialaizhu/Documents/缠论资料/《缠中说禅》学习笔记20.01 Word版压缩包/111"):
    if outputfold is None:
        outputfold  = os.getcwd()
   
    html_str = html = PyDocX.to_html(filename)

    basename = os.path.basename(filename)
    docname = list(os.path.splitext(basename))
    docname.pop()
    docname  = "".join(docname)
    docname = docname.replace(' ','')
    imagefolder = os.path.join(outputfold,"%s.files"%(docname))
    try:
        os.system("rm -rf \"%s\""%(imagefolder))
    except:
        pass

    try:
        os.system("mkdir \"%s\""%(imagefolder))
    except:
        pass

    from bs4 import BeautifulSoup
    soup = BeautifulSoup(html_str)
    num = 0
    for img in soup.findAll('img'):
        srcdata = img['src']
        if srcdata.find('data:image/')==0:
            a = srcdata.find(',')
            filetype = srcdata[srcdata.find('/')+1:srcdata.find(';')]
            schema = srcdata[0:a]
            imgstring = srcdata[a+1:]
            import base64
            imgdata = base64.b64decode(imgstring)
            filename = '%s.%s'%(str(num),filetype) 
            url = "%s.files/%s.%s"%(docname,str(num),filetype)
            filename = os.path.join(imagefolder,filename) 
            num = num+1
            with open(filename, 'wb') as f:
                f.write(imgdata)
            img['src'] = url 
    html_str = str(soup)

    htmlfilename = os.path.join(outputfold,"%s.html"%(docname))
    f = open(htmlfilename, 'w', encoding="utf-8")
    f.write(html_str)
    f.close()

if __name__ == '__main__':
    filename = sys.argv[1]
    conver2html(filename,None)
