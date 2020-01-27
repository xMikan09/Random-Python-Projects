import tkinter

class TKINTER_TEST:
    clickCount = 0
    # Event Callbacks start here
    def BtnClickedEvent(this):
        this.clickCount += 1
        tempStr = "Button has been clicked {:d} times".format(this.clickCount)
        this.str.set(tempStr)
    # Event Callbacks end here

    def __init__(this):
        this.window = tkinter.Tk()
        this.window.geometry("300x200")
        this.str = tkinter.StringVar();
        this.str2 = tkinter.StringVar();
        this.str3 = tkinter.StringVar();


    def BtnExample(this):
        btn = tkinter.Button(this.window,text="Tkinter Button Example",command=this.BtnClickedEvent)
        btn.pack()
        label = tkinter.Label(this.window,textvariable=this.str)
        label.pack()


    def FrameExample(this):
        frame = tkinter.Frame(this.window)
        frame.pack()
        txt = tkinter.Text(frame);
        txt.insert(tkinter.INSERT,"Frame (and text) example")
        txt.config(state=tkinter.DISABLED)
        txt.pack()

    def EntryExample(this):
        ent = tkinter.Entry(this.window, textvariable=this.str2)
        ent.pack()
        label = tkinter.Label(this.window,textvariable=this.str2)
        label.pack()

    def RadioExample(this):
        values = {"Radiobtn_1":"Option 1 is selected","Radiobtn_2":"Option 2 is selected"}
        for (text, value) in values.items(): 
            tkinter.Radiobutton(this.window, text = text, variable = this.str3,  
                value = value, indicator = 0, 
                background = "light blue").pack(fill = tkinter.X, ipady = 5) 
        label = tkinter.Label(this.window,textvariable=this.str3)
        label.pack()

    def BeginDraw(this):
        this.BtnExample()
        this.EntryExample()
        this.RadioExample()
        this.FrameExample()
        this.window.mainloop()


x = TKINTER_TEST()
x.BeginDraw()