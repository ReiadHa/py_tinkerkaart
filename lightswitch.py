import tkinter as tk
window = tk.Tk()


button = tk.Button(text='Hello World', bg="black", fg="white")
button.pack(pady = 200, padx = 200)

# schijf hier tussen je code
getal = 0
def functie():
    global button,getal
    if getal == 0:
        print('test1')
        window.config(bg='red')
        button = tk.Button(text='Hello World', bg="black", fg="white")
        getal += 1
    elif getal == 1:        
        print('test2')
        window.config(bg='green')
        button = tk.Button(text='Hello World', bg="white", fg="black")
        getal -= 1
button.config(command=functie)
# schijf hier tussen je code

window.mainloop()
