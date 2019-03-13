import matplotlib as plt
from numpy import zeros
import numpy  as np
import random
import math
from tqdm import tqdm


  
def init(ip,op):
    ############################################################ 
    #w is randomly defined
    w= zeros([op,ip])
    
    for i in range(0,op):
        
        for j in range(0,ip):
            w[i][j]=random.randint(0,10)
            
    print(w)
    return w



class kn():
  
    
    def feeder(self,ip):
        
        x=zeros([ip,1])
        a=0
        i=0
        while(a==0):
            p1=random.randint(0,10)
            p2=random.randint(0,10)
            if(p1>p2):
                x[0][0]=p1
                x[1][0]=p2
                a=1
        print("x is ",x)
        return x
    
    def distance(self,x,w,ip,op):
        dist=zeros([op,1])
        t=0
        for i in range(0,op):
            item=0
            for j in range(0,ip):
                
                s=x[j][0]
                
                
                t=w[i][j]
                #print("\n\nt is",t,"\n\n" )
                
                item=s-t
                
                dist[i][0]+=pow(item,2)
                
            dist[i][0]=math.sqrt(dist[i][0])
        print("dist is ",dist)
        return dist
    
    def min_dist(self,dist):
        m=dist[0][0]
        win=0
        for i in range(0,len(dist)):
            if(m>dist[i][0]):
                m=dist[i][0]
                win=i
        print("winner neuron layer is ",win)
        return m,win


    def variable_lmbda(self,lmbda,epoch,iter):
        f=lmbda/epoch

        vl=lmbda-(f*(iter+1))
        return vl



    def update(self,x,w,vl,win):

        for i in range(0,ip):
            w[win][i]=w[win][i]+vl*(x[i][0]-w[win][i])
        
        print("\nupdated w is\n ",w)
        
        return w

    def draw(w,x):
        pass






def train(ip,op,epoch,w):
    
    
    for i in tqdm(range(0,epoch)):

        x=kn.feeder(ip)

        dist=kn.distance(x,w,ip,op)

        m,win=kn.min_dist(dist)

        vl=kn.variable_lmbda(lmbda,epoch,i)

        w=kn.update(x,w,vl,win)



if __name__=='__main__':
    ip=2
    op=16
    opoch=1000
    lmbda=1

    q=0

    kn=kn()
    
    w=init(ip,op)

    while(q==0):
        epoch=1000
        if(epoch==0):
            break

        train(ip,op,epoch,w)






        
        
        
        
