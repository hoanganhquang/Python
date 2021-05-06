import tkinter

window = tkinter.Tk()
window.title("My first GUI program")
window.minsize(width=400, height=400)

my_label = tkinter.Label(text="New Text")
my_label.pack()

def change_text():
    a = input_.get()
    my_label.config(text=a)


button = tkinter.Button(text="click", command=change_text)
button.pack()

input_ = tkinter.Entry()
input_.pack()



window.mainloop()
