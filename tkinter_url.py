#!/usr/bin/python3

from tkinter import *
import bitly_api

class MyWindow:
	def __init__(self, win):
		self.lbl1 = Label (win, text= ' Enter the url to shorten')
		self.lbl3=Label(win, text='Result')
		self.t1=Entry()
		self.t3=Entry()
		self.btn1= Button(win, text='Go')
		self.lbl1.place(x=10, y=50)
		self.t1.place(x=200, y=50)
		self.b1=Button(win, text='Go', command=self.short)
		self.lbl3.place(x=10, y=200)
		self.t3.place(x=200, y=200, width=180)
		self.b1.place(x=200, y=150)

	def short(self):
		self.t3.delete(0, 'end')
		BITLY_ACCESS_TOKEN = "<Your access_token>"
		b = bitly_api.Connection(access_token = BITLY_ACCESS_TOKEN)
		response = b.shorten(self.t1.get())
		for key, value in response.items():
			if key.startswith('url'):
				f=key, value
		self.t3.insert (END, str(f))

window=Tk()
mywin=MyWindow(window)
window.title('Short Url Converter')
window.geometry("400x300+10+10")
window.mainloop()
