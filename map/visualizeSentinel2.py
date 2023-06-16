# import the python modules
import os
import rasterio as rio
from osgeo import gdal
import matplotlib.pyplot as plt
import numpy as np

def visual():
    # setting up the path variable value
    path = "C:/Users/Admin/S2B_MSIL2A_20211230T053229_N0301_R105_T43QEG_20211230T071727.SAFE/GRANULE/L2A_T43QEG_A025156_20211230T053226/IMG_DATA/R10m"
    # taking input from the user
    dir_list = os.listdir(path)

    # print the files that are avaiable in path
    print("Files and directories in '", path, "' :")
    
    # prints all files
    print(dir_list)

    # read the downloaded files
    RIO = "C:/Users/Admin/S2B_MSIL2A_20211230T053229_N0301_R105_T43QEG_20211230T071727.SAFE/GRANULE/L2A_T43QEG_A025156_20211230T053226/IMG_DATA/R10m"

    # set path for the downloaded file 
    dir_list = os.listdir(path)
    l2 = []
    # for i in range(1, len(dir_list) + 1):
    #     b_i = rio.open(RIO + '/' + dir_list[i-1])
    #     l2.append(b_i)
        
    # convert the .jp2 data file in th eform of .tiff
    b4 = rio.open(RIO + '/T43QEG_20211230T053229_B04_10m.jp2')
    b3 = rio.open(RIO + '/T43QEG_20211230T053229_B03_10m.jp2')
    b2 = rio.open(RIO + '/T43QEG_20211230T053229_B02_10m.jp2')


    # Create an RGB image 
    with rio.open('RGB2.tiff','w',driver='Gtiff', width=b4.width, height=b4.height, 
                count=3,crs=b4.crs,transform=b4.transform, dtype=b4.dtypes[0]) as rgb:
        rgb.write(b2.read(1),1) 
        rgb.write(b3.read(1),2) 
        rgb.write(b4.read(1),3) 
        rgb.close()

    # open/read .tiff fileaone aap
    dataset = gdal.Open(r'RGB.tiff')
    print(dataset.RasterCount)
    # since there are 3 bands
    # we store in 3 different variables
    band1 = dataset.GetRasterBand(1) # Red channel
    band2 = dataset.GetRasterBand(2) # Green channel
    band3 = dataset.GetRasterBand(3) # Blue channel
    b1 = band1.ReadAsArray()
    b2 = band2.ReadAsArray()
    b3 = band3.ReadAsArray()
    img = np.dstack((b1, b2, b3))
    f = plt.figure()
    plt.imshow(img)
    plt.savefig('Tiff22.png')
    plt.show()