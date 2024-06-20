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

    return entries
    
def the_start(entries):
    def submit():
        sudoku_values = []
        for row in entries:
            row_values = []
            for entry in row:
                value = entry.get()
                row_values.append(value)
            sudoku_values.append(row_values)
            
        for i in sudoku_values:
            for j in range(len(i)):
                if i[j] == '':
                    i[j] = int(0)

    return submit


if __name__ == '__main__':
    root = tkinter.Tk()

    start_button = tkinter.Button(root,width=10,justify='right',text='Submit',command=the_start(main(root)))
    start_button.grid(row=10,column=10,padx=3,pady=3)


    root.mainloop()

