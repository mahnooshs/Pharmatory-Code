# -*- coding: utf-8 -*-
"""
Created on Sun Feb 24 10:40:53 2019

@author: m7979
"""
#Defining dictionary and an integer for the rest of the code
import sys
import csv
content =[]
dct={}
i=1

#Reading in the data as a comma delimited text
file= csv.reader(open(sys.argv[1],'r'), delimiter=',')
next(file, None)
for line in file:
    content.append(line)
pharm = content

medical= [0]*len(pharm)
for i in range(len(pharm)):
    medical[i]=[0, '', '', 0]

#Combining first name and last name to get full name

for i in range(len(pharm)): 
    medical[i][3] = float(pharm[i][4])
    medical[i][2] = pharm[i][3]
    medical[i][1] = pharm[i][1] + ' ' +pharm[i][2]
    

#Making a list of the name of drugs by creating a dictionary and a for loop   
for drug in medical:
    dct.setdefault(drug[2],[]).append(drug)     
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
        totcost[i]=totcost[i]+int(dct[med[i]])[j][3]


#Creating a dataset that includes all the info that I created
data=[0]*(len(med))
for i in range (len(med)):
    data[i]= ['',0,0]
#Filling out the data with the info that I extracted from the initial dataset
for i in range (len(med)):
    data[i][0]= med[i]
    data[i][1]= indiv[i]
    data[i][2]=totcost[i]
 #Sorting data first based on the name and then based on the cost (to make sure cost comes first and then drugs are sorted by alphabet)   
data.sort(key=lambda x: x[1])    
data.sort(key=lambda x: x[0], reverse=True)    

#Inserting column names
data.insert(0,['drug_name','num_prescriber','total_cost'])   
#IF YOU PRINT data, it is the output!
#Creating output file in the directory
with open(sys.argv[2], 'w') as output:
    csv.writer(output).writerows(data)

#in case you want to get a text file as output please run follosing codes
#with open(sys.argv[2], 'w') as output:
 #  for item in data:
  #    output.write("%s\n" % item)
        

