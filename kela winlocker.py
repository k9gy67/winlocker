import tkinter as tk

def check_input(event=None):
    user_input = entry.get().strip().lower()
    if user_input == "12345":  
        root.destroy()  
    else:
        status_label.config(text=f"Введено: {user_input}", fg="orange")

root = tk.Tk()
root.title("winlocker")
root.geometry("1980x1280")
root.attributes("-fullscreen", True)


label = tk.Label(root, text="windows заблокирован", font=("Arial", 12))
label.pack(pady=20)


entry_frame = tk.Frame(root)  
entry_frame.pack(pady=10)

tk.Label(entry_frame, text="Введите пароль для разблокировки", font=("Arial", 9)).pack()

entry = tk.Entry(entry_frame, width=25, font=("Arial", 10))
entry.pack(pady=5)
entry.bind("<Return>", check_input) 


button = tk.Button(entry_frame, text="подтвердить", command=check_input)
button.pack()


status_label = tk.Label(root, text="", font=("Arial", 9))
status_label.pack(pady=5)



root.mainloop()
