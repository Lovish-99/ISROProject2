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

#function that return the available parameters on a site
def element_name():
    master_list = ["Dissolved Oxygen","Bio Chemical Oxygen Demand","Total Coliform","pH"]
    return master_list

#function to create graphs for the updated csv files
def create_graph2(name,loc):
    try:
        plt.figure(figsize=(14,11))
        plt.title('Analysis of Parameter: {}'.format(name), fontdict={ 'fontsize': 23 })
        plt.ylabel(name, fontdict={ 'fontsize': 18 })
        plt.xlabel("Time", fontdict={ 'fontsize': 18 })
        df = pd.read_csv("static/RuntimeS/Runtime/{}/Location{}/Data.csv".format(name,str(loc)))
        g = sns.lineplot(x = "Time", y = name,color="red", data = df)
        g = sns.scatterplot(x = "Time", y = name,marker="v",color="red", data = df, s=100)
        labels = g.get_xticklabels()
        plt.setp(labels, rotation = 90, horizontalalignment = 'right')
        plt.savefig('static/RuntimeS/Runtime/{}/Location{}/Data.jpeg'.format(name,str(loc)),bbox_inches='tight')
        mpl.rc('figure', max_open_warning = 0)
        plt.close('figure')
    except Exception as e:
        print("error : ", e)

#function for generating the updated csv files for the scraped data 
def create_csv():
    #getting the url
    url = urlopen("http://125.19.52.219/wqi/")

    #creating BeautifulSoup Object
    soup = BeautifulSoup(url, "html.parser")

    #get the required data using soup object fron script tag
    scrt = soup.find_all("script")
    #converting the script tag data in string and replacing '\n' & '\t' tags
    final_str=str(scrt[1]).replace("\n","")
    final_str=final_str.replace("\t","")
    
    #craeting the datetime object
    now = datetime.datetime.now()
    
    #extracting required data using string index method
    for i in range(1,93):
        #finding the indicies of the required data from the scraped data
        index=final_str.index("google.maps.LatLng(")
        index2 = final_str.index('class="head">')
        index3 = final_str.index("Monitoring")
        index4 = final_str.index("Sampling Month")
        index5 = final_str.index("Dissolved Oxygen")
        index6 = final_str.index("Bio Chemical Oxygen Demand")
        index7 = final_str.index("Total Coliform")
        index8 = final_str.index("pH")
        
        #--------------------------------------setting values of dictionary----------------------------------------------
        temp_dic2 = {}
        temp_dic2["Frequency Of Monitoring"] = final_str[index3+11:index3+30].split("<")[0]
        temp_dic2["Sampling Month"] = final_str[index4+15:index4+23]
        temp_dic2["Date"] = now.strftime('%d %b %Y')
        temp_dic2["Time"] = now.strftime('%d %b %H:%M')
        
        if index5 < index6:
            temp_dic2["Dissolved Oxygen"] = final_str[index5+18:index5+22].split("<")[0]
        else:
            temp_dic2["Dissolved Oxygen"] = 0 
            
        #read the previously generated csv file
        df1=pd.read_csv("static/RuntimeS/Runtime/Dissolved Oxygen/Location{}/Data.csv".format(str(i)))
        #converting the data into list of dictionary
        a=df1.to_dict("records")
        #print(a)
        try:
            #eleminating unwanted column generated due to the "".read_csv method"
            del a[-1]["Unnamed: 0"]
        except:
            pass
        
        #checking for the updation of data
        if float(a[-1]["Dissolved Oxygen"]) != float(temp_dic2["Dissolved Oxygen"]): 
            print(a[-1]['Dissolved Oxygen'],temp_dic2['Dissolved Oxygen'])
            #adding updated data to list of dictionary
            a.append(temp_dic2)
            #create a dataframe
            df2=pd.DataFrame(a)
            #genrating the updated csv file
            df2.to_csv('static/RuntimeS/Runtime/Dissolved Oxygen/Location{}/Data.csv'.format(str(i)), index=False)
            create_graph2("Dissolved Oxygen",i)

        #--------------------------------------setting values of dictionary----------------------------------------------
        temp_dic3 = {}
        temp_dic3["Frequency Of Monitoring"] = final_str[index3+11:index3+30].split("<")[0]
        temp_dic3["Sampling Month"] = final_str[index4+15:index4+23]
        temp_dic3["Date"] = now.strftime('%d %b %Y')
        temp_dic3["Time"] = now.strftime('%d %b %H:%M')
        if index6 < index7:
            temp_dic3["Bio Chemical Oxygen Demand"] = final_str[index6+28:index6+34].split("<")[0]
        else:
            temp_dic3["Bio Chemical Oxygen Demand"] = 0
        
        #read the previously generated csv file
        df3=pd.read_csv("static/RuntimeS/Runtime/Bio Chemical Oxygen Demand/Location{}/Data.csv".format(str(i)))
        #converting the data into list of dictionary
        b=df3.to_dict("records")
        try:
            #eleminating unwanted column generated due to the "".read_csv method"
            del b[-1]["Unnamed: 0"]
        except:
            pass
        
        #checking for the updation of data
        if float(b[-1]["Bio Chemical Oxygen Demand"]) != float(temp_dic3["Bio Chemical Oxygen Demand"]): 
            print(b[-1]["Bio Chemical Oxygen Demand"],temp_dic3["Bio Chemical Oxygen Demand"])
            #adding updated data to list of dictionary
            b.append(temp_dic3)
            #create a dataframe
            df4=pd.DataFrame(b)
            #genrating the updated csv file
            df4.to_csv('static/RuntimeS/Runtime/Bio Chemical Oxygen Demand/Location{}/Data.csv'.format(str(i)), index=False)
            create_graph2("Bio Chemical Oxygen Demand",i)
        
        #--------------------------------------setting values of dictionary----------------------------------------------
        temp_dic4 = {}
        temp_dic4["Frequency Of Monitoring"] = final_str[index3+11:index3+30].split("<")[0]
        temp_dic4["Sampling Month"] = final_str[index4+15:index4+23]
        temp_dic4["Date"] = now.strftime('%d %b %Y')
        temp_dic4["Time"] = now.strftime('%d %b %H:%M')
        if index7 < index8:
            temp_dic4["Total Coliform"] = final_str[index7+16:index7+25].split("<")[0]
        else:
            temp_dic4["Total Coliform"] = 0
        
        #read the previously generated csv file
        df5=pd.read_csv("static/RuntimeS/Runtime/Total Coliform/Location{}/Data.csv".format(str(i)))
        #converting the data into list of dictionary
        c=df5.to_dict("records")
        try:
            #eleminating unwanted column generated due to the "".read_csv method"
            del c[-1]["Unnamed: 0"]
        except:
            pass
        
        #checking for the updation of data
        if float(c[-1]["Total Coliform"]) != float(temp_dic4["Total Coliform"]): 
            print(c[-1]['Total Coliform'],temp_dic4['Total Coliform'])
            #adding updated data to list of dictionary
            c.append(temp_dic4)
            #create a dataframe
            df6=pd.DataFrame(c)
            #genrating the updated csv file
            df6.to_csv('static/RuntimeS/Runtime/Total Coliform/Location{}/Data.csv'.format(str(i)), index=False)
            create_graph2("Total Coliform",i)

        #--------------------------------------setting values of dictionary----------------------------------------------
        temp_dic5 = {}
        temp_dic5["Frequency Of Monitoring"] = final_str[index3+11:index3+30].split("<")[0]
        temp_dic5["Sampling Month"] = final_str[index4+15:index4+23]
        temp_dic5["Date"] = now.strftime('%d %b %Y')
        temp_dic5["Time"] = now.strftime('%d %b %H:%M')
        if index8 < (index + 300): 
            temp_dic5["pH"] = final_str[index8+4:index8+10].split("<")[0]
        else:
            temp_dic5["pH"] = 0
        
        #read the previously generated csv file
        df7=pd.read_csv("static/RuntimeS/Runtime/pH/Location{}/Data.csv".format(str(i)))
        #converting the data into list of dictionary
        d=df7.to_dict("records")
        try:
            #eleminating unwanted column generated due to the "".read_csv method"
            del d[-1]["Unnamed: 0"]
        except:
            pass
        
        #checking for the updation of data
        if float(d[-1]["pH"]) != float(temp_dic5["pH"]): 
            print(d[-1]['pH'],temp_dic5['pH'])
            d.append(temp_dic5)
            #create a dataframe
            df8=pd.DataFrame(d)
            #genrating the updated csv file
            df8.to_csv('static/RuntimeS/Runtime/pH/Location{}/Data.csv'.format(str(i)), index=False)
            create_graph2("pH",i)
        
        #changing the value of index in order to extract the next location data
        final_str=final_str[index+300:]