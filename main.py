import tkinter
from tkinter import *;
import random
import math

#this function is used to clear the text area
def clearToTextInput():
   T.delete("1.0","end")

#this function is used to generate hashtags for a reel
def reel():
    T.delete("1.0","end")#clear the text area first
    
    tags_list = []
    size_list = [13,15,18,21]
    random.shuffle(size_list)
    no_of_tags = size_list[0]#this wil be the total no. of hashtags generated

    T.insert(tkinter.END, "Here are the hashtags for a reel : \n")
    high = math.ceil(0.60*no_of_tags)#60% of hashtags will be of highly popular
    med =  math.ceil(0.20*no_of_tags)#20% of hashtags will be of medium popular
    low =  math.ceil(0.10*no_of_tags)#10% of hashtags will be of low popular

    T.insert(tkinter.END, "\n")
    
    #open text file with high number of posts
    file = open("high.txt",'r')
    lines = file.read().split("\n")
    random.shuffle(lines)
    count = 0
    for w in lines:
        tags_list.append(w)
        count = count + 1
        if(count==high):
            break
    T.insert(tkinter.END, "got "+str(count)+" tags from high\n")
    file.close()
    
    #open text file with medium number of posts
    file = open("med.txt",'r')
    lines = file.read().split("\n")
    random.shuffle(lines)

    count = 0
    for w in lines:
        tags_list.append(w)
        count = count + 1
        if(count==med):
            break
    T.insert(tkinter.END,"got "+str(count)+" tags from med\n")  
    file.close()
    
    #open text file with low number of posts
    file = open("low.txt",'r')
    lines = file.read().split("\n")
    random.shuffle(lines)

    count = 0
    for w in lines:
        tags_list.append(w)
        count = count + 1
        if(count==low):
            break
    T.insert(tkinter.END,"got "+str(count)+" tags from low\n") 
    file.close()
    
    T.insert(tkinter.END, "\n")
    
    #print the tags and total tags in text area
    c = 0
    random.shuffle(tags_list)
    for i in tags_list[:size_list[0]]:
        T.insert(tkinter.END, i+"\n")
        c+=1
    T.insert(tkinter.END,"Total number of hashtags : "+str(c))
     
#this function is used to generate hashtags for a picture     
def picture():
    T.delete("1.0","end")#clear the text area first
    tags_list = []
    size_list = [13,15,18,21]
    random.shuffle(size_list)
    no_of_tags = size_list[0]#this wil be the total no. of hashtags generated

    T.insert(tkinter.END, "Here are the hashtags for a pic : \n")

    T.insert(tkinter.END, "\n")
    
    high = math.ceil(0.20*no_of_tags)#20% of hashtags will be of highly popular
    med =  math.ceil(0.20*no_of_tags)#20% of hashtags will be of medium popular
    low =  math.ceil(0.60*no_of_tags)#60% of hashtags will be of low popular

   
    #open text file with high number of posts
    file = open("high.txt",'r')
    lines = file.read().split("\n")
    count = 0
    for w in lines:
        tags_list.append(w)
        count = count + 1
        if(count==high):
            break
    T.insert(tkinter.END, "got "+str(count)+" tags from high\n")
    file.close()
    
    #open text file with medium number of posts
    file = open("med.txt",'r')
    lines = file.read().split("\n")
    count = 0
    for w in lines:
        tags_list.append(w)
        count = count + 1
        if(count==med):
            break
    T.insert(tkinter.END,"got "+str(count)+" tags from med\n")  
    file.close()
    
    #open text file with low number of posts
    file = open("low.txt",'r')
    lines = file.read().split("\n")
    count = 0
    for w in lines:
        tags_list.append(w)
        count = count + 1
        if(count==low):
            break
    T.insert(tkinter.END,"got "+str(count)+" tags from low\n") 
    file.close()
    
    T.insert(tkinter.END, "\n")
    
    #print the tags and total no. of tags
    c = 0
    random.shuffle(tags_list)
    for i in tags_list[:size_list[0]]:
        T.insert(tkinter.END, i+"\n")
        c+=1
    T.insert(tkinter.END,"Total number of hashtags : "+str(c))
    
                
m = tkinter.Tk()#the window
m.geometry("1920x1080")#window default size 
m.title('Instagram tags')#window title

# Label for text area
l = Label(m, text = "Here your tags will be generated after you click on a button : ")
l.config(font =("Courier", 14))
l.pack()

# Create text widget and specify size.
T = Text(m, height = 35, width = 35)
T.pack()

# reel button
reelBtn  = tkinter.Button(m, text='Posting a reel', width=30, height=2,   command=reel)
reelBtn.pack()

# picture button
picBtn  = tkinter.Button(m, text='Posting a pic', width=30, height=2,   command=picture)
picBtn.pack()

# clear button
clearBtn  = tkinter.Button(m, text='Clear', width=30, height=2,   command=clearToTextInput)
clearBtn.pack()

#exit
exitBtn  = tkinter.Button(m, text='Exit', width=30, height=2,   command=m.destroy)
exitBtn.pack()

m.mainloop()