def create(dirname="."):
    import os
    ret = []
    files = os.listdir(dirname)
    def cmp(a):
        try:
            n1 = a.find(' ')+1
            n2 = a.find('：')
            a = a[n1:n2]
            a = a[5:]
            return int(a)
        except:
            return 0
    aa =[]
    for a in files:
        if a=='index.htm':
            continue
        try:
            if a.split('.')[1] =='html':
                aa.append(a)
        except :
            pass
    files= sorted(aa, key=cmp, reverse=False)

    for a in files:
        filename = a
        filename = filename.replace(' ',"%20")
        a = '- [%s](%s)'%(a.replace(".html",""),filename)
        ret.append(a)
    index = "\n".join(ret)
    fp = open("README.md","w+")
    fp.write(index)
    pass

if __name__ == '__main__':
    import sys
    if len(sys.argv)>1:
        create(sys.argv[1])
    else:
        create()
