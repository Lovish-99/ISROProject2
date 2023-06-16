# chat/consumers.py
# importing the modules
import json
import time
from channels.generic.websocket import WebsocketConsumer
from .query import *

# declare chatconsumer class
# for starting the work
class ChatConsumer(WebsocketConsumer):
    # function for connecting the socket
    def connect(self):
        self.accept()

    # function for breaking the signal from the socket
    def disconnect(self, close_code):
        pass
        
    # function for receiving the signals from the browser
    def receive(self, text_data):
        text_data_json = json.loads(text_data)
        message = text_data_json['message']
        starttime = text_data_json['key1']
        endtime = text_data_json['key2']
        point = text_data_json['key3']
        plateform = text_data_json['key4']
        prodtype = text_data_json['key5']
        polarmode = text_data_json['key6']
        sensormode = text_data_json['key7']
        cloudper = text_data_json['key8']
        self.send(text_data=json.dumps({
            'message': message,
            'key1': starttime,
            'key2': endtime,
            'key3': point,
            'key4': plateform,
            'key5': prodtype,
            'key6': polarmode,
            'key7': sensormode,
            'key8': cloudper
        }))
        
        # logic starts......
        # for getting the co-ordinates from the web server
        arr = []
        latlng = point.split(",")
        print(latlng)
        if len(latlng) > 2:
            l2 = latlng
            for i in range(0, len(latlng)-1):
                c = float(l2[i].strip().split(".")[0][0:2] + "." + l2[i].strip().split(".")[0][2:4])
                arr.append(c)
            #return master_list
            print(arr)    
        else:
            l2 = latlng
            for i in range(0, len(latlng)):
                c = float(l2[i].strip().split(".")[0][0:2] + "." + l2[i].strip().split(".")[0][2:4])
                arr.append(c)
            #return master_list
            print(arr) 
        # logic ends......
        
        print(starttime, endtime, point, plateform, prodtype, polarmode, sensormode, cloudper)
        #  sending the parameter values to
        # the sendRepeatedMessage function of the web socket
        self.sendRepeatedMessage(text_data, arr)
    
    # sending the process status on the browser
    def sendRepeatedMessage(self, text_data, arr):
        time.sleep(10)
        text_data_json = json.loads(text_data)
        ss = len(arr)
        if ss == 2:
            valuee = query_search(text_data_json['key4'], text_data_json['key5'], arr[1], 0.0, arr[0], 0.0, text_data_json['key1'], text_data_json['key2'], text_data_json['key8'], text_data_json['key6'], text_data_json['key7'])
        else:
            valuee = query_search(text_data_json['key4'], text_data_json['key5'], arr[1], arr[ss-1], arr[0], arr[ss-2], text_data_json['key1'], text_data_json['key2'], text_data_json['key8'], text_data_json['key6'], text_data_json['key7'])
        print(valuee)
        
        print("1")
        self.send(text_data=json.dumps({
            'message': "Search Start"
        }))
        time.sleep(10)
        
        # showing status of downloading the sentinel product
        print("2")
        if valuee != {}:
            fileid = valuee["id"]
            filename = valuee["file"]
            self.send(text_data=json.dumps({
                'message': "Downloading Starts..."
            }))
            if valuee['status'] != True:
                download_data_set(fileid)
                self.send(text_data=json.dumps({
                    'message': "Work in progress..."
                }))
            else:
                self.send(text_data=json.dumps({
                    'message': "Downloading ends..."
                })) 
            time.sleep(10)
            
            # showing status of unziping the data
            print("3")
            if valuee['status'] == True:
                self.send(text_data=json.dumps({
                    'message': " Sentinel Data is available to use now..."
                }))
            else:
                self.send(text_data=json.dumps({
                    'message': " Sentinel Data is available to use after processing..."
                }))
                print(filename)
                unzip(filename)    
            time.sleep(10)
            
            # status of finishing the process
            print("4")
            self.send(text_data=json.dumps({
                'message': "Process Finishes..."
            }))
        else:
            self.send(text_data=json.dumps({
                'message': "Data not found..."
            }))
