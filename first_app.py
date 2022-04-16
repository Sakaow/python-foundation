import tkinter as tk

def set_message():
    message = text_input.get()
    title_lable.configure(text=message)

window = tk.Tk()
window.title('PythonApp')
window.minsize(width=400, height=400)

# display message
title_lable = tk.Label(master=window, text='Input something and click the button to replace me!')
title_lable.pack()

# input field
text_input = tk.Entry(master=window)
text_input.pack()

# button 
ok_button = tk.Button(master=window, text="OK", command=set_message)
ok_button.pack()

# display window
window.mainloop()