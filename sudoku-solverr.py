def main(root,start):
    entries = []
    for i in range(9):
        row_entries = []
        for j in range(9):
            entry = tkinter.Entry(root, width=5, justify='center')
            entry.grid(row=j,column=i,padx=2,pady=2)
            row_entries.append(entry)
        entries.append(row_entries)

    if start is True:
        print(entries)
        return entries
    
def the_start(root):
    def returns():
        return 1
    start_button = tkinter.Button(root,width=10,justify='right',text='Submit',command=returns())
    start_button.grid(row=10,column=10,padx=3,pady=3)
    return returns

if __name__ == '__main__':
    root = tkinter.Tk()
    sudoku_entry = main(root,the_start(root))
    print(sudoku_entry)
    root.mainloop()
