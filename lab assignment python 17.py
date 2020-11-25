from tkinter import *
root = Tk()
root.geometry("655x333")
#-------frame1
f1 = Frame(root, bg = "white",borderwidth=2 ,relief =SUNKEN )
f1.pack(side = TOP ,fill="x")

l1 = Label(f1 , text ='''GUI using tkinter''', font="Helvetica 16 bold", fg="red", pady=12)
l1.pack(padx = 40)
#------frame2
f2 = Frame(root,bg = "grey" , borderwidth=4,relief=RAISED)
f2.pack(side=TOP , fill="x")

l2 = Label(f2 , text="Python Lab Assignment " ,bg="grey", font="Helvetica 16 bold", fg="white",pady = 24)
l2.pack(padx = 40)


def donothing():
   filewin = Toplevel(root)
   button = Button(filewin, text="Do nothing button")
   button.pack()
   

menubar = Menu(root)
filemenu = Menu(menubar, tearoff=0)
filemenu.add_command(label="New", command=donothing)
filemenu.add_command(label="Open", command=donothing)
filemenu.add_command(label="Save", command=donothing)
filemenu.add_command(label="Save as...", command=donothing)
filemenu.add_command(label="Close", command=donothing)

filemenu.add_separator()

filemenu.add_command(label="Exit", command=root.quit)
menubar.add_cascade(label="File", menu=filemenu)

homemenu = Menu(menubar, tearoff=0)
homemenu.add_command(label="cut",command=donothing)
homemenu.add_command(label="copy",command=donothing)
homemenu.add_command(label="paste",command=donothing)
menubar.add_cascade(label="Home" , menu = homemenu)


viewmenu = Menu(menubar, tearoff=0)
viewmenu.add_checkbutton(label = "items", onvalue = 1, offvalue = 0)
viewmenu.add_checkbutton(label = "items check boxes", onvalue = 1, offvalue = 0)
viewmenu.add_checkbutton(label = "items check boxes", onvalue = 1, offvalue = 0)
menubar.add_cascade(label="View" , menu = viewmenu)


editmenu = Menu(menubar, tearoff=0)
editmenu.add_command(label="Undo", command=donothing)

editmenu.add_separator()

editmenu.add_command(label="Cut", command=donothing)
editmenu.add_command(label="Copy", command=donothing)
editmenu.add_command(label="Paste", command=donothing)
editmenu.add_command(label="Delete", command=donothing)
editmenu.add_command(label="Select All", command=donothing)

menubar.add_cascade(label="Edit", menu=editmenu)
helpmenu = Menu(menubar, tearoff=0)
helpmenu.add_command(label="Help Index", command=donothing)
helpmenu.add_command(label="About...", command=donothing)
menubar.add_cascade(label="Help", menu=helpmenu)

root.config(menu=menubar)
#--------------------------------------------------------------------------
scrollbar = Scrollbar(root)
scrollbar.pack( side = LEFT, fill = Y )


mylist = Listbox(root, yscrollcommand = scrollbar.set )
for line in range(100):
   mylist.insert(END, "India.........." + str(line))

mylist.pack( side = LEFT, fill = BOTH )
scrollbar.config( command = mylist.yview )

#......frame3
f3 = Frame(root , bg = "lightblue" , borderwidth = 5 , relief = RIDGE)
f3.pack(side=RIGHT , fill = "y" )


l3 = Label(f3 , text="*" ,bg="lightblue", font="Helvetica 16 bold", fg="black",pady = 24,padx = 500)
l3.pack(padx = 40)

l4 = Label(f3 , text="*" ,bg="lightblue", font="Helvetica 16 bold", fg="black",pady = 24,padx = 500)
l4.pack(padx = 40)

l5 = Label(f3 , text="*" ,bg="lightblue", font="Helvetica 16 bold", fg="black",pady = 24,padx = 500)
l5.pack(padx = 40)

l3 = Label(f3 , text="*" ,bg="lightblue", font="Helvetica 16 bold", fg="black",pady = 24,padx = 500)
l3.pack(padx = 40)

l3 = Label(f3 , text="Punjab Technical University Mohali Campus - 1" ,bg="lightblue", font="Helvetica 30 bold", fg="black",pady = 24,padx = 500)
l3.pack(padx = 40)


l3 = Label(f3 , text="*" ,bg="lightblue", font="Helvetica 16 bold", fg="black",pady = 24,padx = 500)
l3.pack(padx = 40)

l3 = Label(f3 , text="*" ,bg="lightblue", font="Helvetica 16 bold", fg="black",pady = 24,padx = 500)
l3.pack(padx = 40)

l3 = Label(f3 , text="*" ,bg="lightblue", font="Helvetica 16 bold", fg="black",pady = 24,padx = 500)
l3.pack(padx = 40)



root.mainloop()


