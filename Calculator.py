from tkinter import * 
class calculator():
    def __init__(self,root):
        self.f=Frame(root,width="800",height="800")
        self.f.propagate(0)
        self.f.pack()
        self.f2=Frame(self.f,bg="gray",width="580",height="580")
        self.f2.place(x=180,y=40)
        self.calc=Label(self.f2,bg="white",fg="black",text="Calculator",width="50",height="2",font=('corier','15','bold'))
        self.calc.place(x="0",y="0")
        self.cf=Frame(self.f,bg="black",width="500",height="500")
        self.cf.place(x=220,y=100)
        self.enterbox=Entry(self.cf,width="15",font=('corier','41','bold'))
        self.enterbox.place(x=12,y=15)
        
        self.b1=Button(self.cf,text="C",width="8",height="2",bg="orange",fg="white",font=('corier','14','bold'),command=lambda:self.clear())
        self.b1.place(x=12,y=100)
        self.b2=Button(self.cf,text="%",width="8",height="2",font=('corier','14','bold'),command=lambda:self.show("%"))
        self.b2.place(x=135,y=100)
        self.b3=Button(self.cf,text="X",width="8",height="2",font=('corier','14','bold'),command=lambda:self.show("*"))
        self.b3.place(x=255,y=100)
        self.b4=Button(self.cf,text="/",width="8",height="2",font=('corier','14','bold'),command=lambda:self.show("/"))
        self.b4.place(x=375,y=100)
        
        self.b1=Button(self.cf,text="7",width="8",height="2",font=('corier','14','bold'),command=lambda:self.show("7"))
        self.b1.place(x=12,y=180)
        self.b2=Button(self.cf,text="8",width="8",height="2",font=('corier','14','bold'),command=lambda:self.show("8"))
        self.b2.place(x=135,y=180)
        self.b3=Button(self.cf,text="9",width="8",height="2",font=('corier','14','bold'),command=lambda:self.show("9"))
        self.b3.place(x=255,y=180)
        self.b4=Button(self.cf,text="-",width="8",height="2",font=('corier','14','bold'),command=lambda:self.show("-"))
        self.b4.place(x=375,y=180)
        
        self.b1=Button(self.cf,text="4",width="8",height="2",font=('corier','14','bold'),command=lambda:self.show("4"))
        self.b1.place(x=12,y=260)
        self.b2=Button(self.cf,text="5",width="8",height="2",font=('corier','14','bold'),command=lambda:self.show("5"))
        self.b2.place(x=135,y=260)
        self.b3=Button(self.cf,text="6",width="8",height="2",font=('corier','14','bold'),command=lambda:self.show("6"))
        self.b3.place(x=255,y=260)
        self.b4=Button(self.cf,text="+",width="8",height="2",font=('corier','14','bold'),command=lambda:self.show("+"))
        self.b4.place(x=375,y=260)
        
        self.b1=Button(self.cf,text="1",width="8",height="2",font=('corier','14','bold'),command=lambda:self.show("1"))
        self.b1.place(x=12,y=340)
        self.b2=Button(self.cf,text="2",width="8",height="2",font=('corier','14','bold'),command=lambda:self.show("2"))
        self.b2.place(x=135,y=340)
        self.b3=Button(self.cf,text="3",width="8",height="2",font=('corier','14','bold'),command=lambda:self.show("3"))
        self.b3.place(x=255,y=340)
        
        self.b1=Button(self.cf,text="00",width="8",height="2",font=('corier','14','bold'),command=lambda:self.show("00"))
        self.b1.place(x=12,y=420)
        self.b2=Button(self.cf,text="0",width="8",height="2",font=('corier','14','bold'),command=lambda:self.show("0"))
        self.b2.place(x=135,y=420)
        self.b3=Button(self.cf,text=".",width="8",height="2",font=('corier','14','bold'),command=lambda:self.show("."))
        self.b3.place(x=255,y=420)
        self.b4=Button(self.cf,text="=",bg="green",fg="white",width="8",height="6",font=('corier','14','bold'),command=lambda:self.solve())
        self.b4.place(x=375,y=340)
   
        
        self.equation=StringVar()
        self.entry_value=''
        Entry(self.cf,width="15",font=('corier','41','bold'),textvariable=self.equation).place(x=12,y=15)
        
    def show(self,value):
        self.entry_value+=(value)
        self.equation.set(self.entry_value)
        
    def clear(self):
        self.entry_value=" "
        self.equation.set(self.entry_value)
        
    def solve(self):
        result=eval(self.entry_value)
        self.equation.set(result)
    
        
    
root=Tk()
root.title("calculator")
c=calculator(root)
root.mainloop()
        
    