import tkinter as tk
from form import Auth

root = tk.Tk()
root.title("VK Download Music by Dimer")
'''w = root.winfo_screenwidth()
h = root.winfo_screenheight()'''
root["bg"] = "#fcfff0"
root.geometry("800x600")
mainmenu = tk.Menu(root) 
root.config(menu=mainmenu) 
"""
filemenu = tk.Menu(mainmenu, tearoff=0)
filemenu.add_command(label="Открыть...")
filemenu.add_command(label="Новый")
filemenu.add_command(label="Сохранить...")
filemenu.add_command(label="Выход")
 
helpmenu = tk.Menu(mainmenu, tearoff=0)
helpmenu.add_command(label="Помощь")
helpmenu.add_command(label="О программе")
 
mainmenu.add_cascade(label="Файл", menu=filemenu)
mainmenu.add_cascade(label="Справка", menu=helpmenu)
"""
user_Auth = Auth(root)
root.mainloop()
