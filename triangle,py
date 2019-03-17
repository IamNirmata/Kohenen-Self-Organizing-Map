# -*- coding: utf-8 -*-
"""
Created on Wed Mar 13 03:46:53 2019

@author: sreeh
"""

from matplotlib import pyplot as plt
from numpy import zeros
import numpy  as np
import random
import math
from tqdm import tqdm
import matplotlib.animation as animation
from matplotlib import style

  
def init(ip,op):
    ############################################################ 
    #w is randomly defined
    w= zeros([op,ip])
    
    for i in range(0,op):
        
        for j in range(0,ip):
            w[i][j]=random.uniform(0,500)
            
    #print(w)
    return w



class kn():
  
    
    def feeder(self,ip):
        
        x=zeros([ip,1])
        a=0
        
        while(a==0):
            p1=random.uniform(0,500)
            p2=random.uniform(0,500)
            l=p1-250
            m=p2-250
            if(p1>p2):
                x[0][0]=p1
                x[1][0]=p2
                a=1
        #print("x is ",x)
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
                
            #dist[i][0]=math.sqrt(dist[i][0])
        #print("dist is ",dist)
        return dist
    
    def min_dist(self,dist,pick):
        m=dist[0][0]
        win=0
        for i in range(0,len(dist)):
            if(m>dist[i][0]):
                m=dist[i][0]
                win=i
        #print("winner neuron layer is ",win)
        pick.append(win)
        return m,win,pick


    def variable_lmbda(self,lmbda,epoch,iter):
        f=lmbda/epoch

        vl=lmbda-(f*(iter+1))
        return vl



    def update(self,x,w,vl,win):

        for i in range(0,ip):
            w[win][i]=w[win][i]+vl*(x[i][0]-w[win][i])
        
        #print("\nupdated w is\n ",w)
        
        return w

    def draw(self,w,pick):
        p=[]
        q=[]
        for i in pick:
            p.append(float(w[i][0]))
            q.append(float(w[i][1]))
        #print(p,q)
        fig = plt.figure()
        #plt.clf()
        plt.scatter(p,q,label='kohenen',color='k',s=30,marker="x")
        plt.xlim(0,500)
        plt.ylim(0,500)
        plt.pause(1)
        plt.show

def train(ip,op,epoch,w,lmbda):
    
    pick=[]
    for i in tqdm(range(0,epoch)):

        x=kn.feeder(ip)

        dist=kn.distance(x,w,ip,op)

        m,win,pick=kn.min_dist(dist,pick)

        vl=kn.variable_lmbda(lmbda,epoch,i)
        
        w=kn.update(x,w,vl,win,)
        
        if(i%1000==0):
            kn.draw(w,pick)
    return w,pick

if __name__=='__main__':
    ip=2
    op=100
    epoch=10000
    lmbda=.1
    q=0

    kn=kn()
    
    w=init(ip,op)

    while(q==0):
        
        if(epoch==0):
            break
        #kn.draw(w)
        w,pick=train(ip,op,epoch,w,lmbda)
        w=kn.draw(w,pick)
        #q=int(input("Training is done,press 0 to continue , 1 to quit:"))
        break




        
        
        
        
