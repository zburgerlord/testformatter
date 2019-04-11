#!/usr/bin/python3
import re
from tkinter import *
from tkinter.filedialog import askopenfilename

 

class MyFrame(Frame):
    def __init__(self):
        Frame.__init__(self)
        self.master.title("Test Formatter")
        self.master.rowconfigure(5, weight=1)
        self.master.columnconfigure(5, weight=1)
        self.grid(sticky=W+E+N+S)
        
               
        self.button = Button(self, text="Remove Answers", command=self.remove_answer, width=20, height=3)
        self.button.grid(row=1, column=0)
        
        self.button = Button(self, text="Append Answers", command=self.answer_maker, width=20, height=3)
        self.button.grid(row=1, column=1)
        
         
    def remove_answer(self):
        test_original = open(askopenfilename(),'r')
        ft = open('new_test.txt','w+')
        pattern = re.compile('^(ANS|Answer|answer|Objective|Topic|Skill|Level|Page number):?\s?\s?(\w+)\.?:?(\w+)?\n?$|^Objective:?\s?.+')
      
        for line in test_original:
            line = re.sub(pattern, '', line)
            ft.write(line)    
        
        ft.close()
    
        
    def answer_maker(self):
    
        test_answers = open(askopenfilename(),'r')
        answers_text = test_answers.read() 
        fw = open('new_test.txt', 'a')
        pattern1 = re.compile(r'^(?:ANS|Answer|answer):?\s?\s?(\w+)', re.M)
    
        answers = pattern1.findall(answers_text)
    
        fw.write('\n')
        fw.write('Answers:' + '\n')   
    
        for index, line in enumerate(answers, 1):
            answer_list = (str(index) + '. ' + line + '\n')
            fw.write(answer_list)
    
       
        fw.close()    
        
        
        
            
def main():
    MyFrame().mainloop()
    

    

    
    
    
if __name__ == "__main__": main()

