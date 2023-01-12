import speech_recognition as sr
import pyttsx3

from tkinter import *


class Calculator():
    def __init__(self):
        self.is_on=True
        
    engine=pyttsx3.init('sapi5')
    voices=engine.getProperty('voices')
    engine.setProperty('voice','voices[1].id')

    def speak(self,text):
        self.engine.say(text)
        self.engine.runAndWait()

    def takeCommand(self):  
        r=sr.Recognizer()
    
        with sr.Microphone() as source:
            print("Listening...")
            r.adjust_for_ambient_noise(source)
            audio=r.listen(source)
          
            try:
                statement=r.recognize_google(audio,language='en-in')
                print(f"user said:{statement}\n")
            except Exception as e:
                self.speak("Sorry, please click the button and say again")
                self.textin.set("Sorry, please click the button and say again")
                return "None"
            return statement
    def voice_calc(self):
        self.speak("Tell me what I can do for you?")
        statement = self.takeCommand().lower()
        try:    
            if "bye" in statement or "stop" in statement or "close" in statement:
                self.speak('calculator is shutting down, Good bye')
                print('calculator is shutting down, Good bye')
                self.tab1.destroy()
            elif "+" in statement or "multiply" in statement or "multiply by" in statement or "x" in statement or "divide" in statement or "-" in statement or "/" in statement or "plus" in statement or "into" in statement:
                number=(statement.replace("x","*").replace("multiply by","*").replace("divide","/").replace("hundred","100").replace("divide by", "/").replace("into","*").replace("plus","+"))
                ans=eval(number)
                self.clickbut(number)
                self.equlbut()
                self.speak(self.textin.get())
        except Exception as e:
            err="Sorry, please click the button and say again"
            self.textin.set(err)
            print(e)
            self.speak("Sorry, please click the button and say again")        
            

    def pictures(self):
        self.photo1=PhotoImage(file=r"Images/line.png")
        self.photo2=PhotoImage(file = r"Images/line0.png")
        self.photo3 = PhotoImage(file = r"Images/repeat1.png")
        self.photo4 = PhotoImage(file = r"Images/plus_sym.png")
        self.photo5 = PhotoImage(file = r"Images/minus_sym.png")
        self.photo6 = PhotoImage(file = r"Images/multi_sym.png")
        self.photo7 = PhotoImage(file = r"Images/div_sym.png")
        self.photo8 = PhotoImage(file = r"Images/equal_sym.png")
        self.photo12 = PhotoImage(file=r"Images/black_screen.png")
        self.photo13 = PhotoImage(file=r"Images/black_screen2.png")
        self.lbl01=Label(self.tab1,image=self.photo2,bd=0)
        self.lbl01.config(bg="black")
        self.lbl02=Label(self.tab1,image=self.photo8,bd=0)
        self.lbl02.config(bg="black")
        self.lbl03=Label(self.tab1,image=self.photo4,bd=0)
        self.lbl03.config(bg="black")
        self.lbl04=Label(self.tab1,image=self.photo5,bd=0)
        self.lbl04.config(bg="black")
        self.lbl05=Label(self.tab1,image=self.photo6,bd=0)
        self.lbl05.config(bg="black")
        self.lbl06=Label(self.tab1,image=self.photo7,bd=0)
        self.lbl06.config(bg="black")
        self.lbl07=Label(self.tab1,image=self.photo1,bd=0)
        self.lbl07.config(bg="black")
        self.blkscr=Label(self.tab1,image=self.photo12,bd=0)
        self.blkscr.config(bg="black")
        self.blkscr2=Label(self.tab1,image=self.photo13,bd=0)
        self.blkscr2.config(bg="black")
    
    def clickbut(self,number):
        # global operator
        self.operator=self.operator+str(number)
        self.textin.set(self.operator)

    def Textual_Ani(self):
        self.ans=str(self.ans)
        self.spl[0],self.spl[1]=str(self.spl[0]),str(self.spl[1])
        self.disp1.set("\t"+self.spl[0]+"\n     "+self.operators+"\n\t"+self.spl[1])
        self.disp2.set(self.ans)
        lbl00=Label(self.tab1,textvariable=self.disp1,bg="black",fg="red",font=("Arial",40))
        lbl00.place(x=550,y=200) #operand 1,op,2 placement

        self.lbl07.place(x=650,y=400)#line placement

        lbl02=Label(self.tab1,textvariable=self.disp2,bg="black",fg="red",font=("Arial",40))
        lbl02.place(x=790,y=405) #Ans placement

    def Pictorial_Ani(self):      
        #Operator Placement
        self.blkscr.place(x=650,y=100)
        self.blkscr2.place(x=650,y=410)
        if self.operators=='+':
            self.lbl03.place(x=550,y=250)
        elif self.operators=='-':
            self.lbl04.place(x=550,y=240)
        elif self.operators=='*' or self.operators=='X':
            self.lbl05.place(x=550,y=250)
        elif self.operators=='/':
            self.lbl06.place(x=550,y=250)

        self.grid0=650
        self.grid1=650
        self.grid2=650
                    
        for i in range(0,self.spl[0]):  #operand 1 placement
            Label(self.tab1,image=self.photo3,bd=0,bg="black").place(x=self.grid0,y=200)
            self.grid0=self.grid0+65
                
        for i in range(0,self.spl[1]):  #operand 2 placement
            Label(self.tab1,image=self.photo3,bd=0,bg="black").place(x=self.grid1,y=300)
            self.grid1=self.grid1+65
        
        self.lbl01.place(x=500,y=390)  #Line Placement

        for i in range(0,self.ans):     #Ans Placement
            Label(self.tab1,image=self.photo3,bd=0,bg="black").place(x=self.grid2,y=410)
            self.grid2=self.grid2+65

        self.lbl02.place(x=550,y=420)#equal sign placement

    def equlbut(self):
        
        self.pictures()
        self.blkscr.place(x=650,y=100)
        self.blkscr2.place(x=650,y=410)
        # global operator 
        self.disp1=StringVar()
        self.disp2=StringVar()
        
        self.ans=str(eval(self.operator.replace('X',"*")))
        self.textin.set(self.ans)
        count=0
        for i in self.operator[1:]:
            if i=='+':
                self.spl=self.operator.split('+')
                self.operators='+'
                count=count+1
            elif i=='-':
                self.spl=self.operator.split('-')
                self.operators='-'
                count=count+1
            elif i=='X':
                self.spl=self.operator.split('X')
                self.operators='X'
                count=count+1
            elif i=='/':
                self.spl=self.operator.split('/')
                self.operators="/"
                count=count+1

        #PICTORIAL ANIMATION
        if(count==1):
            try:
                self.ans=int(self.ans)
                self.spl[0],self.spl[1]=int(self.spl[0]),int(self.spl[1])  
                if(self.spl[0]>0 and self.ans>0 and self.ans<11 and self.spl[0]<11 and self.spl[1]<11):
                    self.Pictorial_Ani()
                else:
                    self.Textual_Ani()
            except Exception as e:
                self.Textual_Ani()
        self.operator=''
    def clrbut(self): 
        self.tab1.destroy()
        self.calc1=Calculator()
        self.calc1.Main()

    def clr1but(self):
        self.operator=self.operator[:-1]
        self.textin.set(self.operator)

        
    
    #KEY BINDINGS FUNCTIONS
    def one(self,event=None):
        self.clickbut("1")
    def two(self,event=None):
        self.clickbut("2")
    def three(self,event=None):
        self.clickbut("3")
    def four(self,event=None):
        self.clickbut("4")
    def five(self,event=None):
        self.clickbut("5")
    def six(self,event=None):
        self.clickbut("6")
    def seven(self,event=None):
        self.clickbut("7")
    def eight(self,event=None):
        self.clickbut("8")
    def nine(self,event=None):
        self.clickbut("9")
    def zero(self,event=None):
        self.clickbut("0")
    def dot(self,event=None):
        self.clickbut(".")
    def mul(self,event=None):
        self.clickbut("X")
    def divide(self,event=None):
        self.clickbut("/")
    def plus(self,event=None):
        self.clickbut("+")
    def minus(self,event=None):
        self.clickbut("-")
    def equal(self,event=None):
        self.equlbut()
    def bkspc(self,event=None):
        self.clr1but()
    def refresh(self,event=None):
        self.clrbut()

    def Main(self):
        self.tab1=Toplevel(first)
        self.tab1.geometry("1525x490")
        self.tab1.title("CALCULATOR")
        self.tab1.focus()
        self.tab1.config(background='Black')
        #KEY BINDING IMPLEMENTATION
        self.tab1.bind('1',self.one)
        self.tab1.bind('2',self.two)
        self.tab1.bind('3',self.three)
        self.tab1.bind('4',self.four)
        self.tab1.bind('5',self.five)
        self.tab1.bind('6',self.six)
        self.tab1.bind('7',self.seven)
        self.tab1.bind('8',self.eight)
        self.tab1.bind('9',self.nine)
        self.tab1.bind('0',self.zero)
        self.tab1.bind('+',self.plus)
        self.tab1.bind('-',self.minus)
        self.tab1.bind('*',self.mul)
        self.tab1.bind('/',self.divide)
        self.tab1.bind('.',self.dot)
        self.tab1.bind('=',self.equal)
        self.tab1.bind('<Return>',self.equal)
        self.tab1.bind('<BackSpace>',self.bkspc)
        self.tab1.bind('<F5>',self.refresh)
        self.textin=StringVar()
        self.operator=""

        
        self.photo10 = PhotoImage(file = r"Images/clrone.png")


        self.ans=Entry(self.tab1,font=("Courier New",20,'bold'),textvar=self.textin,width=45,bd=5,state="readonly")
        self.ans.pack(side="top",ipady="20",ipadx="10")



        self.mic_but=Button(self.tab1, text="voice", image=mic,command=self.voice_calc)
        self.mic_but.place(x=1143, y=0)


        #ROW1
        self.but1=Button(self.tab1,padx=14,pady=14,bd=4,bg='black',fg="blue",command=lambda:self.clickbut(1),text="1",font=("Courier New",16,'bold'))
        self.but1.place(x=10,y=110)

        self.but4=Button(self.tab1,padx=14,pady=14,bd=4,bg='black',fg="blue",command=lambda:self.clickbut(4),text="4",font=("Courier New",16,'bold'))
        self.but4.place(x=75,y=110)

        self.but7=Button(self.tab1,padx=14,pady=14,bd=4,bg='black',fg="blue",command=lambda:self.clickbut(7),text="7",font=("Courier New",16,'bold'))
        self.but7.place(x=140,y=110)

        self.butpl=Button(self.tab1,padx=14,pady=14,bd=4,bg='black',fg="green",text="+",command=lambda:self.clickbut("+"),font=("Courier New",16,'bold'))
        self.butpl.place(x=205,y=110)

        self.butreset=Button(self.tab1,padx=14,pady=73,bd=4,bg='black',fg="red",text="R\nE\nS\nE\nT",command=self.clrbut,font=("Courier New",16,'bold'))
        self.butreset.place(x=270,y=110)


        #ROW2
        self.but2=Button(self.tab1,padx=14,pady=14,bd=4,bg='black',fg="blue",command=lambda:self.clickbut(2),text="2",font=("Courier New",16,'bold'))
        self.but2.place(x=10,y=180)

        self.but5=Button(self.tab1,padx=14,pady=14,bd=4,bg='black',fg="blue",command=lambda:self.clickbut(5),text="5",font=("Courier New",16,'bold'))
        self.but5.place(x=75,y=180)

        self.but8=Button(self.tab1,padx=14,pady=14,bd=4,bg='black',fg="blue",command=lambda:self.clickbut(8),text="8",font=("Courier New",16,'bold'))
        self.but8.place(x=140,y=180)

        self.butsub=Button(self.tab1,padx=14,pady=14,bd=4,bg='black',text="-",fg="green",command=lambda:self.clickbut("-"),font=("Courier New",16,'bold'))
        self.butsub.place(x=205,y=180)


        #ROW3
        self.but3=Button(self.tab1,padx=14,pady=14,bd=4,bg='black',fg="blue",command=lambda:self.clickbut(3),text="3",font=("Courier New",16,'bold'))
        self.but3.place(x=10,y=250)

        self.but6=Button(self.tab1,padx=14,pady=14,bd=4,bg='black',fg="blue",command=lambda:self.clickbut(6),text="6",font=("Courier New",16,'bold'))
        self.but6.place(x=75,y=250)

        self.but9=Button(self.tab1,padx=14,pady=14,bd=4,bg='black',fg="blue",command=lambda:self.clickbut(9),text="9",font=("Courier New",16,'bold'))
        self.but9.place(x=140,y=250)

        self.butml=Button(self.tab1,padx=14,pady=14,bd=4,bg='black',fg="green",text="X",command=lambda:self.clickbut("X"),font=("Courier New",16,'bold'))
        self.butml.place(x=205,y=250)


        #ROW4
        self.but0=Button(self.tab1,padx=14,pady=14,bd=4,bg='black',fg="blue",command=lambda:self.clickbut(0),text="0",font=("Courier New",16,'bold'))
        self.but0.place(x=10,y=320)

        self.butdiv=Button(self.tab1,padx=14,pady=14,bd=4,bg='black',fg="green",text="/",command=lambda:self.clickbut("/"),font=("Courier New",16,'bold'))
        self.butdiv.place(x=205,y=320)

        self.butdot=Button(self.tab1,padx=46,pady=14,bd=4,bg='black',fg="blue",text=".",command=lambda:self.clickbut("."),font=("Courier New",16,'bold'))
        self.butdot.place(x=75,y=320)


        #ROW5
        self.butequal=Button(self.tab1,padx=111,pady=12,bd=4,bg='black',fg="green",command=self.equlbut,text="=",font=("Courier New",16,'bold'))
        self.butequal.place(x=10,y=390)

        self.butclear=Button(self.tab1,padx=14,pady=14,bd=4,bg='black',fg="white",image=self.photo10,command=self.clr1but,font=("Courier New",16,'bold'))
        self.butclear.place(x=270,y=390)


class Sici():
    engine=pyttsx3.init('sapi5')
    voices=engine.getProperty('voices')
    engine.setProperty('voice','voices[1].id')

    def speak(self,text):
        self.engine.say(text)
        self.engine.runAndWait()

    def takeCommand(self):  
        r=sr.Recognizer()
    
        with sr.Microphone() as source:
            print("Listening...")
            r.adjust_for_ambient_noise(source)
            audio=r.listen(source)
          
            try:
                statement=r.recognize_google(audio,language='en-in')
                print(f"user said:{statement}\n")
            except Exception as e:
                self.speak("Sorry, please click the button and say again")
                self.ans.delete("1.0","end")
                self.ans.insert("1.0","Sorry, please click the button and say again")
                return "None"
            return statement
    def voice_calc(self):
        self.speak("Tell me what I can do for you?")
        statement = self.takeCommand().lower()
        try:    
            if "bye" in statement or "stop" in statement or "close" in statement:
                self.speak('SICI is shutting down, Good bye')
                print('SICI is shutting down, Good bye')
                self.tab2.destroy()
            elif "principal" in statement or "rate" in statement or "time" in statement:
                self.stat=statement.replace('thousand',"1000").replace("to","2").replace("fire","5").replace("hundred","100").replace("x","time")
                self.txt1.delete(0,"end")
                self.txt2.delete(0,"end")
                self.txt3.delete(0,"end")
                self.txt1.insert(0,self.stat.split("principal ",1)[1].split("rate ",1)[0])
                self.txt2.insert(0,self.stat.split("principal ",1)[1].split("rate ",1)[1].split("time ",1)[0])
                self.txt3.insert(0,self.stat.split("principal ",1)[1].split("rate ",1)[1].split("time ",1)[1])
                self.evaluate()
                self.speak(self.ans.get("1.0","end"))
                

        except Exception as e:
            self.ans.delete("1.0","end")
            self.ans.insert("1.0","Sorry, please click the button and say again")
            print(e)
            self.speak("Sorry, please click the button and say again")

    def evaluate(self):
        self.ci_image=PhotoImage(file=r"Images/ci_image.png")
        self.A=PhotoImage(file=r"Images/A_image.png")
        self.redline=PhotoImage(file=r"Images/redline.png")
        self.si_image=PhotoImage(file = r"Images/si_image.png")
        

        self.strP=str(self.txt1.get())
        self.strR=str(self.txt2.get())
        self.strT=str(self.txt3.get())
        self.ans.delete("1.0","end")
        self.Principal=float(self.txt1.get())
        self.Rate=float(self.txt2.get())
        self.Time=float(self.txt3.get())
        self.SI=(self.Principal*self.Rate*self.Time)/100
        self.Amount = self.Principal * (pow((1 + self.Rate / 100), self.Time))
        self.strA = str(self.Amount)
        self.CI=round(self.Amount-self.Principal,2)
        self.ans.insert("end","SIMPLE INTEREST=")
        self.ans.insert("end",self.SI)
        self.ans.insert("end","\nCOMPOUND INTEREST=")
        self.ans.insert("end",self.CI)
        #SI DESIGN
        Label(self.tab2,image=self.si_image,bd=0).place(x=1000,y=0)
        self.disp0=StringVar()
        self.disp0.set("=  " + self.strP + "  x  " + self.strR + "  x  " + self.strT)
        self.lbl0 = Label(self.tab2,textvariable=self.disp0,bg="black",font=('Helvetica bold',30), fg="white").place(x=1050,y=140)
        self.lbl1 = Label(self.tab2,image=self.redline,bg="black").place(x=1100,y=200)
        self.lbl2 = Label(self.tab2,text="100",bg="black",font=('Helvetica bold',30), fg="white").place(x=1219,y=210)
        
        #A DESIGN
        self.disp1=StringVar()
        self.disp1.set("= " + self.strP + " (1 + " + self.strR + " / 100)" + self.strT)
        Label(self.tab2,image=self.A,bd=0).place(x=1000,y=290)
        self.lbl3 = Label(self.tab2,textvariable=self.disp1,bg="black",font=('Helvetica bold',25), fg="white").place(x=1050,y=400)
        
        #CI DESIGN
        self.disp2=StringVar()
        self.disp2.set("= " + self.strA + " - " + self.strP)
        Label(self.tab2,image=self.ci_image,bd=0,bg="black").place(x=1000,y=500)
        self.lbl4 = Label(self.tab2,textvariable=self.disp2,bg="black",fg="white",font=('Helvetica bold',25)).place(x=1060,y=600)



    def Main(self):
        self.tab2=Toplevel(first)
        self.tab2.geometry("1525x1525")
        # self.tab2.resizable(0,0)
        self.tab2.state('zoomed')
        self.tab2.title("SIMPLE INTERST-COMPOUND INTEREST")
        self.tab2.config(background='black')
        

        self.ans = Text(self.tab2,font=("Courier New",20,'bold'),width=30,height=2,bd=4,bg="light grey")
        self.ans.place(x=500,y=0)

        self.lbl1 = Label(self.tab2, text="PRINCIPAL",font=("Courier New",20,'bold'),bg="black",fg="white")   
        self.lbl1.place(x=0, y=150)

        self.txt1 = Entry(self.tab2,font=("Courier New",18))
        self.txt1.place(x=200, y=150)

        self.lbl2 = Label(self.tab2, text="RATE", font=("Courier New",20,'bold'),bg="black",fg="white")
        self.lbl2.place(x=0, y=285)

        self.txt2 = Entry(self.tab2, font=("Courier New",18))
        self.txt2.place(x=200, y=285)

        self.lbl3 = Label(self.tab2, text="TIME(IN YEARS)", font=("Courier New",18,'bold'),bg="black",fg="white")
        self.lbl3.place(x=0, y=420)

        self.txt3 = Entry(self.tab2, font=("Courier New",18))
        self.txt3.place(x=200, y=420)

        self.Eval_but = Button(self.tab2, text ="EVALUATE",font=("Courier New",20,'bold'), command=self.evaluate)
        self.Eval_but.place(x=650, y=270) 

        self.mic_butt = Button(self.tab2, text="voice", bd=2,image=mic,command=self.voice_calc)
        self.mic_butt.place(x=411, y=0)   

class Proloss():
    engine=pyttsx3.init('sapi5')
    voices=engine.getProperty('voices')
    engine.setProperty('voice','voices[1].id')

    def speak(self,text):
        self.engine.say(text)
        self.engine.runAndWait()

    def takeCommand(self):  
        r=sr.Recognizer()
    
        with sr.Microphone() as source:
            print("Listening...")
            r.adjust_for_ambient_noise(source)
            audio=r.listen(source)
          
            try:
                statement=r.recognize_google(audio,language='en-in')
                print(f"user said:{statement}\n")
            except Exception as e:
                self.ans.delete("1.0","end")
                self.speak("Sorry, please click the button and say again")
                self.ans.insert("1.0","Sorry, please click the button and say again")
                return "None"
            return statement
    def voice_calc(self):
        self.speak("Tell me what I can do for you?")
        statement = self.takeCommand().lower()
        try:    
            if "bye" in statement or "stop" in statement or "close" in statement:
                self.speak('calculator is shutting down, Good bye')
                print('calculator is shutting down, Good bye')
                self.tab3.destroy()

            elif "cp" in statement or "cost price" in statement:
                stat=statement.replace("sp","selling price").replace("cp","cost price").replace("hp","selling price")
                self.txt1.delete(0,"end")
                self.txt2.delete(0,"end")
                if(stat[0]=="c"):
                    self.txt1.insert(0,stat.split("cost price ",1)[1].split(" selling",1)[0])
                    self.txt2.insert(0,stat.split("selling price ",1)[1])
                    self.evaluate()
                elif(stat[0]=="s"):
                    self.txt2.insert(0,stat.split("selling price ",1)[1].split(" cost",1)[0])
                    self.txt1.insert(0,stat.split("cost price ",1)[1])
                    self.evaluate()
                self.speak(self.ans.get("1.0","end"))
        except Exception as e:
            self.ans.delete("1.0","end")
            self.ans.insert("1.0","Sorry, please click the button and say again")
            print(e)
            self.speak("Sorry, please click the button and say again") 
    def evaluate(self):
        self.ans.delete("1.0","end")
        self.sp=float(self.txt2.get())
        self.cp=float(self.txt1.get())
        self.blackscreen = PhotoImage(file="Images/black_screen3.png")
        if self.sp<self.cp:
            self.loss=self.cp-self.sp
            self.lossper=(self.loss*100)/self.cp
            self.ans.insert("end","LOSS=")
            self.ans.insert("end",self.loss)
            self.ans.insert("end","\nLOSS %=")
            self.ans.insert("end",self.lossper)

            #design
            self.lossimage = PhotoImage(file="Images/loss_image.png")
            self.lossperimage = PhotoImage(file="Images/lossper_image.png")
            self.redline=PhotoImage(file=r"Images/redline.png")
            self.SPstr = str(self.sp)
            self.CPstr = str(self.cp)

                #loss
            self.blacklabel = Label(self.tab3,image=self.blackscreen,bd=0,bg='black')
            self.blacklabel.place(x=990,y=0)
            self.blacklabel0 = Label(self.tab3,image=self.blackscreen,bd=0,bg='black')
            self.blacklabel0.place(x=950,y=200)
            self.disp0 = StringVar()
            self.disp0.set("= " + self.CPstr + " - " + self.SPstr)
            self.losslabel = Label(self.tab3,image=self.lossimage,bd=0,bg="black")
            self.losslabel.place(x=1050,y=0)
            self.losslabel0 = Label(self.tab3,textvariable=self.disp0,font=('Helvetica bold',30),bg="black",fg="white")
            self.losslabel0.place(x=1220,y=100)

                #loss %
            self.disp1 = StringVar()
            self.disp1.set("= " + str(self.loss) + " x 100")
            self.lossperlabel = Label(self.tab3,image=self.lossperimage,bd=0,bg="black")
            self.lossperlabel.place(x=950,y=200)
            self.lossperlabel0 = Label(self.tab3,textvariable=self.disp1,font=('Helvetica bold',30),bg="black",fg="white")
            self.lossperlabel0.place(x=1163,y=350)
            self.line= Label(self.tab3,image=self.redline,bd=0,bg="black")
            self.line.place(x=1183,y=397)
            self.lossperlabel2 = Label(self.tab3,text=self.CPstr,font=('Helvetica bold',30),bg="black",fg="white")
            self.lossperlabel2.place(x=1250,y=410)

        elif self.sp>self.cp:
            self.profit=self.sp-self.cp
            self.profitper=(self.profit*100)/self.cp
            self.ans.insert("end","PROFIT=")
            self.ans.insert("end",self.profit)
            self.ans.insert("end","\nPROFIT %=")
            self.ans.insert("end",self.profitper)

            #design
            self.profitimage = PhotoImage(file=r"Images/profit_image.png")
            self.profitperimage = PhotoImage(file=r"Images/profitper_image.png")
            self.redline=PhotoImage(file=r"Images/redline.png")
            self.SPstr = str(self.sp)
            self.CPstr = str(self.cp)

                #profit
            self.blacklabel = Label(self.tab3,image=self.blackscreen,bd=0,bg='black')
            self.blacklabel.place(x=990,y=0)
            self.blacklabel0 = Label(self.tab3,image=self.blackscreen,bd=0,bg='black')
            self.blacklabel0.place(x=950,y=200)
            self.disp0 = StringVar()
            self.disp0.set("= " + self.SPstr + " - " + self.CPstr)
            self.profitlabel = Label(self.tab3,image=self.profitimage,bd=0,bg="black")
            self.profitlabel.place(x=1050,y=0)
            self.profitlabel0 = Label(self.tab3,textvariable=self.disp0,font=('Helvetica bold',30),bg="black",fg="white")
            self.profitlabel0.place(x=1220,y=100)
                #profit %
            self.disp1 = StringVar()
            self.disp1.set("= " + str(self.profit) + " x 100")
            self.profitperlabel = Label(self.tab3,image=self.profitperimage,bd=0,bg="black")
            self.profitperlabel.place(x=950,y=200)
            self.profitperlabel0 = Label(self.tab3,textvariable=self.disp1,font=('Helvetica bold',30),bg="black",fg="white")
            self.profitperlabel0.place(x=1163,y=350)
            self.line= Label(self.tab3,image=self.redline,bd=0,bg="black")
            self.line.place(x=1183,y=397)
            self.profitperlabel2 = Label(self.tab3,text=self.CPstr,font=('Helvetica bold',30),bg="black",fg="white")
            self.profitperlabel2.place(x=1250,y=410)
                    
        else:
            self.ans.insert("end","PROFIT=0")
            self.ans.insert("end","\nPROFIT %=0")
            self.ans.insert("end","\nLOSS=0")      
            self.ans.insert("end","\nLOSS %=0")


            #Design
            self.proloimage = PhotoImage(file="Images/prolo_image.png")
            self.proloperimage = PhotoImage(file="Images/proloper_image.png")
            self.redline=PhotoImage(file=r"Images/redline.png")
            self.SPstr = str(self.sp)
            self.CPstr = str(self.cp)

            self.blacklabel = Label(self.tab3,image=self.blackscreen,bd=0,bg='black')
            self.blacklabel.place(x=990,y=0)
            self.blacklabel0 = Label(self.tab3,image=self.blackscreen,bd=0,bg='black')
            self.blacklabel0.place(x=950,y=200)
            self.disp0=StringVar()
            self.disp0.set("= " + self.SPstr + " - " + self.CPstr)
            self.prololabel = Label(self.tab3, image=self.proloimage,bd=0,bg="black")
            self.prololabel.place(x=1050, y=0)
            self.prololabel0 = Label(self.tab3,textvariable=self.disp0,font=('Helvetica bold',30),bg="black",fg="white")
            self.prololabel0.place(x=1250,y=100)

            self.disp1=StringVar()
            self.disp1.set("= " + "0" + " x 100")
            self.proloperlabel = Label(self.tab3, image=self.proloperimage,bd=0,bg="black")
            self.proloperlabel.place(x=950,y=200)
            self.proloperlabel0 = Label(self.tab3,textvariable=self.disp1,font=('Helvetica bold',30),bg="black",fg="white")
            self.proloperlabel0.place(x=1163,y=350)
            self.line= Label(self.tab3,image=self.redline,bd=0,bg="black")
            self.line.place(x=1183,y=397)
            self.proloperlabel1 = Label(self.tab3,text=self.SPstr,font=('Helvetica bold',30),bg="black",fg="white")
            self.proloperlabel1.place(x=1250,y=410)
            


    def Main(self):
        self.tab3=Toplevel(first)
        self.tab3.geometry("1525x490")
        self.tab3.title("PROFIT-LOSS")
        self.tab3.resizable(0,0)
        self.tab3.config(background='black')
        

        self.ans = Text(self.tab3,font=("Courier New",20,'bold'),width=30,height=4,bd=4,bg="light grey")
        self.ans.place(x=500,y=0)

        self.lbl1 = Label(self.tab3, text="COST\nPRICE",font=("Courier New",20,'bold'),bg="black",fg="white")   
        self.lbl1.place(x=0, y=150)

        self.txt1 = Entry(self.tab3,font=("Courier New",20))
        self.txt1.place(x=200, y=160)

        self.lbl2 = Label(self.tab3, text="SELLING\nPRICE", font=("Courier New",20,'bold'),bg="black",fg="white")
        self.lbl2.place(x=0, y=400)

        self.txt2 = Entry(self.tab3, font=("Courier New",20))
        self.txt2.place(x=200, y=420)

        self.Eval_but = Button(self.tab3,command=self.evaluate,text ="EVALUATE",font=("Courier New",20,'bold'))
        self.Eval_but.place(x=650, y=270)

        self.mic_butt = Button(self.tab3, text="voice",image=mic,bd=2, command=self.voice_calc)
        self.mic_butt.place(x=400, y=30) 


class Percentage():

    def evaluate(self):
        self.ans.delete("1.0","end")
        
        self.box1=str(self.txt1.get())
        self.box2=str(self.txt2.get())
        self.box3=str(self.txt3.get())
        self.box4=str(self.txt4.get())
        self.box5=str(self.txt5.get())
        self.box6=str(self.txt6.get())
        if(self.box1=="" and self.box2==""):
            pass
        else:
            self.output=(int(self.box2)*int(self.box1)/100)
            self.ans.insert('end',"1)"+str(self.output)+"\n")
        if(self.box3=="" and self.box4==""):
            pass
        else:
            self.ans.insert('end',"2)"+str(((int(self.box3)/int(self.box4))*100))+"\n")

        if(self.box5=="" and self.box6==""):
            pass
        else:
            if(int(self.box5)<int(self.box6)):
                answer=((int(self.box6)-int(self.box5))/abs(int(self.box5)))*100
                self.ans.insert('end',"3)"+str(self.box6)+" is a " + str(answer)+ "%" + " increase of " + str(self.box5) + "\n")

            elif(int(self.box5)==int(self.box6)):
                self.ans.insert('end',"3)"+str(self.box6)+" is a 0" + "%" + " increase of "+ str(self.box5) + "\n")
            else:
                answer=((int(self.box5)-int(self.box6))/abs(int(self.box5)))*100
                self.ans.insert('end',"3)"+str(self.box6)+" is a " + str(answer)+ "%" + " decrease of " + str(self.box5) + "\n")
            
    
    def Main(self):
        self.tab4=Toplevel(first)
        self.tab4.title("PERCENTAGE CALCULATOR")
        self.tab4.geometry('805x545')
        self.tab4.resizable(0,0)
        self.tab4.config(bg="black")

        self.ans = Text(self.tab4,font=("Courier New",20,'bold'),width=95,height=4,bd=4,bg="light grey")
        self.ans.place(x=0,y=0)

        self.greyscreen = PhotoImage(file="Images/grey_screen.png")
        self.greylabel = Label(self.tab4,image=self.greyscreen,bd=0,bg="yellow")
        self.greylabel.place(x=0,y=185)
        #ans 1
        self.txt01=StringVar()
        self.disp1=StringVar()
        self.disp1.set("1)What is          % of              ?                 ")

        self.lbl1=Label(self.tab4,textvariable=self.disp1,font=("Times",20),bg="red",fg="white")
        self.lbl1.place(x=0,y=200)

        self.txt1=Entry(self.tab4,font=("Times",20),fg="white",bg="red",bd=4, justify= CENTER)
        self.txt1.place(x=89,y=200,height=38, width=80)

        self.txt2=Entry(self.tab4,font=("Times",20),fg="white",bg="red",bd=4, justify= CENTER)
        self.txt2.place(x=240,y=200,height=38, width=80)

        #ans 2
        self.disp2=StringVar()
        self.disp2.set("2)             is what % of                    ?        ")

        self.lbl2=Label(self.tab4,textvariable=self.disp2,font=("Times",20),bg="green",fg="white")
        self.lbl2.place(x=0,y=320)

        self.txt3=Entry(self.tab4,font=("Times",20),fg="white",bg="green",bd=4, justify= CENTER)
        self.txt3.place(x=25,y=320,height=38, width=80)

        self.txt4=Entry(self.tab4,font=("Times",20),fg="white",bg="green",bd=4, justify= CENTER)
        self.txt4.place(x=260,y=320,height=38, width=127)

        #ans 3
        

        self.lbl3=Label(self.tab4,text="3)What is the percentage Increase/Decrease   ",font=("Times",19),bg="blue",fg="white",justify="left")
        self.lbl3.place(x=0,y=440)
        
        self.lbl4 = Label(self.tab4, text="From                           to                        ? ",font=("Times",20),bg="blue",fg="white")
        self.lbl4.place(x=0,y=480)

        self.txt5=Entry(self.tab4,font=("Times",20),fg="white",bg="blue",bd=4, justify= CENTER)
        self.txt5.place(x=75,y=480,height=38, width=157)

        self.txt6=Entry(self.tab4,font=("Times",20),fg="white",bg="blue",bd=4, justify= CENTER)
        self.txt6.place(x=285,y=480,height=38, width=143) 

        self.Eval_but = Button(self.tab4,text ="EVALUATE",command=self.evaluate,font=("Courier New",20,'bold'))
        self.Eval_but.place(x=650, y=250) 

class shapes:
    def controls(self):
        rad=float()
        self.side=Entry(self.tab5,font=("Courier New",20))
        self.Length=Entry(self.tab5,font=("Courier New",20))
        self.Breadth=Entry(self.tab5,font=("Courier New",20))
        self.Radius=Entry(self.tab5,font=("Courier New",20),textvariable=rad)
        self.side0=Entry(self.tab5,font=("Courier New",20))
        self.side1=Entry(self.tab5,font=("Courier New",20))
        self.side2=Entry(self.tab5,font=("Courier New",20))
        self.height=Entry(self.tab5,font=("Courier New",20))
        self.base=Entry(self.tab5,font=("Courier New",20))
        self.lbl0=Label(self.tab5,font=("Courier New",20,'bold'),bg="black",fg="white")
        self.lbl1=Label(self.tab5,font=("Courier New",20,'bold'),bg="black",fg="white")
        self.lbl2=Label(self.tab5,font=("Courier New",20,'bold'),bg="black",fg="white")

    def forget0(self,widget):
        self.widget=widget
        self.widget.place_forget()
    
    def resetbut(self): 
        self.tab5.destroy()
        self.shapes1=shapes()
        self.shapes1.Main()

    def selected0(self,*arg):
        self.arg=arg
        self.arg=self.clicked.get()
        self.blackscreen=PhotoImage(file="Images/black_screen.png")
        self.lblblk=Label(self.tab5,image=self.blackscreen,bd=0,bg="black")
        
        #ANIMATION-1
        if(self.arg == "SQUARE"):
            self.lblblk.place(x=840,y=80)
            self.square=PhotoImage(file=r"Images/squarecard.png")
            self.lblsq=Label(self.tab5,image=self.square,bd=0,bg="black")
            self.lblsq.place(x=850,y=80)
        elif(self.arg == "TRIANGLE"):
            self.lblblk.place(x=840,y=80)
            self.triangle=PhotoImage(file=r"Images/trianglecard.png")
            self.lblta=Label(self.tab5,image=self.triangle,bd=0,bg="black")
            self.lblta.place(x=850,y=80)
        elif(self.arg == "RECTANGLE"):
            self.lblblk.place(x=840,y=80)
            self.rectangle=PhotoImage(file=r"Images/rectanglecard.png")
            self.lblrt=Label(self.tab5,image=self.rectangle,bd=0,bg="black")
            self.lblrt.place(x=850,y=80)
        elif(self.arg == "CIRCLE"):
            self.lblblk.place(x=840,y=80)
            self.circle=PhotoImage(file=r"Images/circlecard.png")
            self.lblcc=Label(self.tab5,image=self.circle,bd=0,bg="black")
            self.lblcc.place(x=850,y=80)

        self.arg0=self.clicked1.get()

        self.disp=StringVar()
        self.ShapeLbl=Label(self.tab5,font=("Courier New",20,'bold'),bg="black",textvariable=self.disp)
        self.ShapeLbl.place(x=750,y=520)

        #ANIMATION-2
        if(self.arg0 == "PERIMETER/CIRCUMFERENCE"):
        
            self.disp=StringVar()
            self.ShapeLbl=Label(self.tab5,font=("Courier New",20,'bold'),bg="black",textvariable=self.disp)
            self.ShapeLbl.place(x=750,y=520)
            if(self.arg == "TRIANGLE"):
                self.ShapeLbl.config(fg="red")
                self.disp.set("PERIMETER OF TRIANGLE = S1 + S2 + S3      ")
            elif(self.arg == "SQUARE"):
                self.ShapeLbl.config(fg="yellow")
                self.disp.set("PERIMETER OF SQUARE = S x 4               ")
            elif(self.arg == "RECTANGLE"):
                self.ShapeLbl.config(fg="blue")
                self.disp.set("PERIMETER OF RECTANGLE = 2(L + B)         ")
            elif(self.arg == "CIRCLE"):
                self.ShapeLbl.config(fg="green")
                self.disp.set("CIRCUMFERENCE OF CIRCLE = 2(3.14(PIE) x r)")

        elif(self.arg0 == "AREA"):
            if(self.arg == "TRIANGLE"):
                self.ShapeLbl.config(fg="red")
                self.disp.set("AREA OF TRIANGLE = H x B              ")
            elif(self.arg == "SQUARE"):
                self.ShapeLbl.config(fg="yellow")
                self.disp.set("AREA OF SQUARE = S x S                ")
            elif(self.arg == "RECTANGLE"):
                self.ShapeLbl.config(fg="blue")
                self.disp.set("AREA OF RECTANGLE = L x B             ")
            elif(self.arg == "CIRCLE"):
                self.ShapeLbl.config(fg="green")
                self.disp.set("AREA OF CIRCLE = 2(3.14(PIE) x (r + r)")

        if self.arg=="SQUARE" and (self.arg0=="PERIMETER/CIRCUMFERENCE" or self.arg0=="AREA"):
            self.forget0(self.side1)
            self.forget0(self.side2)
            self.forget0(self.base)
            self.forget0(self.Breadth)
            self.forget0(self.lbl1)
            self.forget0(self.lbl2)

            self.lbl0.config(text="SIDE(S)")
            self.lbl0.place(x=0,y=400)
            
            self.side.place(x=200,y=400)
        elif self.arg=="RECTANGLE" and (self.arg0=="PERIMETER/CIRCUMFERENCE" or self.arg0=="AREA"):
            self.forget0(self.side1)
            self.forget0(self.base)
            self.forget0(self.side2)
            self.forget0(self.lbl2)
            
            self.lbl0.config(text="LENGTH(L)")
            self.lbl0.place(x=0,y=400)
            
            self.Length.place(x=200,y=400)
            self.lbl1.config(text="BREADTH(B)")
            self.lbl1.place(x=0,y=530)

            self.Breadth.place(x=200,y=530)
        elif self.arg=="CIRCLE" and (self.arg0=="PERIMETER/CIRCUMFERENCE" or self.arg0=="AREA"):
            self.forget0(self.side1)
            self.forget0(self.side2)
            self.forget0(self.base)
            self.forget0(self.Breadth)
            self.forget0(self.lbl1)
            self.forget0(self.lbl2)

            self.lbl0.config(text="RADIUS(R)")
            self.lbl0.place(x=0,y=400)
            
            self.Radius.place(x=200,y=400)
        elif self.arg=="TRIANGLE":
            if self.arg0=="PERIMETER/CIRCUMFERENCE":
                self.forget0(self.Breadth)
                self.forget0(self.base)
                self.lbl0.config(text="SIDE(S1)")
                self.lbl0.place(x=0,y=400)
                
                self.side0.place(x=200,y=400)
                self.lbl1.config(text="SIDE(S2)")
                self.lbl1.place(x=0,y=480)
                self.side1.place(x=200,y=480)
                self.lbl2.config(text="SIDE(S3)")
                self.lbl2.place(x=0,y=560)

                self.side2.place(x=200,y=560)
            else:
                self.forget0(self.side2)
                self.forget0(self.lbl2)
                self.forget0(self.side1)

                self.lbl0.config(text="HEIGHT(H)")
                self.lbl0.place(x=0,y=400)
                
                self.height.place(x=200,y=400)
                self.lbl1.config(text="BASE(B)")
                self.lbl1.place(x=0,y=530)
                self.base.place(x=200,y=530)

    def evaluate(self):   
        self.PIE=3.14
        if self.arg=="CIRCLE":
            self.r=float(self.Radius.get())
            if self.arg0=="PERIMETER/CIRCUMFERENCE":
                self.perimeter=2*(self.PIE*self.r)
                self.perimeter=str(self.perimeter)
                self.r=str(self.r)
                self.ans.delete("1.0","end")
                self.ans.insert("end","Circumference of Circle(For R="+self.r+")="+self.perimeter)

            else:
                self.area=self.PIE*(self.r*self.r)
                self.ans.delete("1.0","end")
                self.ans.insert("end","Area of Circle(For R="+str(self.r)+")="+str(self.area))
            
        elif self.arg=="TRIANGLE":
            if self.arg0=="AREA":
                self.h=float(self.height.get())
                self.b=float(self.base.get())
                self.area=0.5*self.h*self.b
                self.h=str(self.h)
                self.b=str(self.b)
                self.area=str(self.area)
                self.ans.delete("1.0","end")
                self.ans.insert("end","Area of Triangle(For H="+self.h+" ,B="+self.b+")="+self.area)
            else:
                self.s0=float(self.side0.get())
                self.s1=float(self.side1.get())
                self.s2=float(self.side2.get())
                self.perimeter=self.s0+self.s1+self.s2
                self.s0=str(self.s0)
                self.s1=str(self.s1)
                self.s2=str(self.s2)
                self.perimeter=str(self.perimeter)
                self.ans.delete("1.0","end")
                self.ans.insert("end","Area of Triangle(For S0="+self.s0+" ,S1="+self.s1+",S2="+self.s2+")="+self.perimeter)
       
        elif self.arg=="RECTANGLE":
            self.l=float(self.Length.get())
            self.b=float(self.Breadth.get())

            if self.arg0=="PERIMETER/CIRCUMFERENCE":
                self.p=2*(self.l + self.b)
                self.ans.delete("1.0","end")
                self.ans.insert("end","Perimeter of Rectangle = " + str(self.p))
            elif self.arg0=="AREA":
                self.ra=self.l*self.b
                self.ra=str(self.ra)
                self.ans.delete("1.0","end")
                self.ans.insert("end","Area of Rectangle = " + self.ra)
       
        elif self.arg=="SQUARE":
           
            self.s=float(self.side.get())
            if self.arg0=="PERIMETER/CIRCUMFERENCE":
                self.sp=self.s*4
                self.sp=str(self.sp)
                self.ans.delete("1.0","end")
                self.ans.insert("1.0","Perimeter of Square = " + self.sp)
            elif self.arg0=="AREA":
                self.sa=self.s*self.s
                self.sa=str(self.sa)
                self.ans.delete("1.0","end")
                self.ans.insert("1.0","Area of Square = " + self.sa)


    def Main(self):
        self.tab5=Toplevel(first)
        self.tab5.state('zoomed')
        self.tab5.resizable(0,0)
        self.tab5.title("2D SHAPES")
        self.tab5.config(background='black')

        self.clicked1=StringVar()
        self.clicked=StringVar()
        self.clicked.set("SQUARE")
        self.clicked1.set("PERIMETER/CIRCUMFERENCE")

        self.ans = Text(self.tab5,font=("Courier New",20,'bold'),width=95,height=1.5,bd=4,bg="light grey")
        self.ans.place(x=0,y=0)
    
        self.Shapels=["TRIANGLE","SQUARE","RECTANGLE","CIRCLE"]
        self.Formulas={"PERIMETER/CIRCUMFERENCE" : "1","AREA" : "2"}
        self.shapes=OptionMenu(self.tab5, self.clicked, *self.Shapels,command=self.selected0)
        self.shapes.place(x=30, y=140)
        self.shapes.config(width=15,bg="green",font=("Courier New",18,"bold"),fg="red")
    
        self.formula=OptionMenu(self.tab5, self.clicked1, *self.Formulas,command=self.selected0)
        self.formula.place(x=30, y=270)
        self.formula.config(width=25,bg="green",font=("Courier New",18,"bold"),fg="red")
        self.controls()
        self.Eval_but=Button(self.tab5,text="EVALUATE",font=("Courier New",20,'bold'),command=self.evaluate)
        self.Eval_but.place(x=700,y=400)

        self.reset_but = Button(self.tab5,text="RESET",font=("Courier New",20,'bold'),command=self.resetbut)
        self.reset_but.place(x=900,y=400)
        
        self.tab5.mainloop()


first=Tk()
first.title("FIRST PAGE")
first.config(background="black")
first.geometry("1530x400")
first.resizable(0,0)

calc=Calculator()
SICI=Sici()
PL=Proloss()
per=Percentage()
sh=shapes()

calc_button = PhotoImage(file="Images/calc_button.png")
sici_button = PhotoImage(file="Images/sici_button.png")
pl_button = PhotoImage(file="Images/pl_button.png")
per_button = PhotoImage(file="Images/per_button.png")
shapes_button = PhotoImage(file="Images/shapes_button.png")

calculator=Button(first,bd=4,bg="red",image=calc_button,text="CALCULATOR",command=calc.Main,font=("Courier New",16,'bold'))
sici=Button(first,bd=4,bg="green",image=sici_button,text="SIMPLE INTEREST/COMPOUND INTEREST",command=SICI.Main,font=("Courier New",16,'bold'))
proloss=Button(first,bd=4,bg="white",image=pl_button,text="PROFIT/LOSS",font=("Courier New",16,'bold'),command=PL.Main)
percentage=Button(first,bd=4,bg="yellow",image=per_button,text="PERCENTAGE CALCULATOR",font=("Courier New",16,'bold'),command=per.Main)
Shapes=Button(first,bd=4,bg="purple",image=shapes_button,text="SHAPES",command=sh.Main,font=("Courier New",16,'bold')) 

calculator.pack(side="left")
sici.pack(side="left")
proloss.pack(side="left")
percentage.pack(side="left")
Shapes.pack(side="left")
mic = PhotoImage(file = r"Images/mic_on.png")
first.mainloop()