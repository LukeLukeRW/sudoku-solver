import tkinter 

root = tkinter.Tk()

for i in range(9):
    for j in range(9):
        entry = tkinter.Entry(root, width=5, justify='center')
        entry.grid(row=j,column=i,padx=2,pady=2)
root.mainloop()
