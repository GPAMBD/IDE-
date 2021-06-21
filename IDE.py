from tkinter import *
from tkinter import ttk
import functools
from tkinter import scrolledtext
from tkinter import PhotoImage
from tkinter import filedialog
import os
import subprocess
from tkinter import messagebox
import time


# all header file related function for c
def addheader(event, userfile):
    file = '#include<' + userfile.get() + '.h>\n'
    code.insert(INSERT, file)
    save.configure(fg='white')


def stdiofile(event):
    code.insert(INSERT, '#include<stdio.h>\n')
    save.configure(fg='white')


def coniofile(event):
    code.insert(INSERT, '#include<conio.h>\n')
    save.configure(fg='white')


def globalfile(event):
    code.insert(INSERT, '#include<bits/c++.h>\n')
    save.configure(fg='white')


# all function realted function
def mainfunc(event):
    a = '''void main(){
            //write your code here
    }\n'''
    code.insert(INSERT, a)
    save.configure(fg='white')


def addfunction(event, data):
    a = "void" + data + "(){\n   //code here\n}\n"
    code.insert(INSERT, a)
    save.configure(fg='white')


# all input output function reated to C
def printfunc(event):
    a = 'printf("  statement  ", variable );\n'
    code.insert(INSERT, a)
    save.configure(fg='white')


def scanfunc(event):
    a = 'scanf(" %(modifier) ", & variable);\n'
    code.insert(INSERT, a)
    save.configure(fg='white')


# all condition related functions
def iffunction(event):
    a = 'if(condition){\n\n}\n'
    code.insert(INSERT, a)
    save.configure(fg='white')


def elsefunction(event):
    a = 'else {\n  \n}\n'
    code.insert(INSERT, a)
    save.configure(fg='white')


def ifelsefunction(event):
    a = 'if(condition){\n\n}\nelse{\n\n}\n'
    code.insert(INSERT, a)
    save.configure(fg='white')


def ifelseladder(event):
    a = '''if(condition){

        }
        else if(condition){

        }
        else{

        }\n'''
    code.insert(INSERT, a)
    save.configure(fg='white')


# all looping realated fucntion
def forloopfunc(event):
    a = '''for(initialize;condition;increment/decrement)
    {

    }\n'''
    code.insert(INSERT, a)
    save.configure(fg='white')


def whileloopfunc(event):
    a = '''while(condition)
    {

        //increment/decrement
    }\n'''
    code.insert(INSERT, a)
    save.configure(fg='white')


def dowhileloopfunc(event):
    a = '''do{


    }while(condition);\n'''
    code.insert(INSERT, a)
    save.configure(fg='white')


# looping function
def looping(event):
    b = Text(base, width=60, height=15, bg='grey', state='disable')
    b.place(y=500, x=0)
    forloop = Label(base, text='For loop', bg='light yellow', font=('arial bold', 15))
    forloop.place(y=520, x=20)
    forloop.bind("<Button>", forloopfunc)
    whileloop = Label(base, text='While loop', bg='light yellow', font=('arial bold', 15))
    whileloop.place(y=560, x=20)
    whileloop.bind("<Button>", whileloopfunc)
    dowhileloop = Label(base, text='Do-while loop', bg='light yellow', font=('arial bold', 15))
    dowhileloop.place(y=600, x=20)
    dowhileloop.bind("<Button>", dowhileloopfunc)
    save.configure(fg='white')


# condtion statement
def condition_statement(event):
    b = Text(base, width=60, height=15, bg='grey', state='disable')
    b.place(y=500, x=0)
    ifs = Label(base, text='if', bg='light yellow', font=('arial bold', 15))
    ifs.place(y=520, x=20)
    ifs.bind("<Button>", iffunction)
    elses = Label(base, text='else', bg='light yellow', font=('arial bold', 15))
    elses.place(y=560, x=20)
    elses.bind("<Button>", elsefunction)
    ifelses = Label(base, text='if-else', bg='light yellow', font=('arial bold', 15))
    ifelses.place(y=600, x=20)
    ifelses.bind("<Button>", ifelsefunction)
    isls = Label(base, text='if- else ladder', bg='light yellow', font=('arial bold', 15))
    isls.place(y=640, x=20)
    isls.bind("<Button>", ifelseladder)
    save.configure(fg='white')


# input and output statement for C
def input_output(event):
    b = Text(base, width=60, height=15, bg='grey', state='disable')
    b.place(y=500, x=0)
    printf = Label(base, text='Printf', bg='light yellow', font=('arial bold', 15))
    printf.place(y=520, x=20)
    printf.bind('<Button>', printfunc)
    scanf = Label(base, text='Scanf', bg='light yellow', font=('arial bold', 15))
    scanf.place(y=560, x=20)
    scanf.bind('<Button>', scanfunc)

    save.configure(fg='white')


# function for function for c ,c++
def function(event):
    # for the base of the menu
    b = Text(base, width=60, height=15, bg='grey', state='disable')
    b.place(y=500, x=0)
    # menu startes
    main = Label(base, text='Main', bg='light yellow', font=('arial bold', 15))
    main.place(y=510, x=20)
    main.bind('<Button>', mainfunc)
    funcl = Label(base, text='function name :', bg='white', font=('arial bold', 10))
    funcl.place(y=550, x=20)
    fun = Entry(base, width=20, font=('arial', 15))
    fun.place(y=550, x=150)
    addfunc = Button(base, text='ADD', font=('arial bold', 15), bg='black', fg='light green')
    addfunc.place(y=580, x=50)
    addfunc.bind('<Button>', functools.partial(addfunction, data=fun.get()))

    save.configure(fg='white')


# headerfile function for c
def headerfunction(event):
    b = Text(base, width=60, height=15, bg='grey', state='disable')
    b.place(y=500, x=0)
    bit = Label(base, text='Global Header File', bg='light yellow', fg='black', font=('arial bold', 15))
    bit.place(y=510, x=20)
    bit.bind('<Button>', globalfile)
    stdio = Label(base, text='stdio.h', bg='light yellow', fg='black', font=('arial bold', 15))
    stdio.place(y=510, x=220)
    stdio.bind('<Button>', stdiofile)
    conio = Label(base, text='conio.h', bg='light yellow', fg='black', font=('arial bold', 15))
    conio.place(y=510, x=300)
    conio.bind('<Button>', coniofile)
    userfilel = Label(base, text='File name :', bg='white', font=('arial bold', 10))
    userfilel.place(y=560, x=20)
    userfile = Entry(base, font=('arial', 15))
    userfile.place(y=560, x=100)
    add = Button(base, text='ADD', font=('arial bold', 15), bg='black', fg='light green')
    add.bind("<Button>", functools.partial(addheader, userfile=userfile))
    add.place(y=610, x=80)
    save.configure(fg='white')


# for the selected language
def method(event):
    getfile()
    code.configure(state='normal')
    c = language.get()
    save.configure(fg='white')

    if c == '-select-':  # if no language selected
        menu.configure(image=img1)
        code.configure(state='disable')

    elif c == 'C':  # if C is selected
        # for c ,this is the menu..
        header = Label(base, text='Header file', width=25, bg='black', fg='white', font=('arial bold', 20))
        header.place(y=80, x=20)
        header.bind('<Button>', headerfunction)
        func = Label(base, text='Function', width=25, bg='black', fg='white', font=('arial bold', 20))
        func.place(y=130, x=20)
        func.bind('<Button>', function)
        inout = Label(base, text='Input / Output', width=25, bg='black', fg='white', font=('arial bold', 20))
        inout.place(y=190, x=20)
        inout.bind('<Button>', input_output)
        condition = Label(base, text='Condition Statement', width=25, bg='black', fg='white', font=('arial bold', 20))
        condition.place(y=240, x=20)
        condition.bind('<Button>', condition_statement)
        loop = Label(base, text='Looping Statement', width=25, bg='black', fg='white', font=('arial bold', 20))
        loop.place(y=290, x=20)
        save.configure(fg='white')
        loop.bind('<Button>', looping)
        menu.place(y=340, x=170)



file = None


def compilecode(event):
    '''     if language.get()=='C':
             flag=1
             try:
                 fout=open(file.get(),'w')
             except:
                 flag=2
                 messagebox.showerror('NOT FOUND',"Can't Compile the file..\n(hint:give proper extension.!")
             if flag==1:
                 fout.write(code.get(0.0,END))
                 fout.close()
                 try:
                     subprocess.call(["gcc",file.get()])
                 except:
                     messagebox.showerror("Compiler Error","Compilation Error..!")
                     return None
                 run.bind('<Button>',functools.partial(runcode,file=file.get()))
                 run.configure(fg='light green')
                 b.destroy()
 '''
    try:
        subprocess.call(["gcc", cfile])
        run.configure(fg='light green')
        run.bind('<Button>', runcode)
    except :
        messagebox.showerror("Compiler error",
                             "Compilation Went Wrong..!!\n(hint:check the file type or directory..!!)")

cfile = None


def getfile():
    b = Toplevel()
    b.geometry('400x300')
    l = Label(b, text="File name:", bg='white', font=('arial bold', 15))
    l.place(y=20, x=30)
    file = Entry(b, font=('arial bold', 15))
    file.place(y=20, x=150)

    def openfile():
        f = filedialog.askopenfile()
        global cfile
        cfile = f.name
        code.insert(0.0, f.read())
        b.destroy()
        data=cfile.split('/')

        filename = Label(base, text=f"Running : {data[len(data)-1]} ",bg='black',fg='white',font=('arial bold',15))
        filename.place(y=750,x=25)

    open = Button(b, text='Open', command=openfile, fg='light green', bg='black', font=('arial bold', 15))
    open.place(y=80, x=200)

    def sub():
        global cfile
        cfile = file.get()
        b.destroy()

        data=cfile.split('/')
        filename = Label(base, text=f"Running : {data[len(data)-1]} ",bg='black',fg='white',font=('arial bold',15))
        filename.place(y=300,x=20)


    submit = Button(b, text='Submit', bg='black', command=sub, fg='light green', font=('arial bold', 15))
    submit.place(y=80, x=80)


def runcode(event):
    sub = subprocess.Popen("a.exe", shell=True, stdout=subprocess.PIPE)
    result = sub.stdout.read()
    l = Text(base, font=('arial bold', 20), bg='black', fg='red')
    l.insert(0.0, '---OUTPUT----\n\n')
    l.insert(INSERT, str(result))
    l.configure(state='disable')
    l.place(y=600, x=500)


def savefile(event):
    fout = open(cfile, 'w')
    fout.write(code.get(0.0, END))
    fout.close()
    save.configure(fg='red')


base = Tk()
base.configure(bg='black')
base.geometry("1500x800")
base.title("IDE -by AmeyCorporates")
img = PhotoImage(file="coding.png")
nav = Label(base, bg='black', width=250, font=('arial', 40))
nav.place(y=0, x=0)
imgn = Label(base, image=img, bg='black')
imgn.place(y=10, x=20)
code = ['-select-', 'C', 'C++']
language = ttk.Combobox(nav, value=code, state='readonly')
language.place(y=30, x=400)
language.current(0)
save = Label(nav, text='Save', bg='black', fg='white', font=('arial bold', 15))
save.place(y=25, x=570)
save.bind('<Button>', savefile)
dlog = Label(nav, text='EAT-SLEEP-CODE-REPEAT', bg='black', fg='light green', font=('arial bold', 15))
dlog.place(y=10, x=700)
compiler = Label(nav, text='Compile', bg='black', fg='white', font=('arial bold', 15))
compiler.place(y=15, x=1300)
compiler.bind('<Button>', compilecode)
run = Label(nav, text='Run', bg='black', fg='dark green', font=('arial bold', 15))
run.place(y=15, x=1420)

img1 = PhotoImage(file='gamer1.png')

menu = Label(base, image=img1)
menu.place(y=250, x=200)
code = scrolledtext.ScrolledText(base, wrap=WORD,bg='grey', height=22, width=65, font=('arial bold', 20))
code.place(y=70, x=500)
code.configure(state=DISABLED)

language.bind('<<ComboboxSelected>>', method)

base.mainloop()