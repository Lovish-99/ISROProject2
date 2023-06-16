#importing libraries and modules
import time
import datetime
import hashlib
from urllib.request import urlopen, Request
from bs4 import BeautifulSoup
import pandas as pd
from time import gmtime, strftime
import os
import csv
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import matplotlib as mpl
from matplotlib.pyplot import figure

#function for genrating the list that contains the directory folders names
def item_list():
    #request and open the required url
    url = urlopen("http://125.19.52.218/realtime/")

    #make BeautifulSoup object
    soup = BeautifulSoup(url, "html.parser")

    #find the needed info using bs4 object
    m3 = soup.find_all("div", {"class" : "tableData"})

    master_list1 = []

    #create list of water sample other details
    for element in m3:
        temp_dic={}
        m4=element.find_all("tr")
        for ele in m4:
            try:
                master_list1.append(ele.find("td").text.strip())
            except:
                continue
    list_set = set(master_list1)
    master_list = list(list_set)
    
    #making a csv file of parameter names for future use
    master_list2 = []
    for para in master_list:
        temp_dic2 = {}
        temp_dic2['Parameters'] = para
        master_list2.append(temp_dic2)
    d = pd.DataFrame(master_list2)
    d.to_csv("static/RuntimeS1/Parameter's.csv",index=True)
    
    names = []
    for i in master_list:
        i = i.replace("/","_")
        names.append(i)
    return names

#function for creating graphs for updated csv files 
def create_graph2(name,loc):
    name2 = name.replace("_","/")
    try:
        plt.figure(figsize=(14,11))
        plt.title('Analysis of Parameter: {}'.format(name2), fontdict={ 'fontsize': 23 })
        plt.ylabel(name2, fontdict={ 'fontsize': 18 })
        plt.xlabel("Time", fontdict={ 'fontsize': 18 })
        df = pd.read_csv("static/RuntimeS1/{}/Location{}/Data.csv".format(name,str(loc)))
        g = sns.lineplot(x = "DateTime", y = name2,color="red", data = df)
        g = sns.scatterplot(x = "DateTime", y = name2,marker="v",color="red", data = df, s=100)
        labels = g.get_xticklabels()
        plt.setp(labels, rotation = 90, horizontalalignment = 'right')
        plt.savefig('static/RuntimeS1/{}/Location{}/Data.jpeg'.format(name,str(loc)),bbox_inches='tight')
        mpl.rc('figure', max_open_warning = 0)
        plt.close('figure')
    except Exception as e:
        print("error : ", e)

#function for generating the updated csv files for the scraped data 
def create_csv2():
    #request and open the required url
    url = urlopen("http://125.19.52.218/realtime/")
    #make BeautifulSoup object
    soup = BeautifulSoup(url, "html.parser")
    
    #find the needed info using bs4 object
    m3 = soup.find_all("div", {"class" : "tableData"})
    
    #create datetime object
    now = datetime.datetime.now()
    
    #initilizing the variable k
    k = 1
    
    #calling the item-list function and replacing the list names element with specified value
    master_list3 = item_list()
    names=[]
    for j in master_list3:
        j = j.replace("_","/")
        names.append(j)
        
    #create list of water sample other details
    for element in m3:
        temp_dic={}
        l = 0
        m4=element.find_all("tr")
        for ele in m4:
            try:
                #finding the required data
                temp_dic[ele.find("td").text.strip()]=ele.find_all("td")[-1].text.strip()
            except:
                continue
        #checking whether the dictionary is empty or not
        if temp_dic!={}:
            for i in names:
                l1 = []
                temp_dic2 = {}
                temp_dic2["DateTime"] = now.strftime('%d %b %H:%M')
                temp_dic2["Date"] = now.strftime('%d %b %Y')
                temp_dic2["Time"] = now.strftime('%H:%M:%S')
                temp_dic2[i]=temp_dic.get(i,"")
                
                #read the previously generated csv file
                df1=pd.read_csv('static/RuntimeS1/{}/Location{}/Data.csv'.format(master_list3[l],str(k)))
                #converting the data into list of dictionary
                a=df1.to_dict("records")
                try:
                    #eleminating unwanted column generated due to the "".read_csv method"
                    del a[-1]["Unnamed: 0"]
                except:
                    pass
                try:
                    x = float(temp_dic2[i])
                except:
                    #chaning the nan/empty string with a value(0.0)
                    temp_dic2[i]=0.0
                
                #checking for the updation of data    
                if float(a[-1].get(i,"0.0")) != float(temp_dic2.get(i,"0.0")): 
                    #adding updated data to list of dictionary
                    a.append(temp_dic2)
                    #craete a panda dataframe
                    df2=pd.DataFrame(a)
                    #genrating the updated data csv file
                    df2.to_csv('static/RuntimeS1/{}/Location{}/Data.csv'.format(master_list3[l],str(k)), index=False)
                    create_graph2(master_list3[l],k)
                    time.sleep(5)
                l = l + 1
            k = k + 1