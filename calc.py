from tkinter import *

root = Tk()

root.title('Calculator')
root.geometry('400x400')
e = Entry(root)
e.pack()
fr = Frame(root)
fr.pack(pady=10)

btn_list = [
    '7', '8', '9', '/', 'C',
    '4', '5', '6', '*', '%',
    '1', '2', '3', '-', '+',
    '0', '.', '='
]

row = 0
col = 0

for i in btn_list:
    if i == '=':
        Button(fr, text=i, padx=20, pady=10).grid(row=row, column=col, columnspan=3, sticky=W + E)
    else:
        Button(fr, text=i, padx=20, pady=10).grid(row=row, column=col)
    col += 1
    if col == 5:
        col = 0
        row += 1

root.mainloop()
