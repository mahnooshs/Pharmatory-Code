# -*- coding: utf-8 -*-
"""
Created on Sun Feb 24 10:40:53 2019

@author: m7979
"""
#Defining dictionary and an integer for the rest of the code
import sys
dct={}
i=1
infile = sys.argv[1]
outfile = sys.argv[2]
#file = open(sys.argv[1],'r')
#Opening the text file
#file = open("..\\input\\itcont.txt",'r')
#Skiping the header line 
#next (file)
#Reading in the data as a comma delimited text
#content = file.readlines()

lines = []
with open(sys.argv[1]) as f:
    content = [line for line in f if line.strip()]
pharm=content
for i in range (len(pharm)):
    pharm[i] = pharm[i].split(",")

#Combining first name and last name to get full name
for i in range(len(content)): 
    pharm[i][1] = pharm[i][1] + ' ' +pharm[i][2]

#Making a list of the name of drugs by creating a dictionary and a for loop   
for drug in content:
    dct.setdefault(drug[3],[]).append(drug)     
med= list(dct.keys())

#Defining the objects that we are using during the rest of the code, the for loop is to make sure the length is sufficient
name=[1]*len(med)
totcost=[1]*len(med)
indiv=[1]*len(med)

for i in range ((len(med))):
    totcost[i]=0
    name[i]=[]
    indiv[i]=0
    
#Counting unique names of individuals that consumed each drug     
for i in range (len(med)):
    name=[0]*len(dct[med[i]])
    for j in range (len(dct[med[i]])):
                name[j]=(dct[med[i]])[j][1]  
    indiv[i]=len(name)-name.count([]) 
#Calculation the total cost for each drug based on dctionary values

for i in range (len(med)):
    for j in range (len(dct[med[i]])):
        #(x[i])[j]=float((dct[med[i]])[j][4])
        (dct[med[i]])[j][4]=float((dct[med[i]])[j][4])
#Total cost is as follows        
for i in range (len(med)):
    for j in range (len(dct[med[i]])):
        totcost[i]=totcost[i]+(dct[med[i]])[j][4]
        #totcost[i]=totcost[i]+(x[i])[j]
        
          
                
#Creating a dataset that includes all the info that I created
data=[0]*(len(med))
for i in range (len(med)):
    data[i]= ['',0,0]
#Filling out the data with the info that I extracted from the initial dataset
for i in range (len(med)):
    data[i][0]= med[i]
    data[i][1]= totcost[i]
    data[i][2]=indiv[i]
 #Sorting data first based on the name and then based on the cost (to make sure cost comes first and then drugs are sorted by alphabet)   
data.sort(key=lambda x: x[0])    
data.sort(key=lambda x: x[1], reverse=True)    

#Inserting column names
data.insert(0,['Drug','Total Cost','Unique Individuals'])   
#IF YOU PRINT data, IT is the output!
#Creating output file in the directory
with open(sys.argv[2], 'w') as output:
    for item in data:
        output.write("%s\n" % item)
        

