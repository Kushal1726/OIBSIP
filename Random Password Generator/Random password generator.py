from tkinter import *
from tkinter import messagebox
import random


Sp = ['@','$','#','&','%','!']
Number = [0,1,2,3,4,5,6,7,8,9]
Uppercase = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
Lowercase = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']


def password_generator():
	pg = Tk()
	pg.geometry("350x150")
	pg.title("Password-Generator")
	pg.resizable(1,0)
	def pass_gen():
		pass_entry_text = (" ")
		generated = (" ")
		choice_lst = []
		length = random.randint(6,8)
		for i in range(length+2):
			special = random.choice(Sp)
			no = random.choice(Number)
			non_special = random.choice(Uppercase)
			non_special2 = random.choice(Lowercase)
			choice_lst.append(special)
			choice_lst.append(no)
			choice_lst.append(non_special)
			choice_lst.append(non_special2)
			choice = random.choice(choice_lst)
			generated += str(choice)
		pass_entry.delete(0, END)
		pass_entry_text = generated
		pass_entry.insert(END, pass_entry_text)
		
	empty = Label(pg, text="        ")
	empty.pack()
	pass1 = Label(pg, text="GENERATE PASSWORD", font=('bold',20), fg="pink")
	pass1.pack()
	pass_entry = Entry(pg, textvariable=StringVar)
	pass_entry.pack()
	pass_btn = Button(pg, text="GENERATE", font=8, fg="black", bg="yellow", command=pass_gen)
	pass_btn.pack()
	pg.mainloop()

if __name__ == '__main__':
	password_generator()