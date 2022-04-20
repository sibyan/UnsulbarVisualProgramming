import tkinter

main_window = tkinter.Tk()

def kalkulator():
    label2 = tkinter.Label(main_window, text='Masukan Bilangan')
    label2.pack()

label = tkinter.label(main_window, text='Hasilnya Adalah')
hasil = tkinter.Button(main_window, text='hasilnya', command = kalkulator)

label.pack()
hasil.pack()

main_window.mainloop()
