import tkinter
import tkinter.font
import tkinter.ttk
import datetime


class BIODATA:
    def __init__(this):
        this.__window = tkinter.Tk(None, None,"Just a random biodata software") 
        this.__window.geometry("800x600")
        this.__window.maxsize(800,600)
        this.__window.minsize(800,600)

        this.__PersonalData = {}
        this.__fontHeader = tkinter.font.Font(family="Segoe UI", size="24",weight="bold")
        this.__fontLabel = tkinter.font.Font(family="Segoe UI", size="14",weight="bold")
        this.__fontNormal = tkinter.font.Font(family="Segoe UI", size="12",weight="normal")

    def __HandleInputs(this,var,key):
        try:
            datetime.datetime.strptime(var.get(),"%d/%m/%Y")
            this.__PersonalData[key].config(bg="#27293D",fg="#BEBFC5")

        except ValueError:
            this.__PersonalData[key].config(bg="#F00",fg="#000")

    def DrawWindowHeader(this):
        tkinter.Label(this.__window,text="BIODATA",font=this.__fontHeader).place(x = 0, y = 0,width=800)

    def DrawPersonalDataFrame(this):
        this.__DropDownBtn = tkinter.Button(this.__window,text="PERSONAL DATA",anchor="w", font=this.__fontLabel,bg="#27293D",activebackground="#313347",fg="#BEBFC5",width=800)
        this.__DropDownBtn.place(x=-1,y=70)
        this.__personalDataFrame = tkinter.Frame(this.__window,bg="#1E1E2B")
        this.__personalDataFrame.place(x=0,y=114,width=800,height=100)

        tkinter.Label(this.__personalDataFrame,text="Position Desired: ", font=this.__fontNormal,bg="#1E1E2B",fg="#BEBFC5").place(x=0,y=0)
        this.__PersonalData["desiredPos"] = tkinter.Entry(this.__personalDataFrame, font=this.__fontNormal)
        this.__PersonalData["desiredPos"].config(highlightthickness=1, highlightcolor="#D74DC3", highlightbackground="#D74DC3", borderwidth=1,bg="#1E1E2B",fg="#BEBFC5")
        this.__PersonalData["desiredPos"].place(x=150,width=300)


        tkinter.Label(this.__personalDataFrame,text="Date (DD/MM/YYYY): ", font=this.__fontNormal,bg="#1E1E2B",fg="#BEBFC5").place(x=500,y=0)
        this.__dateValue = tkinter.StringVar()
        this.__dateValue.trace('w', lambda *_, var=this.__dateValue: this.__HandleInputs(var,"date"))
        this.__PersonalData["date"] = tkinter.Entry(this.__personalDataFrame, text="12/12/2012", font=this.__fontNormal,textvariable=this.__dateValue)
        this.__PersonalData["date"].config(highlightthickness=1, highlightcolor="#D74DC3", highlightbackground="#D74DC3", borderwidth=1,bg="#1E1E2B",fg="#BEBFC5")
        this.__PersonalData["date"].place(x=670,width=120)

        tkinter.Label(this.__personalDataFrame,text="Name: ", font=this.__fontNormal,bg="#1E1E2B",fg="#BEBFC5").place(x=0,y=0)
        this.__PersonalData["name"] = tkinter.Entry(this.__personalDataFrame, font=this.__fontNormal)
        this.__PersonalData["name"].config(highlightthickness=1, highlightcolor="#D74DC3", highlightbackground="#D74DC3", borderwidth=1,bg="#1E1E2B",fg="#BEBFC5")
        this.__PersonalData["name"].place(x=150,width=300)

        tkinter.Label(this.__personalDataFrame,text="City Address: ", font=this.__fontNormal,bg="#1E1E2B",fg="#BEBFC5").place(x=0,y=0)
        this.__PersonalData["cityAddress"] = tkinter.Entry(this.__personalDataFrame, font=this.__fontNormal)
        this.__PersonalData["cityAddress"].config(highlightthickness=1, highlightcolor="#D74DC3", highlightbackground="#D74DC3", borderwidth=1,bg="#1E1E2B",fg="#BEBFC5")
        this.__PersonalData["cityAddress"].place(x=150,width=300)

        tkinter.Label(this.__personalDataFrame,text="Provincial Address: ", font=this.__fontNormal,bg="#1E1E2B",fg="#BEBFC5").place(x=0,y=0)
        this.__PersonalData["provAddress"] = tkinter.Entry(this.__personalDataFrame, font=this.__fontNormal)
        this.__PersonalData["provAddress"].config(highlightthickness=1, highlightcolor="#D74DC3", highlightbackground="#D74DC3", borderwidth=1,bg="#1E1E2B",fg="#BEBFC5")
        this.__PersonalData["provAddress"].place(x=150,width=300)

        tkinter.Label(this.__personalDataFrame,text="Telephone: ", font=this.__fontNormal,bg="#1E1E2B",fg="#BEBFC5").place(x=0,y=0)
        this.__PersonalData["telephone"] = tkinter.Entry(this.__personalDataFrame, font=this.__fontNormal)
        this.__PersonalData["telephone"].config(highlightthickness=1, highlightcolor="#D74DC3", highlightbackground="#D74DC3", borderwidth=1,bg="#1E1E2B",fg="#BEBFC5")
        this.__PersonalData["telephone"].place(x=150,width=300)

        tkinter.Label(this.__personalDataFrame,text="Email Address: ", font=this.__fontNormal,bg="#1E1E2B",fg="#BEBFC5").place(x=0,y=0)
        this.__PersonalData["email"] = tkinter.Entry(this.__personalDataFrame, font=this.__fontNormal)
        this.__PersonalData["email"].config(highlightthickness=1, highlightcolor="#D74DC3", highlightbackground="#D74DC3", borderwidth=1,bg="#1E1E2B",fg="#BEBFC5")
        this.__PersonalData["email"].place(x=150,width=300)

        

        tkinter.Label(this.__personalDataFrame,text="Date of Birth: ", font=this.__fontNormal,bg="#1E1E2B",fg="#BEBFC5").place(x=0,y=0)
        this.__dateValueBirth = tkinter.StringVar()
        this.__dateValueBirth.trace('w', lambda *_, var=this.__dateValueBirth: this.__HandleInputs(var,"dateBirth"))
        this.__PersonalData["dateBirth"] = tkinter.Entry(this.__personalDataFrame, text="12/12/2012", font=this.__fontNormal,textvariable=this.__dateValue)
        this.__PersonalData["dateBirth"].config(highlightthickness=1, highlightcolor="#D74DC3", highlightbackground="#D74DC3", borderwidth=1,bg="#1E1E2B",fg="#BEBFC5")
        this.__PersonalData["dateBirth"].place(x=670,width=120)

    def BeginPresentLoop(this):
        this.DrawWindowHeader()
        this.DrawPersonalDataFrame()
        while True:
            this.__window.update_idletasks()
            this.__window.update()


x = BIODATA()
x.BeginPresentLoop()