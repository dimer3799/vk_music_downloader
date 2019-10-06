import tkinter as tk

class Auth(tk.Frame):
	def __init__(self, master=None, service=None):
		super().__init__(master)
		self.service = service
		self.pack()
		self.render_form()
		
	def func(self):
		top = tk.Toplevel(self)
		top.geometry('400x200')
		top["bg"] = "#FFFFE0"

		lbl_l = tk.Label(top, text='Login')
		lbl_l.pack()
		login = tk.Entry(top, width=30, bg = '#FFF0F5', font = 'Liberation', justify = 'center')
		login.pack()

		lbl_password = tk.Label(top, text='Password')
		lbl_password.pack()
		password = tk.Entry(top, width=30, show='*', bg = '#FFF0F5', font = 'Liberation' , justify = 'center')
		password.pack()

		btn_level = tk.Button(top, text='Submit' ,command= top.quit)
		btn_level.pack()
		
		top.grab_set()
		top.focus_set()
		top.wait_window()


		#top.overrideredirect(True)
		label1 = Label(text="Hello Python", fg="#eee", bg="#333")
		label1.pack()
		top.pack()

		
	def render_form(self):
		form = tk.Frame(self)
		form.pack()
		btn_auth = tk.Button(form, text='Avtorizacia', command=lambda : self.func())
		btn_auth.pack(side=tk.RIGHT)

	
	def submit(top):
		top.window_bar.destroy()