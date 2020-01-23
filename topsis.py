# -*- coding: utf-8 -*-
"""
Created on Mon Jan 20 23:28:39 2020

@author: naman
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
   
def normalize_matrix(filename):
    #looks_dict={'Low':1,'Below Average':2,'Average':3,'Good':4,'Excellent':5}
    data=pd.read_csv(filename)
    data=data.replace(to_replace =["Good","Low","Average","Excellent","Below Average"], value =[4,1,3,5,2])
    x=data.iloc[:,1:]
    y=x.values
    z=data.iloc[:,0].values
    #print(y.dtype)
    y=y.astype("float64")
    
    s=[]
    n1=len(y)
    n2=len(y[0])
    for i in range(n2): #for columns
        sum1=0;
        for j in range(n1): #for rows
            sum1+=y[j][i]*y[j][i]
        s.append(sum1) 
        
    for i in range(len(s)):
         s[i]=np.sqrt(s[i])
    
    for i in range(n2):#for columns
        for j in range(n1): #for rows
            y[j][i]=y[j][i]/s[i]
    return (y,z);    
    
def weighted_matrix(y,e):
    w=e.split(',')
    #print(w)          #string to list
    w=[float(i) for i in w]
    sum=0
    for i in range(len(w)):
        sum+=w[i];
    sum
    for i in range(len(w)):
        w[i]=(w[i]/sum);
        #print(w)
    n1=len(y)
    n2=len(y[0])
    for i in range(n2):
        for j in range(n1):
            y[j][i]=y[j][i]*w[i];       
    return y;

def vj(y,impacts):
    #impacts="+,+,-,+"
    impacts=list(impacts.split(","))
    vg_plus=[]
    vg_minus=[]
    n1=len(y)
    n2=len(y[0])
    for i in range(n2):
            if(impacts[i]=="+"):
                vg_plus.append(max(y[:,i]))
                vg_minus.append(min(y[:,i]))
            else:
                vg_plus.append(min(y[:,i]))
                vg_minus.append(max(y[:,i]))        
    return(vg_plus,vg_minus)  
    
def separation_positive(y,vg_plus):
    n1=len(y)
    n2=len(y[0])
    sg_plus=[]
    for i in range(n1):
        sum1=0
        for j in range(n2):
            sum1+=(vg_plus[j]-y[i][j])**2
        sg_plus.append(sum1**0.5)    
    sg_plus=np.array(sg_plus)
    return sg_plus

def separation_negative(y,vg_minus):
    n1=len(y)
    n2=len(y[0])
    sg_minus=[]
    for i in range(n1):
        sum1=0
        for j in range(n2):
            sum1+=(vg_minus[j]-y[i][j])**2
        sg_minus.append(sum1**0.5) 
    sg_minus=np.array(sg_minus)
    return sg_minus
      
def performance_score(sg_plus,sg_minus):
    score = []
    score = sg_minus/(sg_plus + sg_minus)
    return score

"""def final_ranking(score):
    n1=len(score)
    k=score
    k.sort(reverse=True)
    dicti={}
    for i in range(0,n1):
        dicti[k[i]]=n1-i
    return score  """
 
def main():
    import sys
    import pandas as pd
    total = len(sys.argv)
    if (total!=4):
        print("ERROR! WRONG NUMBER OF PARAMETERS")
        print("USAGES: $python <programName> <dataset> <weights array> <impacts array>")
        print('EXAMPLE: $python programName.py data.csv "1,1,1,1" "+,+,-,+" ')
        exit(1)
    (z,p)=normalize_matrix(sys.argv[1])
    #print(sys.argv[2])
    x=weighted_matrix(z,sys.argv[2])
    (c,d)=vj(x,sys.argv[3])
    v=separation_positive(x,c)
    b=separation_negative(x,d)
    n=performance_score(v,b)
    #m=final_ranking(n)
    for i in range(len(p)):
        print(p[i],'-',n[i])
    
main()
    
    
    
    
    
    
     
     

  
    
    
    