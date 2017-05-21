import os
import os.path
##
## the implementation  of the algorithm  of Permutation  in  book  <<The Art Of Computer Programming >> by D.E.Knuth 
class DicPermutation:
    def __init__(self):
        pass
    def getElements(self):
        inp=raw_input('input elements separated by space  \n')
        self.es=inp.split()
        self.es.sort()
        self.n=len(self.es)
        st=''
        for i in self.es :
            st+=repr(i)
        print st
    def step1(self):
        ''' find the  j '''
        j=self.n-1
        while j>0 and self.es[j-1]>=self.es[j]:
            j=j-1
            if j<=0:
                print "-----over------\n"
                return False
        self.j=j
        return True
        
    def step2(self):
        '''increse a[j] '''
        l=self.n
        while(self.es[self.j-1]>=self.es[l-1]):
            l=l-1
        tmp=self.es[l-1]
        self.es[l-1]=self.es[self.j-1]
        self.es[self.j-1]=tmp
    def step3(self):
        ''' swap rest of list '''
        k=self.j+1
        l=self.n
        while k<l:
            tmp=self.es[k-1]
            self.es[k-1]=self.es[l-1]
            self.es[l-1]=tmp
            k=k+1
            l=l-1
        self.printList()
    def printList(self):
        strs=''
        for i in self.es:
            strs+=repr(i)
        print strs
    def run(self):
        if self.n<1:
            print 'no element'
            return
        while(self.step1()):
            self.step2()
            self.step3()
class  FullPermutation:
    def __init__(self):
        sts=raw_input('input eles separated by space  \n')
        es=sts.split()
        es.sort()
        if len(es)==0:
            print 'no elements'
            return
        self.c=[0 for i in range(len(es))]
        self.o=[1 for i in range(len(es))]
        self.es=es
        self.n=len(self.es)
    def step2(self):
        re=''
        print '---------------------'
        for i in self.es:
            re+=i
        print re
        re=''
        for i in self.c:
            re+=repr(i)
        print re
        #print '---------------------'
        self.step3()
    def step3(self):
        ''' try to change '''
        self.j=self.n
        self.s=0
        self.step4()
    def step4(self):
        self.q=self.c[self.j-1]+self.o[self.j-1]
        if self.q<0:
            self.step7()
        elif self.q==self.j:
            self.step6()
        else:
            self.step5()
    def step5(self):
        tmp=self.es[self.j-self.c[self.j-1]+self.s-1]
        self.es[self.j-self.c[self.j-1]+self.s-1]=self.es[self.j-self.q+self.s-1]
        self.es[self.j-self.q+self.s-1]=tmp
        n1=self.j-self.c[self.j-1]+self.s
        n2=self.j-self.q+self.s
        self.c[self.j-1]=self.q
        #print "step5  j=%d q=%d swap(%d,%d)"%(self.j,self.q,n1,n2)
        self.step2()
    def step6(self):
        if self.j==1:
            print '\n......over.......\n'
            return
        self.s+=1
        #print 'step 6  s=%d'%self.s
        self.step7()
    def step7(self):
        #print 'step7 j=%d o[j]=-o[j]'%self.j 
        self.o[self.j-1]=-1*self.o[self.j-1]
        self.j-=1
        self.step4()

if __name__=='__main__':
    ins= DicPermutation()
    ins.getElements()
    ins.run()
    #ins2=FullPermutation()
    #ins2.step2()
