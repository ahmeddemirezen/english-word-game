#Ahmed Demirezen 08/17/2019 16/00

import os
import codecs
import tkinter as tk
import numpy as np
import random as rn


#we imported the txt file.
class read_class:
    def __init__(self):

        self.word_list=codecs.open("wordList.txt","r",encoding="utf-8")

        self.word_list_read=self.word_list.read()

        #print(self.word_list_read)

        self.word_list_splitted=self.word_list_read.split("\r")

        #print(type(self.word_list_splitted[0].split()[0]))

        self.word_list_all_splitted=[]

        for i in range(len(self.word_list_splitted)):
            for k in range(2):
                self.word_list_all_splitted.append(self.word_list_splitted[i].split()[k])

        #print(self.word_list_all_splitted)

        self.uzunluk=len(self.word_list_all_splitted)

        self.word_list_numpy=np.array(self.word_list_all_splitted).reshape(int(self.uzunluk/2),2)

        #print(self.word_list_numpy)

#this is our graphical interface        
class gui:
    def __init__(self,window):

        self.last10_c=[]#control variable to avoid using the same word.
        self.q_list=[0,1,2,3]#unchanged answer button list
        self.q_rand_c=[]#for random answer placement
        self.q_n_list=[4,4,4,4]#firstly working needed for first point get
        self.rn_integer=0#this variable is needed for first true meaning get
        
        
        self.point=1#we are created global score variable
            
        self.frame=tk.Frame(window)
        self.frame.pack(side="top")

        self.l1=tk.Label(self.frame,text="Welcome words game",bg="white")
        self.l1.config(font=("Courier","50"))
        self.l1.grid(row=0,column=2)

        self.b0=tk.Button(self.frame,text="b1",font=("Courier","10"),command=self.answer_b0)
        self.b0.grid(row=2,column=1)

        self.b1=tk.Button(self.frame,text="b2",font=("Courier","10"),command=self.answer_b1)
        self.b1.grid(row=1,column=1)

        self.b2=tk.Button(self.frame,text="b3",font=("Courier","10"),command=self.answer_b2)
        self.b2.grid(row=1,column=3)

        self.b3=tk.Button(self.frame,text="b4",font=("Courier","10"),command=self.answer_b3)
        self.b3.grid(row=2,column=3)

        self.point_l=tk.Label(self.frame,text="0")
        self.point_l.grid(row=3,column=2)

        self.true_l=tk.Label(self.frame,text="true meaning")
        self.true_l.grid(row=4,column=2)
        
    def answer_b0(self):

        self.true_l["text"]=str(read_c.word_list_numpy[self.rn_integer,0]) +" ==> "+ str(read_c.word_list_numpy[self.rn_integer,1])#write true meaning on gui
        
        ##point winnig or losing
        if self.q_n_list[0]==0:
            self.point=self.point + 1
        else:
            self.point=self.point - 1
        ##    
        self.point_l["text"]=str(self.point)#write score on gui    

        ###This codes are setting random english word 
        self.rn_integer=rn.randint(0,int(read_c.uzunluk / 2) - 1)
        
        while self.rn_integer in self.last10_c:
            self.rn_integer=rn.randint(0,int(read_c.uzunluk / 2)- 1)
        
            
        self.last10_c.append(self.rn_integer)
        if len(self.last10_c)==21:
            self.last10_c.pop(0)
        else:
            pass
        #print(self.last10_c)
        #print(self.rn_integer)
        self.l1["text"]=read_c.word_list_numpy[self.rn_integer,0]
        ###
        
        c_v=0#this variable needed for  write true answer on true button.

        self.q_n_list=rn.sample(self.q_list,4)
        
        for i in range(4):
            if c_v==0:
                
                if self.q_n_list[i]==0:
                    self.b0["text"]=read_c.word_list_numpy[self.rn_integer,1]
                    
                elif self.q_n_list[i]==1:
                    self.b1["text"]=read_c.word_list_numpy[self.rn_integer,1]
                    
                elif self.q_n_list[i]==2:
                    self.b2["text"]=read_c.word_list_numpy[self.rn_integer,1]
                    
                elif self.q_n_list[i]==3:
                    self.b3["text"]=read_c.word_list_numpy[self.rn_integer,1]
                    
                c_v=1

            
            
            else:
                self.q_rand_v=rn.randint(0,int(read_c.uzunluk / 2) - 1)
                self.q_rand_c.append(self.q_rand_v)

                if len(self.q_rand_c)==21:
                    self.q_rand_c.pop(0)
                else:
                    pass
                
                while self.q_rand_v in self.q_rand_c:
                    self.q_rand_v=rn.randint(0,int(read_c.uzunluk / 2) - 1)
                    
                if self.q_n_list[i]==0:
                    self.b0["text"]=read_c.word_list_numpy[self.q_rand_v,1]
                    
                elif self.q_n_list[i]==1:
                    self.b1["text"]=read_c.word_list_numpy[self.q_rand_v,1]
                    
                elif self.q_n_list[i]==2:
                    self.b2["text"]=read_c.word_list_numpy[self.q_rand_v,1]
                    
                elif self.q_n_list[i]==3:
                    self.b3["text"]=read_c.word_list_numpy[self.q_rand_v,1]
                    
    def answer_b1(self):

        self.true_l["text"]=str(read_c.word_list_numpy[self.rn_integer,0]) +" ==> "+ str(read_c.word_list_numpy[self.rn_integer,1])
        
        if self.q_n_list[0]==1:
            self.point=self.point + 1
        else:
            self.point=self.point - 1
            
        self.point_l["text"]=str(self.point)    
        
        self.rn_integer=rn.randint(0,int(read_c.uzunluk / 2) - 1)
        
        while self.rn_integer in self.last10_c:
            self.rn_integer=rn.randint(0,int(read_c.uzunluk / 2)- 1)
        
            
        self.last10_c.append(self.rn_integer)
        if len(self.last10_c)==21:
            self.last10_c.pop(0)
        else:
            pass
        #print(self.last10_c)
        #print(self.rn_integer)
        self.l1["text"]=read_c.word_list_numpy[self.rn_integer,0]

        
        c_v=0

        self.q_n_list=rn.sample(self.q_list,4)
        
        for i in range(4):
            if c_v==0:
                
                if self.q_n_list[i]==0:
                    self.b0["text"]=read_c.word_list_numpy[self.rn_integer,1]
                    
                elif self.q_n_list[i]==1:
                    self.b1["text"]=read_c.word_list_numpy[self.rn_integer,1]
                    
                elif self.q_n_list[i]==2:
                    self.b2["text"]=read_c.word_list_numpy[self.rn_integer,1]
                    
                elif self.q_n_list[i]==3:
                    self.b3["text"]=read_c.word_list_numpy[self.rn_integer,1]
                    
                c_v=1

            
            
            else:
                self.q_rand_v=rn.randint(0,int(read_c.uzunluk / 2) - 1)
                self.q_rand_c.append(self.q_rand_v)

                if len(self.q_rand_c)==21:
                    self.q_rand_c.pop(0)
                else:
                    pass
                
                while self.q_rand_v in self.q_rand_c:
                    self.q_rand_v=rn.randint(0,int(read_c.uzunluk / 2) - 1)
                    
                if self.q_n_list[i]==0:
                    self.b0["text"]=read_c.word_list_numpy[self.q_rand_v,1]
                    
                elif self.q_n_list[i]==1:
                    self.b1["text"]=read_c.word_list_numpy[self.q_rand_v,1]
                    
                elif self.q_n_list[i]==2:
                    self.b2["text"]=read_c.word_list_numpy[self.q_rand_v,1]
                    
                elif self.q_n_list[i]==3:
                    self.b3["text"]=read_c.word_list_numpy[self.q_rand_v,1]
                    
    def answer_b2(self):

        self.true_l["text"]=str(read_c.word_list_numpy[self.rn_integer,0]) +" ==> "+ str(read_c.word_list_numpy[self.rn_integer,1])
        
        if self.q_n_list[0]==2:
            self.point=self.point + 1
        else:
            self.point=self.point - 1

        self.point_l["text"]=str(self.point)
        
        self.rn_integer=rn.randint(0,int(read_c.uzunluk / 2) - 1)
        
        while self.rn_integer in self.last10_c:
            self.rn_integer=rn.randint(0,int(read_c.uzunluk / 2)- 1)
        
            
        self.last10_c.append(self.rn_integer)
        if len(self.last10_c)==21:
            self.last10_c.pop(0)
        else:
            pass
        #print(self.last10_c)
        #print(self.rn_integer)
        self.l1["text"]=read_c.word_list_numpy[self.rn_integer,0]

        
        c_v=0

        self.q_n_list=rn.sample(self.q_list,4)
        
        for i in range(4):
            if c_v==0:
                
                if self.q_n_list[i]==0:
                    self.b0["text"]=read_c.word_list_numpy[self.rn_integer,1]
                    
                elif self.q_n_list[i]==1:
                    self.b1["text"]=read_c.word_list_numpy[self.rn_integer,1]
                    
                elif self.q_n_list[i]==2:
                    self.b2["text"]=read_c.word_list_numpy[self.rn_integer,1]
                    
                elif self.q_n_list[i]==3:
                    self.b3["text"]=read_c.word_list_numpy[self.rn_integer,1]
                    
                c_v=1

            
            
            else:
                self.q_rand_v=rn.randint(0,int(read_c.uzunluk / 2) - 1)
                self.q_rand_c.append(self.q_rand_v)

                if len(self.q_rand_c)==21:
                    self.q_rand_c.pop(0)
                else:
                    pass
                
                while self.q_rand_v in self.q_rand_c:
                    self.q_rand_v=rn.randint(0,int(read_c.uzunluk / 2) - 1)
                    
                if self.q_n_list[i]==0:
                    self.b0["text"]=read_c.word_list_numpy[self.q_rand_v,1]
                    
                elif self.q_n_list[i]==1:
                    self.b1["text"]=read_c.word_list_numpy[self.q_rand_v,1]
                    
                elif self.q_n_list[i]==2:
                    self.b2["text"]=read_c.word_list_numpy[self.q_rand_v,1]
                    
                elif self.q_n_list[i]==3:
                    self.b3["text"]=read_c.word_list_numpy[self.q_rand_v,1]
                    
    def answer_b3(self):

        self.true_l["text"]=str(read_c.word_list_numpy[self.rn_integer,0]) +" ==> "+ str(read_c.word_list_numpy[self.rn_integer,1])
        
        if self.q_n_list[0]==3:
            self.point=self.point + 1
        else:
            self.point=self.point - 1

        self.point_l["text"]=str(self.point)
        
        self.rn_integer=rn.randint(0,int(read_c.uzunluk / 2) - 1)
        
        while self.rn_integer in self.last10_c:
            self.rn_integer=rn.randint(0,int(read_c.uzunluk / 2)- 1)
        
            
        self.last10_c.append(self.rn_integer)
        if len(self.last10_c)==21:
            self.last10_c.pop(0)
        else:
            pass
        #print(self.last10_c)
        #print(self.rn_integer)
        self.l1["text"]=read_c.word_list_numpy[self.rn_integer,0]

        
        c_v=0

        self.q_n_list=rn.sample(self.q_list,4)
        
        for i in range(4):
            if c_v==0:
                
                if self.q_n_list[i]==0:
                    self.b0["text"]=read_c.word_list_numpy[self.rn_integer,1]
                    
                elif self.q_n_list[i]==1:
                    self.b1["text"]=read_c.word_list_numpy[self.rn_integer,1]
                    
                elif self.q_n_list[i]==2:
                    self.b2["text"]=read_c.word_list_numpy[self.rn_integer,1]
                    
                elif self.q_n_list[i]==3:
                    self.b3["text"]=read_c.word_list_numpy[self.rn_integer,1]
                    
                c_v=1

            
            
            else:
                self.q_rand_v=rn.randint(0,int(read_c.uzunluk / 2) - 1)
                self.q_rand_c.append(self.q_rand_v)

                if len(self.q_rand_c)==21:
                    self.q_rand_c.pop(0)
                else:
                    pass
                
                while self.q_rand_v in self.q_rand_c:
                    self.q_rand_v=rn.randint(0,int(read_c.uzunluk / 2) - 1)
                    
                if self.q_n_list[i]==0:
                    self.b0["text"]=read_c.word_list_numpy[self.q_rand_v,1]
                    
                elif self.q_n_list[i]==1:
                    self.b1["text"]=read_c.word_list_numpy[self.q_rand_v,1]
                    
                elif self.q_n_list[i]==2:
                    self.b2["text"]=read_c.word_list_numpy[self.q_rand_v,1]
                    
                elif self.q_n_list[i]==3:
                    self.b3["text"]=read_c.word_list_numpy[self.q_rand_v,1]
#window                    
window_g=tk.Tk()
window_g.title("English Word Game")
window_g.geometry("1024x200")
window_include=gui(window_g)
read_c=read_class()
window_g.mainloop()
