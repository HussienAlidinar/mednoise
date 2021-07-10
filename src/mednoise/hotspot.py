import tkinter as tk
from PIL import ImageTk, Image, ImageDraw
import ntpath
import glob2 as glob
from collections import OrderedDict
import datetime
import numpy as np
from scipy.spatial import distance

def about(header=False):
    if header==True:
        logo = """
        #############################################################################################
                                             8I                                                     
                                             8I                                                     
                                             8I                              gg                     
                                             8I                              ""                     
          ,ggg,,ggg,,ggg,    ,ggg,     ,gggg,8I   ,ggg,,ggg,     ,ggggg,     gg     ,g,      ,ggg,  
         ,8" "8P" "8P" "8,  i8" "8i   dP"  "Y8I  ,8" "8P" "8,   dP"  "Y8ggg  88    ,8'8,    i8" "8i 
         I8   8I   8I   8I  I8, ,8I  i8'    ,8I  I8   8I   8I  i8'    ,8I    88   ,8'  Yb   I8, ,8I 
        ,dP   8I   8I   Yb, `YbadP' ,d8,   ,d8b,,dP   8I   Yb,,d8,   ,d8'  _,88,_,8'_   8)  `YbadP' 
        8P'   8I   8I   `Y8888P"Y888P"Y8888P"`Y88P'   8I   `Y8P"Y8888P"    8P""Y8P' "YY8P8P888P"Y888
        #############################################################################################
        """
        print(logo)
        global storeddictionary
        global analyzedval
        storeddictionary = 1
        analyzedval = 1

    if header==False:
        logo = """
        #############################################################################################
                                             8I                                                     
                                             8I                                                     
                                             8I                              gg                     
                                             8I                              ""                     
          ,ggg,,ggg,,ggg,    ,ggg,     ,gggg,8I   ,ggg,,ggg,     ,ggggg,     gg     ,g,      ,ggg,  
         ,8" "8P" "8P" "8,  i8" "8i   dP"  "Y8I  ,8" "8P" "8,   dP"  "Y8ggg  88    ,8'8,    i8" "8i 
         I8   8I   8I   8I  I8, ,8I  i8'    ,8I  I8   8I   8I  i8'    ,8I    88   ,8'  Yb   I8, ,8I 
        ,dP   8I   8I   Yb, `YbadP' ,d8,   ,d8b,,dP   8I   Yb,,d8,   ,d8'  _,88,_,8'_   8)  `YbadP' 
        8P'   8I   8I   `Y8888P"Y888P"Y8888P"`Y88P'   8I   `Y8P"Y8888P"    8P""Y8P' "YY8P8P888P"Y888
        #############################################################################################
        Copyright 2021 Ravi Bandaru
        Licensed under the Apache License, Version 2.0 (the "License");
        you may not use this package except in compliance with the License.
        Unless required by applicable law or agreed to in writing, software
        distributed under the License is distributed on an "AS IS" BASIS,
        WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
        See the License for the specific language governing permissions and
        limitations under the License.
        #############################################################################################
        Welcome to mednoise, a python package that contains algorithms to handle and pre-process 
        large amounts of image-based metadata to remove noise and enhance the accuracy of machine
        learning and deep learning models for scientific research.
        #############################################################################################
        You can bring up the help menu (h) or exit (e).
        """
        print(logo)
        response = input("    ")
        print("    #############################################################################################")
        print("")
        if response == "e":
            print("    exiting.")
        if response == "h":
            print("    documentation can be accessed at https://mednoise.github.com.")
        print("")
        print("    #############################################################################################")
    if header != True and header != False:
        raise ValueError('header argument was incorrectly specified. note that it is a boolean attribute.')

about(True)


def hotspot_complete(filepath, x, y, find):
    files = glob.glob(filepath)
    for indexor, item in enumerate(files):
        name = ntpath.basename(files[indexor])
        size = len(name)
        mod_string = name[:size - 4]
        
        
        startTime = datetime.datetime.now().replace(microsecond=0)
        image = Image.open(files[indexor])
        rgb1 = image.convert('RGB')
        width, height = image.size
        pixel_values1 = list(rgb1.getdata())
        pixel_copy = pixel_values1
        endTime = datetime.datetime.now().replace(microsecond=0)
        durationTime = endTime - startTime        
        print ("md.hotspot_complete - Image " + str(indexor+1) + " Importing:" + str(durationTime))
        
        
        startTime = datetime.datetime.now().replace(microsecond=0)
        for index, item in enumerate(pixel_values1):
            if item != find:
                pixel_values1[index] = 2
            if item == find:
                pixel_values1[index] = 1
        endTime = datetime.datetime.now().replace(microsecond=0)
        durationTime = endTime - startTime        
        print("md.hotspot_complete - Image " + str(indexor+1) + " Converting:" + str(durationTime))
        
        
        startTime = datetime.datetime.now().replace(microsecond=0)
        pixel_values1 = np.array(pixel_values1)
        shape = (height, width)
        pixel_values2 = np.reshape(pixel_values1, shape)
        pixel_copy2 = np.reshape(pixel_copy, shape)
        const = (width*height)/100
        store = {}
        analyzedval = {}
        for w in range (x,width+1):
            for h in range (y,height+1):
                store[str(h-y)+":"+str(h)+", "+str(w-x)+":" + str(w)] = pixel_values2[h-y:h, w-x:w]
                a=(w-1)*height+h
                print(str(round((a)/(const),1)) + "%" , end = "\r")  
        endTime = datetime.datetime.now().replace(microsecond=0)
        durationTime = endTime - startTime        
        print("md.hotspot_complete - Image " + str(indexor+1) + " Hotspot Calculating:" + str(durationTime))
        
        
        startTime = datetime.datetime.now().replace(microsecond=0)
        for w in range (x,width):
            for h in range (y,height):
                keytocheck = store.get(str(h-y)+":"+str(h)+", "+str(w-x)+":" + str(w))
                stringforkey = str(h-y)+":"+str(h)+", "+str(w-x)+":" + str(w)
                
                if np.sum(keytocheck[0,:]) == x and np.sum(keytocheck[y-1,:]) == x and np.sum(keytocheck[:,0]) == y and np.sum(keytocheck[:,x-1]) == y:
                    valueforkey = True
                else:
                    valueforkey = False
                a=(w-1)*height+h
                print(str(round((a)/(const),1)) + "%" , end = "\r")
                analyzedval[stringforkey] = valueforkey
        endTime = datetime.datetime.now().replace(microsecond=0)
        durationTime = endTime - startTime        
        print("md.hotspot_complete - Image " + str(indexor+1) + " Hotspot Analyzing:" + str(durationTime))
        
        
        startTime = datetime.datetime.now().replace(microsecond=0) 
        fillmatrix = np.full((y, x), 1)
        for key, value in analyzedval.items():
            if value == True:
                txt = key
                splitter = txt.split(", ")
                split, splitone = splitter[0], splitter[1]
                a = split.split(":")
                b = splitone.split(":")
                one =  int(a[0])
                two = int(a[1])
                three = int(b[0])
                four = int(b[1])
                pixel_copy2[one:two, three:four] = fillmatrix
        
        endTime = datetime.datetime.now().replace(microsecond=0)
        durationTime = endTime - startTime        
        print("md.hotspot_complete - Image " + str(indexor+1) + " Hotspot Isolating:" + str(durationTime))
        
        
        startTime = datetime.datetime.now().replace(microsecond=0)      
        result = pixel_copy2.reshape([1, width*height])
        reult = result.tolist()
        endTime = datetime.datetime.now().replace(microsecond=0)
        durationTime = endTime - startTime        
        print("md.hotspot_complete - Image " + str(indexor+1) + " Array Priming:" + str(durationTime))
        
        
        startTime = datetime.datetime.now().replace(microsecond=0)      
        pixel_values1 = list(rgb1.getdata())
        for i in range(0,width*height):
            if reult[0][i] == 1:
                pixel_values1[i] = find
        durationTime = endTime - startTime        
        print("md.hotspot_complete - Image " + str(indexor+1) + " Translating:" + str(durationTime))
        
        
        startTime = datetime.datetime.now().replace(microsecond=0)      
        image_out = Image.new("RGB",(width,height))
        image_out.putdata(pixel_values1)
        image_out.save(mod_string + "_isolated" + ".PNG")
        endTime = datetime.datetime.now().replace(microsecond=0)
        durationTime = endTime - startTime        
        print("md.hotspot_complete - Image " + str(indexor+1) + " Saving:" + str(durationTime))

        
def hotspot_calculator(filepath, x, y, find):
    files = glob.glob(filepath)
    for indexor, item in enumerate(files):
        name = ntpath.basename(files[indexor])
        size = len(name)
        mod_string = name[:size - 4]
        
        
        startTime = datetime.datetime.now().replace(microsecond=0)
        image = Image.open(files[indexor])
        rgb1 = image.convert('RGB')
        width, height = image.size
        pixel_values1 = list(rgb1.getdata())
        pixel_copy = pixel_values1
        endTime = datetime.datetime.now().replace(microsecond=0)
        durationTime = endTime - startTime        
        print ("md.hotspot_calculator - Image " + str(indexor+1) + " Importing:" + str(durationTime))
        
        
        startTime = datetime.datetime.now().replace(microsecond=0)
        for index, item in enumerate(pixel_values1):
            if item != find:
                pixel_values1[index] = 2
            if item == find:
                pixel_values1[index] = 1
        endTime = datetime.datetime.now().replace(microsecond=0)
        durationTime = endTime - startTime        
        print("md.hotspot_calculator - Image " + str(indexor+1) + " Converting:" + str(durationTime))
        
        
        startTime = datetime.datetime.now().replace(microsecond=0)
        pixel_values1 = np.array(pixel_values1)
        shape = (height, width)
        pixel_values2 = np.reshape(pixel_values1, shape)
        pixel_copy2 = np.reshape(pixel_copy, shape)
        const = (width*height)/100
        global storeddictionary
        storeddictionary = {}
        for w in range (x,width+1):
            for h in range (y,height+1):
                storeddictionary[str(h-y)+":"+str(h)+", "+str(w-x)+":" + str(w)] = pixel_values2[h-y:h, w-x:w]
                a=(w-1)*height+h
                print(str(round((a)/(const),1)) + "%" , end = "\r")  
        endTime = datetime.datetime.now().replace(microsecond=0)
        durationTime = endTime - startTime        
        print("md.hotspot_calculator - Image " + str(indexor+1) + " Hotspot Calculating:" + str(durationTime))
     
    
def hotspot_analyzer(d=None, filepath = None, x = None, y = None, find = None):
    files = glob.glob(filepath)
    for indexor, item in enumerate(files):
        name = ntpath.basename(files[indexor])
        size = len(name)
        mod_string = name[:size - 4]


        startTime = datetime.datetime.now().replace(microsecond=0)
        image = Image.open(files[indexor])
        rgb1 = image.convert('RGB')
        width, height = image.size
        pixel_values1 = list(rgb1.getdata())
        pixel_copy = pixel_values1
        endTime = datetime.datetime.now().replace(microsecond=0)
        durationTime = endTime - startTime        
        print ("md.hotspot_analyzer - Image " + str(indexor+1) + " Importing:" + str(durationTime))


        startTime = datetime.datetime.now().replace(microsecond=0)
        global analyzedval
        analyzedval = {}
        for w in range (x,width):
            for h in range (y,height):
                keytocheck = d.get(str(h-y)+":"+str(h)+", "+str(w-x)+":" + str(w))
                stringforkey = str(h-y)+":"+str(h)+", "+str(w-x)+":" + str(w)

                if np.sum(keytocheck[0,:]) == x and np.sum(keytocheck[y-1,:]) == x and np.sum(keytocheck[:,0]) == y and np.sum(keytocheck[:,x-1]) == y:
                    valueforkey = True
                else:
                    valueforkey = False
                    a=(w-1)*height+h
                    const = (width*height)/100
                    print(str(round((a)/(const),1)) + "%" , end = "\r")
                analyzedval[stringforkey] = valueforkey
        endTime = datetime.datetime.now().replace(microsecond=0)
        durationTime = endTime - startTime        
        print("md.hotspot_analyzer - Image " + str(indexor+1) + " Hotspot Analyzing:" + str(durationTime))

        
def hotspot_isolator(a=None, filepath = None, x = None, y = None, find = None):
    files = glob.glob(filepath)
    for indexor, item in enumerate(files):
        name = ntpath.basename(files[indexor])
        size = len(name)
        mod_string = name[:size - 4]


        startTime = datetime.datetime.now().replace(microsecond=0)
        image = Image.open(files[indexor])
        rgb1 = image.convert('RGB')
        width, height = image.size
        pixel_values1 = list(rgb1.getdata())
        
        
        
        starttTime = datetime.datetime.now().replace(microsecond=0)
        for index, item in enumerate(pixel_values1):
            if item != find:
                pixel_values1[index] = 2
            if item == find:
                pixel_values1[index] = 1
        endTime = datetime.datetime.now().replace(microsecond=0)
        durationTime = endTime - starttTime        
        print("md.hotspot_isolator - Image " + str(indexor+1) + " Converting:" + str(durationTime))
        
        pixel_copy = pixel_values1
        pixel_values1 = np.array(pixel_values1)
        shape = (height, width)
        pixel_values2 = np.reshape(pixel_values1, shape)
        pixel_copy2 = np.reshape(pixel_copy, shape)
        endTime = datetime.datetime.now().replace(microsecond=0)
        durationTime = endTime - startTime        
        print ("md.hotspot_isolator - Image " + str(indexor+1) + " Importing:" + str(durationTime))
            
            
        startTime = datetime.datetime.now().replace(microsecond=0) 
        fillmatrix = np.full((y, x), 1)
        for key, value in a.items():
            if value == True:
                txt = key
                splitter = txt.split(", ")
                split, splitone = splitter[0], splitter[1]
                a = split.split(":")
                b = splitone.split(":")
                one =  int(a[0])
                two = int(a[1])
                three = int(b[0])
                four = int(b[1])
                pixel_copy2[one:two, three:four] = fillmatrix
        
        endTime = datetime.datetime.now().replace(microsecond=0)
        durationTime = endTime - startTime        
        print("md.hotspot_isolator - Image " + str(indexor+1) + " Hotspot Isolating:" + str(durationTime))
        
        
        startTime = datetime.datetime.now().replace(microsecond=0)      
        result = pixel_copy2.reshape([1, width*height])
        reult = result.tolist()
        endTime = datetime.datetime.now().replace(microsecond=0)
        durationTime = endTime - startTime        
        print("md.hotspot_isolator - Image " + str(indexor+1) + " Array Priming:" + str(durationTime))
        
        
        startTime = datetime.datetime.now().replace(microsecond=0)      
        pixel_values1 = list(rgb1.getdata())
        for i in range(0,width*height):
            if reult[0][i] == 1:
                pixel_values1[i] = find
        durationTime = endTime - startTime        
        print("md.hotspot_isolator - Image " + str(indexor+1) + " Translating:" + str(durationTime))
        
        
        startTime = datetime.datetime.now().replace(microsecond=0)      
        image_out = Image.new("RGB",(width,height))
        image_out.putdata(pixel_values1)
        image_out.save(mod_string + "_isolated" + ".PNG")
        endTime = datetime.datetime.now().replace(microsecond=0)
        durationTime = endTime - startTime        
        print("md.hotspot_isolator - Image " + str(indexor+1) + " Saving:" + str(durationTime))


