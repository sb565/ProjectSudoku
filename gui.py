from tkinter import *
import PIL.Image, PIL.ImageTk
import numpy as np
from tkinter import filedialog

window = Tk()

def exit_gui(screen):
	screen.destroy()


def open_file():
	path = filedialog.askopenfilename(title = "Select Image",filetypes = (("jpeg files","*.jpeg"),("all files","*.*")))
	return path


def get_values(reslist,R,window):
	for i in range(9):
		for j in range(9):
			val=reslist[i][j].get()
			if val=='':
				val='0'
			R[i][j]=int(val)
	window.destroy()


def correct_values(img, result):
	R=np.zeros((9,9),dtype=int)

	L1 = Label(window, text = "Sudoku Solver",justify=CENTER, font=('Times New Roman Bold',40))
	L1.grid(column=0,row=0,columnspan=10)

	L2 = Label(window, text = "Please verify the text recognised",justify=CENTER, font=('Times New Roman ',25))
	L2.grid(column=0,row=1,columnspan=10)

	height, width = img.shape
	canvas = Canvas(window, width = width, height = height)
	photo = PIL.ImageTk.PhotoImage(image = PIL.Image.fromarray(img))
	canvas.create_image(0, 0, image=photo, anchor=NW)
	canvas.grid(column=0,row=2,rowspan=9)

	rlist = []
	for i in range(9):
		rlist.append([])
		for j in range(9):
			c=j+1
			r=i+2
			tempentry = Entry(window,font=("Calibri Bold",12),justify="center",width=4)
			if(not result[i][j]==0):
				tempentry.insert(0, result[i][j])
			tempentry.grid(column=c,row=r,sticky=NSEW)

			rlist[i].append(tempentry)

	B1 = Button(window,text='Solve',font=('Bold'),command = lambda :get_values(rlist,R, window))
	B1.grid(column=0,row=11,columnspan=10)
	window.mainloop()

	return R

def solved():
	filepath = 'output.txt'
	rows = []
	with open(filepath) as fp:
		line = fp.readline()
		while line:
			row = np.array(line.split(' '))
			row = np.delete(row, -1)
			row = row.astype(int)
			rows.append(row)
			line = fp.readline()
	display(np.concatenate(rows))

def display(result):
	result.shape = (9,9)
	screen = Tk()
	screen.title("Project Sudoku")
	L1 = Label(screen, text = "Solution",justify=CENTER, font=('Times New Roman Bold',40))
	L1.grid(column=0,row=0,columnspan=9)

	rlist = []
	for i in range(9):
		rlist.append([])
		for j in range(9):
			c=j
			r=i+1
			tempentry = Label(screen,text=result[i][j] ,font=("Calibri Bold",12),justify="center",width=4).grid(column=c,row=r)
			rlist[i].append(tempentry)
	B1 = Button(screen,text='Exit',font=('Bold'),command = lambda :exit_gui(screen))
	B1.grid(column=0,row=10,columnspan=9)
	screen.mainloop()


def initialise_gui():
	window.title("Project Sudoku")
	#window.geometry('800x600')
