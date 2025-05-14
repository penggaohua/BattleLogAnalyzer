#coding=utf-8
import tkinter as tk
from tkinter import *
from tkinter import ttk,scrolledtext


class  LogAnalyerTK:


    def __init__(self,path):
        self.path = path
        self.root = tk.Tk()
        self.root.title("日志分析器3.0")
        self.root.geometry("1400x800+10+10")
        self.is_select = True
    def set_frame(self):
        return Frame(self.root)


    def set_button(self,frame,btn_name,btn_command,bg="white"):
        return Button(frame,text=btn_name,bg=bg,command=btn_command)

    def set_Entry(self,frame,width,input_str=""):
        str_var = StringVar()
        str_var.set(input_str)
        return Entry(frame, width=width, textvariable=str_var)

    def get_Entry(self,entry):
        return entry.get()




    def set_lable(self,frame,label_name):
         return  Label(frame, text=label_name)

    def set_check_button(self,frame,button_text,value):
        return Checkbutton (frame,text=button_text,onvalue=True,offvalue=False,variable=value)


    def set_scroll_text(self,frame,width,height):
         return scrolledtext.ScrolledText(frame, width=width, height=height, font=("宋体", 10))



    def test(self,text_output):
        res = "test \n"
        print("this is a method for test ")
        text_output.insert(END, res)
        text_output.see(END)

    def show_in_text(self,res,text_output):
        text_output.insert(END, res)
        text_output.see(END)

    def clean_text(self,text_output):
        text_output.delete('1.0', 'end')


    def get_entry_content(self,entry):
        return entry.get()

    def main(self):
        self.root.mainloop()

    def select_all(self,atr_dic):
        self.is_select = True ^ self.is_select
        for value in atr_dic.values():
            value.set(self.is_select )




