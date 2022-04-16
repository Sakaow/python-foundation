import tkinter as tk

def show_output():
    number = int(number_input.get())
    if number == 0:
        output_label.configure(text="Zero times any number is always 0!")
        return

    # calculate output using for loop
    output = ''
    for i in range(1, 13):
        output += str(number) + ' x ' + str(i)
        output += ' = ' + str(number * i) + '\n'

    # display the output on screen
    output_label.configure(text=output)


panel = tk.Tk()
panel.title('Multiplication')
panel.minsize(width=400, height=400)

title = tk.Label(master=panel, text='Multiplication table:')
title.pack(pady=20)     # vertical space 'y'

number_input = tk.Entry(master=panel, width=15)
number_input.pack()

go_button = tk.Button(
    master=panel,
    text='click',
    command=show_output, width=15, height=2
)
go_button.pack()

output_label = tk.Label(master=panel)
output_label.pack(pady=20)


panel.mainloop()