from tkinter import Frame, Button, Text, Entry, Label, Tk

class MyFrame(Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master;
        self.master.title = "Simple GUI"; # accidental change of master to string - should use master.title instead
        self.pack()
        self.quit_button()
        self.create_text_widget()
        self.create_user_form()

    def quit_button(self):
        self.quit_button = Button(self, text='QUIT', fg='red', command=self.master.destroy);
        self.quit_button.pack(pady=10)
    
    def create_text_widget(self):
        self.text = Text(self, height=10, width=30)
        self.text.pack(pady=10, padx=10, fill='both', expand=True)
        self.text.config(state='disable')

    def create_user_form(self):
        self.label = Label(self, text="Username:")
        self.label.pack(pady=10, padx=10);
        self.entry = Entry(self)
        self.entry.pack(pady=10, padx=10)
        self.entry.insert(0, "Enter username")
        self.entry.bind("<FocusIn>", self.on_entry_write)

        self.label2 = Label(self, text="Password")
        self.label2.pack(pady=10, padx=10)
        self.entry2 = Entry(self)
        self.entry2.pack(pady=10, padx=10)
        self.entry2.insert(0, "Enter password")
        self.entry2.bind("<FocusIn>", self.on_entry_write)

        self.submit_button = Button(self, text="Submit", command=self.on_submit)
        self.submit_button.pack(pady=10)

    def on_submit(self):
        username = self.entry.get()
        password = self.entry2.get()
        self.text.config(state="normal")
        self.text.insert("end",f"Username: {username}\nPassword: {password}\n")
        self.text.config(state="disabled")

        self.entry.delete(0, "end")
        self.entry.insert(0, "Enter username")
        self.entry.bind("<FocusIn>", self.on_entry_write)

        self.entry2.delete(0, "end")
        self.entry2.insert(0, "Enter password")
        self.entry2.bind("<FocusIn>", self.on_entry_write)


    def on_entry_write(self, event):
        if event.widget.get() in ["Enter username", "Enter password"]:
            event.widget.delete(0, "end");
            event.widget.unbind("<FocusIn>")




root = Tk()
app = MyFrame(master=root)
app.mainloop()