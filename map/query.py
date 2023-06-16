# importing required modules and packages
import wget
import os
import optparse
from xml.dom import minidom
from zipfile import ZipFile

# fix the variables value for the entire code like:
# setting the wget querry command parameter
# setting the certificate values 
# set the username and password of open access hub for downloading the data
# set up the download querry
wg = "wget --no-check-certificate "
wg2 = "wget --content-disposition --continue "
auth = "--user={username} --password={password} ".format(username = "Luv", password = "28w_5FKMBE$xZWu")
search_output1 = "--output-document="
search_output2 = "query_{pform}_{ptype}_{plat}_{plon}_{st}.xml "
url_search = "https://scihub.copernicus.eu/apihub/search?q="
url_download = "https://scihub.copernicus.eu/dhus/odata/v1/"
temp_dic = {}

# function for downling the specific sentinel data file
def download_data_set(product_id):
    try:
        query1 = "Products('{}')/$value".format(product_id)
        command2 = '%s %s "%s%s"' % (wg2, auth, url_download, query1)
        print(command2)
        os.system(command2)
    except:
        print("ok")

# creating the function for unzipping the downloaded zip file
def unzip(file_name):
    try:
        with ZipFile(file_name, 'r') as zip:
            #zip.printdir()
            print('Extracting all the files now...')
            zip.extractall()
            print('Done!')
    except:
        print("ok")
        
# creating the function for getting the required "product id"
def get_id(fname):
    #try:
    # read the file in xml format
    xml = minidom.parse(fname.strip())
    
    # make a list of entry tag elements
    products = xml.getElementsByTagName("entry")
    #print(products)
    
    # check weather the procduct array has element or not  
    if products != []:
        for prod in products:
            # get the id of the desired product from the created querry file
            Id = prod.getElementsByTagName("id")[0].firstChild.data
            
            # get the filename of the desired product from the created querry file
            filename = prod.getElementsByTagName("title")[0].firstChild.data
           
            # print the grabed values
            print("Product Id is: ", Id)
            print("Filename is: ", filename)
            
            # get the zip file name 
            # for unzipping the downloaded zip file
            file_name = filename + ".zip"
             
            # make a dictionary for storing the details   
            temp_dic["id"] = Id
            temp_dic["file"] = file_name
            
            # check for the directory
            # exists or not    
            if os.path.exists(file_name):
                print("Already Downloaded")
                temp_dic["status"] = True
                return temp_dic
            else:
                print("Downloading starts...")
                #download_data_set(Id, user, passd)
                print("Downloading ends...")
                temp_dic["status"] = False
                return temp_dic
                #unzip(file_name)
            break
    else:
        print("Sentinel Data info is not found on the server for this query.")
        return temp_dic
    # except:
    #     print("ok")
    #     return temp_dic

# creating the function for getting the required "product id"
def get_id2(fname):
    #try:
    #print("hello")
    #print(fname)
    # read the file in xml format
    xml = minidom.parse(fname.strip())
    
    # make a list of entry tag elements
    products = xml.getElementsByTagName("entry")
    #print(products)
    
    # check weather the procduct array has element or not 
    if products != []:
        for prod in products:
            # get the id of the desired product from the created querry file
            Id = prod.getElementsByTagName("id")[0].firstChild.data
            
            # get the filename of the desired product from the created querry file
            filename = prod.getElementsByTagName("title")[0].firstChild.data
            print("Product Id is: ", Id)
            print("Filename is: ", filename)
            
            # get the zip file name 
            # for unzipping the downloaded zip file
            file_name = filename + ".zip"
            
            # make a dictionary for storing the details 
            temp_dic["id"] = Id
            temp_dic["file"] = file_name
            print("Downloading starts...")
            print("Downloading ends...")
            temp_dic["status"] = True
            return temp_dic
            break
    else:
        print("Sentinel Data info is not found on the server for this query.")
        return temp_dic
    # except:
    #     print("ok")
    #     return temp_dic
    
# creating the function for generating the querry file
# for downloading the Sentinel data  from opem hub
def query_search(platform, productType, latmin, latmax, lonmin, lonmax, ingesTime1, ingesTime2, cloudpr, prmode, srmode):
    try:
        # setting variable value for platformname
        if productType != "None" and platform != "None":
            qr = "platformname:{} AND producttype:{} ".format(platform, productType)
        elif productType == "None" and platform != "None":
            qr = "platformname:{} ".format(platform)
        elif productType != "None" and platform == "None":
            qr = "producttype:{} ".format(productType)
        else:
            qr=""
        
        # setting variable value for coordinates
        if qr != "":   
            if latmin!=0 and lonmin!=0 and latmax!=0 and lonmax!=0:
                qr1 = "AND footprint: %22Intersects(POLYGON(({lonmin} {latmin}, {lonmax} {latmin}, {lonmax} {latmax}, {lonmin} {latmax}, {lonmin} {latmin})))%22 ".format(latmin=latmin, latmax=latmax, lonmin=lonmin, lonmax=lonmax)
            elif (latmin != 0 and latmax == 0) and (lonmin != 0 and lonmax == 0):
                qr1 = "AND footprint: %22Intersects({latmin}, {lonmin})%22 ".format(latmin=latmin, lonmin=lonmin)
            elif (latmin == 0 and latmax != 0) and (lonmin == 0 and lonmax != 0):
                qr1 = "AND footprint: %22Intersects({latmax}, {lonmax})%22 ".format(latmax=latmax, lonmax=lonmax)
            else:
                qr1 = ""
        else:
            if latmin!=0 and lonmin!=0 and latmax!=0 and lonmax!=0:
                qr1 = "footprint: %22Intersects(POLYGON(({lonmin} {latmin}, {lonmax} {latmin}, {lonmax} {latmax}, {lonmin} {latmax}, {lonmin} {latmin})))%22 ".format(latmin=latmin, latmax=latmax, lonmin=lonmin, lonmax=lonmax)
            elif (latmin != 0 and latmax == 0) and (lonmin != 0 and lonmax == 0):
                qr1 = "footprint: %22Intersects({latmin}, {lonmin})%22 ".format(latmin=latmin, lonmin=lonmin)
            elif (latmin == 0 and latmax != 0) and (lonmin == 0 and lonmax != 0):
                qr1 = "footprint: %22Intersects({latmax}, {lonmax})%22 ".format(latmax=latmax, lonmax=lonmax)
            else:
                qr1 = ""
            
        # setting variable value for start time and end time
        if ingesTime1 != "None" and ingesTime2!= "None" and (qr != "" or qr1 != ""):
            #qr2 = "And ingestiondate:[NOW-{}MONTHS TO NOW]".format(ingesTime)
            qr2 = "AND ingestiondate:[{}T00:00:00.000Z TO {}T00:00:00.000Z]".format(ingesTime1, ingesTime2)
        elif ingesTime1 != "None" and ingesTime2!= "None":
            qr2 = "ingestiondate:[{}T00:00:00.000Z TO {}T00:00:00.000Z]".format(ingesTime1, ingesTime2)
        else:
            qr2 = ""
        
        # checking for "Sentinel-1 data"
        if platform == "Sentinel-1":
            if prmode != "None" and srmode != "None":
                qr3 = "AND polarisationmode:{} AND sensoroperationalmode:{} ".format(prmode, srmode)
                query = qr + qr1 + qr3 + qr2
            elif prmode != "None" and srmode == "None":
                qr3 = "AND polarisationmode:{} ".format(prmode)
                query = qr + qr1 + qr3 + qr2
            elif prmode == "None" and srmode != "None":
                qr3 = "AND sensoroperationalmode:{} ".format(srmode)
                query = qr + qr1 + qr3 + qr2 
            else:
                query = qr + qr1 + qr2
        # checking for "Sentinel-2 data"
        elif platform == "Sentinel-2":
            if cloudpr != "None":
                qr5 = "AND cloudcoverpercentage:{}".format(int(cloudpr))
                query = qr + qr1 + qr2 + qr5
            else:
                query = qr + qr1 + qr2
        # checking for "Sentinel-3 data"
        else:
            query = qr + qr1 + qr2
        
        # naming the file generated by operating search query
        search_out = search_output2.format(pform=platform, ptype=productType, plat=latmax, plon=lonmax, st=ingesTime1)
        search_out2 = search_output1 + search_out
        
        # generating the complete search querry for creating search query text file 
        command = '%s %s %s "%s%s&rows=%d"' % (wg, auth, search_out2, url_search, query, 1)
        print(command)
        print(search_out)
        if os.path.exists(search_out):
            keypair = get_id2(search_out)
            return keypair
        else:
            os.system(command)
            keypair = get_id(search_out)
            return keypair
    
    except:
        print("ok")
