import tkinter


def convert():
    value = input_.get()
    km = 1.609343 * float(value)
    value_label.config(text=str(km))


window = tkinter.Tk()
window.title("My first GUI program")
window.config(padx=20, pady=20)

equal_label = tkinter.Label(text="is equal to")
equal_label.grid(row=1, column=0)

value_label = tkinter.Label(text="0")
value_label.grid(row=1, column=1)

miles_label = tkinter.Label(text="Miles")
miles_label.grid(row=0, column=2)

km_label = tkinter.Label(text="Km")
km_label.grid(row=1, column=2)

button = tkinter.Button(text="Calculate", command=convert)
button.grid(row=2, column=1)

input_ = tkinter.Entry(width=20)
input_.grid(row=0, column=1)



window.mainloop()
