#! /usr/bin/env python
# -*- coding: utf-8 -*-
# Author: thomasliyan
# Email: lyhy7891@qq.com
# 2017-05-21 20:00:09
def generateSequence(eleSet,eleNum,limit , count ) :
    ''' make a sequence of number which is the sum of eleSet. eleNum stards for the count of the ele in eleSet . '''
    ''' limit : if get the limit then stop.'''
    ''' count :  the length of the sequence.  '''
    s=0
    workingList=[ 0 for i in eleSet ]
    c=0
    eleIdx=0
    eleMAx=eleNum[eleIdx]
    cursor=0
    results=[]
    while  True  :
        if s==limit :
            return   results 
        if c==count  :
            return  results 
        if  cursor <= eleMAx :
            workingList[eleIdx]=cursor
            s=getSum(eleSet,workingList)
            results.append(s) 
            c+=1 
            cursor+=1 
        else :
            eleIdx+=1 
            cursor=0 
            while True :
                if eleIdx >= len(eleSet) :
                    print 'over'
                    return  results
                eleMAx=eleNum[eleIdx]
                workingList[eleIdx]=workingList[eleIdx]+1
                if workingList[eleIdx] <=eleMAx :
                    break 
                else  :
                    eleIdx+=1
            for i in  range(eleIdx):
                workingList[i]=0
            eleIdx=0
            eleMAx=eleNum[eleIdx]
    return  results
#get sum of list     
def getSum(eleSet , eleCount) :
    s=0
    for i in range(len(eleSet)):
        s+=eleSet[i] * eleCount[i]
    return s  

if  __name__ == '__main__' :
    eleSet=[1,2,5] # 1 rmb 2 rmb 5 rmb 
    eleNum=[1,3,4] # one bank note  of 1 rmb , three bank notes of 2 rmb and 4 for 5 rmb
    limit = 100  #ignore   this parameter 
    count = 300  # can not reach 300 
    s=generateSequence(eleSet,eleNum,limit,count)
    # how many combinatios which can make 10 yuan 
    #print s
    total= [  x    for x in s if x==10 ]
    print total  # Two  combinations 
    r=s[::-1]
    #print r 
    ss= [ s[i]+r[i] for  i in range(len(s))] 
    #print ss 
