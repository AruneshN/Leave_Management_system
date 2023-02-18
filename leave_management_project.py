import tkinter as Tk
import tkinter 
import tkinter as tk
from tkinter import ttk
from tkinter import*
import pymysql
from tkinter import messagebox
from tkinter import ttk
from tkcalendar import DateEntry
from tkcalendar import*

db_connection =pymysql.connect(
    host="localhost",
    user="root",
    passwd="arunesh5488",
    database="leave_management"
)
my_database=db_connection.cursor()
print("server connected")
name="DHANALAKSHMI"
IDNUM=9080
#______________________________________________login_______________________________________________________________

def bg():
    rt=tkinter.Tk()
    rt.geometry("1366x768")
    rt.config(bg="#342D7E")
    FFrame=Frame(rt,bg="black",highlightbackground="black",highlightthickness=4)
    FFrame.pack(fill="both",expand="yes",padx=200,pady=55)
    
    def dashboard():
        sql_statement="SELECT leave_start_date,leave_end_date,type_of_leave FROM empoyee_leave_management"
        my_database.execute(sql_statement)
        output=my_database.fetchall()
        print(output[0])
        a=output[0]
        b=a[0]
        print(output[0])
        c=output[0]
        d=c[1] 
        print(output[0])
        e=output[0]
        f=e[2]
        sdate=(b)
        a=(sdate[0:2])
        a=int(a)
        print(a)
        ddate=(d)
        s=(ddate[0:2])
        s=int(s)
        print(s)
        dur=s-a
        print(dur)
            
        
        dFrame=Frame(FFrame,bg="white",highlightbackground="black",
                     highlightthickness=4)
        dFrame.pack(fill="both",expand="yes",padx=50,pady=40)
        def si():
            pl=Label(dFrame,text="PENDING",bg="orange",fg="white",
                 font=("times new roman",15,"bold")).place(x=650-220,y=150)
           
        if f=="SICK":
            
            Label(dFrame,text=2-dur,bg="white",fg="black",
                 font=("times new roman",15,"bold")).place(x=270,y=150)
            
            Label(dFrame,text=6,bg="white",fg="black",
                 font=("times new roman",15,"bold")).place(x=270,y=220)
            Label(dFrame,text=5,bg="white",fg="black",
                 font=("times new roman",15,"bold")).place(x=270,y=300)
            si()
           
        elif f=="CASUAL":
            Label(dFrame,text=2,bg="white",fg="black",
                 font=("times new roman",15,"bold")).place(x=270,y=150)
            Label(dFrame,text=6-dur,bg="white",fg="black",
                 font=("times new roman",15,"bold")).place(x=270,y=220)
            p2=Label(dFrame,text="PENDING",bg="orange",fg="white",
                 font=("times new roman",15,"bold")).place(x=650-220,y=220)
            
            Label(dFrame,text=5,bg="white",fg="black",
                 font=("times new roman",15,"bold")).place(x=270,y=300)
           
        elif f=="EMERGENCY":
            Label(dFrame,text=2,bg="white",fg="black",
                 font=("times new roman",15,"bold")).place(x=270,y=150)
            Label(dFrame,text=6,bg="white",fg="black",
                 font=("times new roman",15,"bold")).place(x=270,y=220)
            Label(dFrame,text=5-dur,bg="white",fg="black",
                 font=("times new roman",15,"bold")).place(x=270,y=300)
            p3=Label(dFrame,text="PENDING",bg="orange",fg="white",
                 font=("times new roman",15,"bold")).place(x=650-220,y=300)
            
            def addlog():
                add=tkinter.Tk()
                add.geometry("600x400")
                add.config(bg="green")
                add.title("Admin Login")
                rej=tk.Button(add,relief=FLAT,text="rejection",bg="green",
                              fg="black",command=p3,font=("times new roman",
                                               15,"bold")).place(x=120,y=100)
                
                
        Label(dFrame,text="TYPE",bg="white",fg="black",
              font=("times new roman",15,"bold")).place(x=0,y=80)
        Label(dFrame,text="DAYS",bg="white",fg="black",
              font=("times new roman",15,"bold")).place(x=260,y=80)
        
        Label(dFrame,text="STATUS",bg="white",fg="black",
              font=("times new roman",15,"bold")).place(x=650-220,y=80)
        
        
        Label(dFrame,text="____________________________________________________________________________________",
              bg="white",fg="black",
              font=("times new roman",15,"bold")).place(x=0,y=110)
        Label(dFrame,text="SICK",bg="white",fg="black",
              font=("times new roman",15,"bold")).place(x=0,y=150)
                    
        Label(dFrame,text="____________________________________________________________________________________",
              bg="white",fg="black",
              font=("times new roman",15,"bold")).place(x=0,y=180)
        Label(dFrame,text="CASUAL",bg="white",fg="black",
              font=("times new roman",15,"bold")).place(x=0,y=220)
        
        Label(dFrame,text="____________________________________________________________________________________",
             bg="white",fg="black",
             font=("times new roman",15,"bold")).place(x=0,y=260)
        Label(dFrame,text="EMERGENCY",bg="white",fg="black",
              font=("times new roman",15,"bold")).place(x=0,y=300)
       
        leav=tk.Button(dFrame,relief=FLAT,text="BACK",bg="#c20000",
                      fg="white",command=dFrame.destroy,font=("times new roman",
                                       15,"bold")).place(x=400,y=450)
        leav=tk.Button(dFrame,relief=FLAT,text="Admin Login",bg="#c20000",
                      fg="white",command=addlog,font=("times new roman",
                                       15,"bold")).place(x=720,y=1)
    def detail():
        
        detFrame=Frame(FFrame,bg="white",highlightbackground="black",
                     highlightthickness=4)
        detFrame.pack(fill="both",expand="yes",padx=40,pady=20)
        
        
        sql_statement="SELECT leave_start_date,leave_end_date,type_of_leave,reasons FROM empoyee_leave_management"
        my_database.execute(sql_statement)
        output=my_database.fetchall()
        print(output[0])
        a=output[0]
        b=a[0]
        print(output[0])
        c=output[0]
        d=c[1] 
        print(output[0])
        e=output[0]
        f=e[2]
        print(output[0])
        g=output[0]
        h=g[3]
        sdate=(b)
        a=(sdate[0:2])
        a=int(a)
        print(a)
        ddate=(d)
        s=(ddate[0:2])
        s=int(s)
        print(s)
        dur=s-a
        print(dur)
        
                
        Label(detFrame,text="Employee's Name",bg="white",fg="red",font=("times new roman",15,"bold")).place(x=10,y=60)
        Label(detFrame,text="Start Date",bg="white",fg="red",font=("times new roman",15,"bold")).place(x=10,y=150)
        Label(detFrame,text="End Date",bg="white",fg="red",font=("times new roman",15,"bold")).place(x=10,y=240)
        Label(detFrame,text="Type of leave",bg="white",fg="red",font=("times new roman",15,"bold")).place(x=10,y=330)
        Label(detFrame,text="Reasons",bg="white",fg="red",font=("times new roman",15,"bold")).place(x=10,y=330+90+90)
        Label(detFrame,text="Leave duration",bg="white",fg="red",
              font=("times new roman",15,"bold")).place(x=10,y=330+90)     
        Label(detFrame,text=name,bg="white",fg="black",font=("times new roman",15,"bold")).place(x=10,y=60+30)
        Label(detFrame,text=b,bg="white",fg="black",font=("times new roman",15,"bold")).place(x=10,y=150+30)
        Label(detFrame,text=d,bg="white",fg="black",font=("times new roman",15,"bold")).place(x=10,y=240+30)
        Label(detFrame,text=f,bg="white",fg="black",font=("times new roman",15,"bold")).place(x=10,y=330+30)
        Label(detFrame,text=h,bg="white",fg="black",font=("times new roman",15,"bold")).place(x=10,y=330+90+30+90)
        Label(detFrame,text=dur,bg="white",fg="black",font=("times new roman",15,"bold")).place(x=10,y=330+90+30)
        leavs=tk.Button(detFrame,relief=FLAT,text="X",bg="white",
                      fg="red",command=detFrame.destroy,font=("times new roman",
                                       20,"bold")).place(x=810,y=0)
               
    def lapply():
                
        lFrame=Frame(FFrame,bg="skyblue",highlightbackground="black",
                     highlightthickness=4)
        lFrame.pack(fill="both",expand="yes",padx=20,pady=20)
        Label(lFrame,text="Apply For Leave",bg="skyblue",fg="black",
              font=("times new roman",20,"bold")).place(x=400,y=0)
        
        Label(lFrame,text="Start Date*",bg="skyblue",fg="black",
              font=("times new roman",15,"bold")).place(x=0,y=70)
        scal=DateEntry(lFrame,width=20,date_pattern="dd-mm-yyyy",background='blue',foreground="red")
        scal.place(x=0,y=110)
        Label(lFrame,text="End Date*",bg="skyblue",fg="black",
              font=("times new roman",15,"bold")).place(x=0,y=180)
        ecal=DateEntry(lFrame,width=20,background='blue',date_pattern="dd-mm-yyyy",foreground="red")
        ecal.place(x=0,y=220)
        sdate=(scal.get())
        sdate=(sdate)
        a=(sdate)
        edate=(ecal.get())

        Label(lFrame,text="Leavetype*",bg="skyblue",fg="black",
              font=("times new roman",15,"bold")).place(x=0,y=290)
       # combobox        
        fb1=ttk.Combobox(lFrame,width=28,state="readonly")
        fb1['values']=("SICK","CASUAL",'EMERGENCY')
        fb1.place(x=0,y=320)
        Label(lFrame,text="Reason",bg="skyblue",fg="black",
              font=("times new roman",15,"bold")).place(x=0,y=350)
        rc=Entry(lFrame)
        rc.place(x=0,y=380,width=400,height=80)
        
        def store():  
                                 
            sql_statement="INSERT INTO empoyee_leave_management (leave_start_date,leave_end_date,type_of_leave,reasons) values (%s,%s,%s,%s)"
            values=(scal.get(),ecal.get(),fb1.get(),rc.get())
            my_database.execute(sql_statement,values)
            db_connection.commit()  
            sql_statement="SELECT leave_start_date,leave_end_date,type_of_leave,reasons FROM empoyee_leave_management"
            my_database.execute(sql_statement)
            output=my_database.fetchall()
            print(output[0])
            a=output[0]
            b=a[0]
            print(output[0])
            c=output[0]
            d=c[1] 
            print(output[0])
            e=output[0]
            f=e[2]
            print(output[0])
            g=output[0]
            h=g[3]
            sdate=(b)
            a=(sdate[0:2])
            a=int(a)
            print(a)
            ddate=(d)
            s=(ddate[0:2])
            s=int(s)
            print(s)
            dur=s-a
            print(dur)
            print(f)
        
        lea=tk.Button(lFrame,relief=FLAT,text="X",command=lFrame.destroy,
                      bg="skyblue",
                      fg="red",font=("times new roman",
                                       20,"bold")).place(x=850,y=0)
        
        lea=tk.Button(lFrame,relief=FLAT,text="APPLY",command=store, 
                      bg="skyblue",
                      fg="green",font=("times new roman",15,"bold")).place(x=370,y=510)
        
        
    lea=tk.Button(rt,relief=FLAT,text="APPLY FOR LEAVE",command=lapply,
                  bg="#342D7E",
                  fg="white",font=("times new roman",
                                   15,"bold")).place(x=0,y=200)
    leav=tk.Button(rt,relief=FLAT,text="DASHBOARD",bg="#342D7E",
                  fg="white",command=dashboard,font=("times new roman",
                                   15,"bold")).place(x=0,y=150)
    leav=tk.Button(rt,relief=FLAT,text="VIEW DETAILS",bg="#342D7E",
                  fg="white",command=detail,font=("times new roman",
                                   15,"bold")).place(x=0,y=250)
        
    Label(rt,text="LEAVE MANAGEMENT",bg="#342D7E",fg="black",
          font=("times new roman",25,"bold")).place(x=0,y=10)
    

def logs():
    rot=tkinter.Tk()
    rot.geometry("1366x768")
    rot.config(bg="#52527a")
    Label(rot,text="UTC",bg="#52527a",fg="white",
          font=("times new roman",30,"underline")).place(x=680,y=10)
    FFrame=LabelFrame(rot,highlightbackground="black",highlightthickness=4,
                      bg="#a3a3c2",text="login",
                      font=("times new roman",10,"bold"))
    FFrame.pack(fill="both",expand="yes",padx=200,pady=100)
    Label(FFrame,text="UserName",bg="#a3a3c2",fg="black",
          font=("times new roman",25,"bold")).place(x=300,y=100)
    Label(FFrame,text="Id Number",bg="#a3a3c2",fg="black",
          font=("times new roman",25,"bold")).place(x=300,y=200)
    
    #entry
    fc=Entry(FFrame)
    fc.place(x=470,y=110,width=190,height=30)
    fc1=Entry(FFrame)
    fc1.place(x=470,y=210,width=190,height=30)
    print(name)
    def log():
        if fc.get()=="dhana" and fc1.get()=="12345":
            
            messagebox.showinfo("Login","Login Succesfully") and  bg()            
        else:
            messagebox.showinfo("showerror","check id or name")
        

    log=tk.Button(FFrame,relief=FLAT,command=log,text="LOGIN",bg="#a3a3c2",
                  fg="black",font=("times new roman",
                                   25,"underline")).place(x=440,y=300)
#_________________________________________main window_________________________________________________________
root=tkinter.Tk()
root.geometry("1366x768")
root.config(bg="#2d2d86")
Label(root,text="UTC",bg="#2d2d86",fg="white",font=("times new roman",50,"underline")).place(x=650,y=10)
MFrame=LabelFrame(root,bg="#b3b3e6",highlightbackground="black",highlightthickness=4)
MFrame.pack(fill="both",expand="yes",padx=350,pady=200)
opt2=tk.Button(MFrame,relief=FLAT,command=logs,text="Employee Login",bg="#b3b3e6",
                  fg="black",font=("times new roman",
                                   24,"bold")).place(x=200,y=150)
root.mainloop()

