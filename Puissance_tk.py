import tkinter as tk

def power_of_two():
    number = int(entry.get())
    result = number ** 2
    result_label.config(text=f"Puissance {number} est : {result}")

root = tk.Tk()
root.title("App Puissance")
root.geometry("250x180")
root.resizable(False,False)

label= tk.Label(root,text="Entrez nombre ")
label.pack()
entry = tk.Entry(root, width=20)
entry.pack(pady=10)

calculate_button = tk.Button(root, text="Calculate", command=power_of_two)
calculate_button.pack()

result_label = tk.Label(root, text="")
result_label.pack(pady=10)

root.mainloop()

