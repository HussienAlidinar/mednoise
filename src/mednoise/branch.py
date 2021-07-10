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


def branch_complete(filepath, find,x,y, iterations):
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
        print ("md.branch_complete - Image " + str(indexor+1) + " Importing:" + str(durationTime))
        
        
        startTime = datetime.datetime.now().replace(microsecond=0)
        for index, item in enumerate(pixel_values1):
            if item != find:
                pixel_values1[index] = 2
            if item == find:
                pixel_values1[index] = 1
        endTime = datetime.datetime.now().replace(microsecond=0)
        durationTime = endTime - startTime        
        print("md.branch_complete - Image " + str(indexor+1) + " Converting:" + str(durationTime))
        
        
        startTime = datetime.datetime.now().replace(microsecond=0)
        pixel_values1 = np.array(pixel_values1)
        shape = (height, width)
        global pixel_values2
        pixel_values2 = np.reshape(pixel_values1, shape)
        pixel_copy2 = np.reshape(pixel_copy, shape)
        global coords
        coords = []
        const = (width*height)/100
        endTime = datetime.datetime.now().replace(microsecond=0)
        durationTime = endTime - startTime        
        print("md.branch_complete - Image " + str(indexor+1) + " Translating:" + str(durationTime))
        
        
        startTime = datetime.datetime.now().replace(microsecond=0)
        proximal_brancher(coords, y,x)
        global coordsfinal
        coordsfinal = []
        i = 0
        global diflist
        diflist = coords
        while i != iterations:
            coordsfinalinit = []
            filteredcoords = []
            print(str(round((i*100)/(iterations),1)) + "%", end = "\r")
            for index, item in enumerate(diflist):
                txt = str(diflist[index])
                newstr = txt.replace("[", "")
                finalstr = newstr.replace("]", "")
                splitter = finalstr.split(", ")
                newy, newx = splitter[0], splitter[1]
                newx = int(newx)
                newy = int(newy) 
                if manual_checker(newy, newx) == 2:
                    proximal_brancher(coordsfinal, newy, newx)
            for index, item in enumerate(coordsfinal):
                coordsfinal[index] = str(coordsfinal[index])
            for index, item in enumerate(coords):
                coords[index] = str(coords[index])   
            list(set(coordsfinal))
            list(set(coords))
            diflist = list(set(coordsfinal) - set(coords))
            coords = []
            for index, item in enumerate(coordsfinal):
                coords.append(coordsfinal[index])     
            i += 1
        endTime = datetime.datetime.now().replace(microsecond=0)
        durationTime = endTime - startTime        
        print("md.branch_complete - Image " + str(indexor+1) + " Branching:" + str(durationTime))  
            

        startTime = datetime.datetime.now().replace(microsecond=0)
        a = []
        g = []
        list(set(coords))
        a = coords
        for index, item in enumerate(a):  
            print(str(round((index*100)/(len(coords)),1)) + "%", end = "\r")
            txt = str(a[index])
            newstr = txt.replace("[", "")
            finalstr = newstr.replace("]", "")
            splitter = finalstr.split(", ")
            newy, newx = splitter[0], splitter[1]
            newx = int(newx)
            newy = int(newy)
            if manual_checker(newy, newx) == 2:
                g.append([newy, newx])
        endTime = datetime.datetime.now().replace(microsecond=0)
        durationTime = endTime - startTime        
        print("md.branch_complete - Image " + str(indexor+1) + " Branch Analyzing:" + str(durationTime)) 
        
                                                  
        startTime = datetime.datetime.now().replace(microsecond=0)
        complement = []
        for w in range(width):
            for h in range(height):
                complement.append([h,w])
        setc = {tuple(item) for item in g}
        finalset = [item for item in complement if tuple(item) not in setc]
        for index, item in enumerate(finalset):      
            txt = str(finalset[index])
            newstr = txt.replace("[", "")
            finalstr = newstr.replace("]", "")
            splitter = finalstr.split(", ")
            newy, newx = splitter[0], splitter[1]
            newx = int(newx)
            newy = int(newy) 
            pixel_copy2[newy,newx] = 1
        endTime = datetime.datetime.now().replace(microsecond=0)
        durationTime = endTime - startTime        
        print("md.branch_complete - Image " + str(indexor+1) + " Branch Isolating:" + str(durationTime))
        
                                                  
        startTime = datetime.datetime.now().replace(microsecond=0)      
        result = pixel_copy2.reshape([1, width*height])
        reult = result.tolist()
        endTime = datetime.datetime.now().replace(microsecond=0)
        durationTime = endTime - startTime        
        print("md.branch_complete - Image " + str(indexor+1) + " Array Priming:" + str(durationTime))
        
        
        startTime = datetime.datetime.now().replace(microsecond=0)      
        pixel_values1 = list(rgb1.getdata())
        for i in range(0,width*height):
            if reult[0][i] == 1:
                pixel_values1[i] = find
            if reult[0][i] == 3:
                pixel_values1[i] = (255,0,255)
        durationTime = endTime - startTime        
        print("md.branch_complete - Image " + str(indexor+1) + " Translating:" + str(durationTime))
        
        
        startTime = datetime.datetime.now().replace(microsecond=0)      
        image_out = Image.new("RGB",(width,height))
        image_out.putdata(pixel_values1)
        image_out.save(mod_string + "_isolated" + ".PNG")
        endTime = datetime.datetime.now().replace(microsecond=0)
        durationTime = endTime - startTime        
        print("md.branch_complete - Image " + str(indexor+1) + " Saving:" + str(durationTime))
                                                  
 
def branch_calculator(filepath, find,x,y, iterations):
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
        print ("md.branch_calculator - Image " + str(indexor+1) + " Importing:" + str(durationTime))
        
        
        startTime = datetime.datetime.now().replace(microsecond=0)
        for index, item in enumerate(pixel_values1):
            if item != find:
                pixel_values1[index] = 2
            if item == find:
                pixel_values1[index] = 1
        endTime = datetime.datetime.now().replace(microsecond=0)
        durationTime = endTime - startTime        
        print("md.branch_calculator - Image " + str(indexor+1) + " Converting:" + str(durationTime))
        
        
        startTime = datetime.datetime.now().replace(microsecond=0)
        pixel_values1 = np.array(pixel_values1)
        shape = (height, width)
        global pixel_values2
        pixel_values2 = np.reshape(pixel_values1, shape)
        global pixel_copy2
        pixel_copy2 = np.reshape(pixel_copy, shape)
        global coords
        coords = []
        const = (width*height)/100
        endTime = datetime.datetime.now().replace(microsecond=0)
        durationTime = endTime - startTime        
        print("md.branch_calculator - Image " + str(indexor+1) + " Translating:" + str(durationTime))
        
        
        startTime = datetime.datetime.now().replace(microsecond=0)
        proximal_brancher(coords, y,x)
        global coordsfinal
        coordsfinal = []
        i = 0
        global diflist
        diflist = coords
        while i != iterations:
            coordsfinalinit = []
            filteredcoords = []
            print(str(round((i*100)/(iterations),1)) + "%", end = "\r")
            for index, item in enumerate(diflist):
                txt = str(diflist[index])
                newstr = txt.replace("[", "")
                finalstr = newstr.replace("]", "")
                splitter = finalstr.split(", ")
                newy, newx = splitter[0], splitter[1]
                newx = int(newx)
                newy = int(newy) 
                if manual_checker(newy, newx) == 2:
                    proximal_brancher(coordsfinal, newy, newx)
            for index, item in enumerate(coordsfinal):
                coordsfinal[index] = str(coordsfinal[index])
            for index, item in enumerate(coords):
                coords[index] = str(coords[index])   
            list(set(coordsfinal))
            list(set(coords))
            diflist = list(set(coordsfinal) - set(coords))
            coords = []
            for index, item in enumerate(coordsfinal):
                coords.append(coordsfinal[index])     
            i += 1
        endTime = datetime.datetime.now().replace(microsecond=0)
        durationTime = endTime - startTime        
        print("md.branch_calculator - Image " + str(indexor+1) + " Branching:" + str(durationTime))  

        
def branch_analyzer(c = None):
    startTime = datetime.datetime.now().replace(microsecond=0)
    a = []
    global g
    g = []
    list(set(c))
    a = c
    for index, item in enumerate(a):  
        print(str(round((index*100)/(len(coords)),1)) + "%", end = "\r")
        txt = str(a[index])
        newstr = txt.replace("[", "")
        finalstr = newstr.replace("]", "")
        splitter = finalstr.split(", ")
        newy, newx = splitter[0], splitter[1]
        newx = int(newx)
        newy = int(newy)
        if manual_checker(newy, newx) == 2:
            g.append([newy, newx])
    endTime = datetime.datetime.now().replace(microsecond=0)
    durationTime = endTime - startTime        
    print("md.branch_analyzer - Branch Analyzing:" + str(durationTime)) 

    
def branch_isolator(filepath=None, a=None, find = None):
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
            print ("md.branch_isolator - Image " + str(indexor+1) + " Importing:" + str(durationTime))
            startTime = datetime.datetime.now().replace(microsecond=0)
            complement = []
            for w in range(width):
                for h in range(height):
                    complement.append([h,w])
            setc = {tuple(item) for item in a}
            finalset = [item for item in complement if tuple(item) not in setc]
            for index, item in enumerate(finalset):      
                txt = str(finalset[index])
                newstr = txt.replace("[", "")
                finalstr = newstr.replace("]", "")
                splitter = finalstr.split(", ")
                newy, newx = splitter[0], splitter[1]
                newx = int(newx)
                newy = int(newy) 
                pixel_copy2[newy,newx] = 1
            endTime = datetime.datetime.now().replace(microsecond=0)
            durationTime = endTime - startTime        
            print("md.branch_isolator - Image " + str(indexor+1) + " Branch Isolating:" + str(durationTime))


            startTime = datetime.datetime.now().replace(microsecond=0)      
            result = pixel_copy2.reshape([1, width*height])
            reult = result.tolist()
            endTime = datetime.datetime.now().replace(microsecond=0)
            durationTime = endTime - startTime        
            print("md.branch_isolator - Image " + str(indexor+1) + " Array Priming:" + str(durationTime))


            startTime = datetime.datetime.now().replace(microsecond=0)      
            pixel_values1 = list(rgb1.getdata())
            for i in range(0,width*height):
                if reult[0][i] == 1:
                    pixel_values1[i] = find
                if reult[0][i] == 3:
                    pixel_values1[i] = (255,0,255)
            durationTime = endTime - startTime        
            print("md.branch_isolator - Image " + str(indexor+1) + " Translating:" + str(durationTime))


            startTime = datetime.datetime.now().replace(microsecond=0)      
            image_out = Image.new("RGB",(width,height))
            image_out.putdata(pixel_values1)
            image_out.save(mod_string + "_isolated" + ".PNG")
            endTime = datetime.datetime.now().replace(microsecond=0)
            durationTime = endTime - startTime        
            print("md.branch_isolator - Image " + str(indexor+1) + " Saving:" + str(durationTime))    


def proximal_brancher(matrix, ycord,xcord):
            x = matrix
            pixel_values2
            r = ycord
            c = xcord
            m, n = pixel_values2.shape
            
            for i in [-1, 0, 1]: 
                for j in [-1, 0, 1]: 
                    if 0 <= r + i < m and 0 <= c + j < n:
                        x.append([r + i, c + j])
                            
def manual_checker(coordy, coordx):
    if pixel_values2[coordy,coordx] == 2:
        return 2
    else:
        return 1
