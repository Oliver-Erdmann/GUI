from tkinter import *
from tkinter import messagebox

# tkinter name instance
root = Tk()

# setting the windows size
root.geometry("730x300")
root.configure(bg='gray')

# creating a label for
# name using widget label
box_1_label = Label(root, text='user-input-1', font=('calibre', 10, 'bold'))
# this places the label
box_1_label.grid(row=5, column=1)
box_2_label = Label(root, text='user-input-2', font=('calibre', 10, 'bold'))
box_2_label.grid(row=5, column=2)
box_3_label = Label(root, text='user-input-3', font=('calibre', 10, 'bold'))
box_3_label.grid(row=6, column=1)
box_4_label = Label(root, text='user-input-4', font=('calibre', 10, 'bold'))
box_4_label.grid(row=6, column=2)

# show warning thing for pop-up button
def pop_up1():
    messagebox.showwarning("showwarning", "don't press any buttons")
def pop_up2():
    messagebox.showwarning("showwarning", "stop pressing buttons")
def pop_up3():
    messagebox.showwarning("showwarning", "seriously, stop")
def pop_up4():
    messagebox.showwarning("showwarning", "why are you like this")
def pop_up5():
    messagebox.showwarning("showwarning", "i hate you")

# buttons
pop_up_btn = Button(root, text='pop-up 1', command=pop_up1)
pop_up_btn.grid(row=0, column=0)
pop_up_btn2 = Button(root, text='pop-up 2', command=pop_up2)
pop_up_btn2.grid(row=1, column=0)
pop_up_btn3 = Button(root, text='pop-up 3', command=pop_up3)
pop_up_btn3.grid(row=2, column=0)
pop_up_btn4 = Button(root, text='pop-up 4', command=pop_up4)
pop_up_btn4.grid(row=3, column=0)
pop_up_btn5 = Button(root, text='pop-up 5', command=pop_up5)
pop_up_btn5.grid(row=4, column=0)

# functions for radio buttons
def radio_1():
    print("radio 1")
def radio_2():
    print("radio 2")
def radio_3():
    print("radio 3")
def radio_4():
    print("radio 4")
def radio_5():
    print("radio 5")

# radio buttons
R1 = Radiobutton(root, text="option 1", value=0, command=radio_1)
R1.grid(row=0, column=1)
R2 = Radiobutton(root, text="option 2", value=1, command=radio_2)
R2.grid(row=1, column=1)
R3 = Radiobutton(root, text="option 3", value=2, command=radio_3)
R3.grid(row=2, column=1)
R4 = Radiobutton(root, text="option 4", value=3, command=radio_4)
R4.grid(row=3, column=1)
R5 = Radiobutton(root, text="option 5", value=4, command=radio_5)
R5.grid(row=4, column=1)

# access the menu widget using StringVar function
# dropdown menu
clicked = StringVar()
main_menu = OptionMenu(root, clicked, "C++", "Java", "Python", "Rust", "Go", "Ruby")
main_menu.grid(row=0, column=3)

# slider
slider_2 = Scale(root, from_=-200, to=200, orient=HORIZONTAL)
slider_2.grid(row=5, column=0)
slider_3 = Scale(root, from_=69, to=420, orient=HORIZONTAL)
slider_3.grid(row=6, column=0)

# spin box
spin_box_1 = Spinbox(root, from_=-10, to=10)
spin_box_1.grid(row=0, column=4)
def test_fun():
    print("test_fun")

# check box
check_box_1 = Checkbutton(root, text='yes', onvalue=1, offvalue=0, command=test_fun)
check_box_1.grid(row=0, column=2)
check_box_2 = Checkbutton(root, text='no', onvalue=1, offvalue=0, command=test_fun)
check_box_2.grid(row=1, column=2)
check_box_3 = Checkbutton(root, text='why', onvalue=1, offvalue=0, command=test_fun)
check_box_3.grid(row=2, column=2)
check_box_4 = Checkbutton(root, text='how', onvalue=1, offvalue=0, command=test_fun)
check_box_4.grid(row=3, column=2)

# text entry
entry_box_1 = Entry(root, font=('calibre', 10, 'normal'))
entry_box_1.grid(row=1, column=3)
entry_box_2 = Entry(root, font=('calibre', 10, 'normal'))
entry_box_2.grid(row=2, column=3)

# performing an infinite loop
# for the window to display
root.mainloop()