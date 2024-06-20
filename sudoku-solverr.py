import tkinter
import time

def main(root):
    entries = []
    for i in range(9):
        row_entries = []
        for j in range(9):
            entry = tkinter.Entry(root, width=5, justify='center')
            entry.grid(row=j,column=i,padx=2,pady=2)
            row_entries.append(entry)
        entries.append(row_entries)


if __name__ == '__main__':
    root = tkinter.Tk()
    main(root)
    
    root.mainloop()
