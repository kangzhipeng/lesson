# -*- coding: cp936 -*-
#��9�µ�ϰ��

def readini(fileObj):
    aa={}
    for eachLine in fileObj:
        if  '=' in eachLine :
            x=eachLine.index('=')
            item=eachLine[:x]
            value=eachLine[x+1:]
            #print item
            #print value
            aa[item]=value
    return aa
def dis_ini_value(fileObj,item):
    cc=readini(fileObj)
    print cc[item]
