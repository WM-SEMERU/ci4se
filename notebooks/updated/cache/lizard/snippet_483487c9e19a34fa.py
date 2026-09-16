def GetRadioButtonSelect(selectList, title='Select', msg=''):
    root = tkinter.Tk()
    root.title(title)
    val = tkinter.IntVar()
    val.set(0)
    if msg != '':
        tkinter.Label(root, text=msg).pack()
    index = 0
    for item in selectList:
        tkinter.Radiobutton(root, text=item, variable=val, value=index).pack(
            anchor=tkinter.W)
        index += 1
    tkinter.Button(root, text='OK', fg='black', command=root.quit).pack()
    root.mainloop()
    root.destroy()
    print(selectList[val.get()] + ' is selected')
    return selectList[val.get()], val.get()