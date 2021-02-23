from tkinter import *
import sqlite3
root = Tk()
root.title("MOBILE NUMBERS")
root.geometry("280x300")
#root.configure(background="gray")

# labels:

#label = Label(root, text='ENTER YOUR INFORMATION HERE', bg = 'lightblue')
#label.grid(row=0, column=0, sticky=W, padx=20, pady=30)

name = Label(root, text='Enter name: ')
name.grid(row=0, column=0, sticky=W, padx=20, pady=(10, 0))

phone = Label(root, text='Enter contact number: ')
phone.grid(row=1, column=0, sticky=W)

text = Text(root, width=9, height=7, wrap=WORD)
text.grid(row=6, column=0, columnspan=4, sticky=W, pady=10, padx=10, ipadx=90)

# entry box:

name_var = StringVar()
name_entrybox = Entry(root, width=16, textvariable=name_var)
name_entrybox.grid(row=0, column=1, padx=10, pady=(10, 0))

phone_var = StringVar()
phone_entrybox = Entry(root, width=16, textvariable=phone_var)
phone_entrybox.grid(row=1, column=1)


# Submit button actions and storing user inputs into DB:

def action():
    conn = sqlite3.connect('phonebook.db')
    c = conn.cursor()
    c.execute("INSERT INTO phonebook.db VALUES(:name, :contact)",
              {
                  'name': name_var.get(),
                  'contact': phone_var.get()
              }
              )
    c.execute("SELECT *,oid FROM phonebook")
    records = c.fetchall()
   
    # fetchall numbers from DB into list:

    list = []
    for i in records:
        list.append(i[1])

    new_list = []
    for i in range(0, len(list)-1):
        new_list.append(list[i])
    print(new_list)

    # Showing message on screen :

    no = (phone_var.get())
    no_msg = ""
    if int(no) not in new_list and len(no) == 10:
        no_msg = "Registerd Succesfully Number is : " + str(no)
    elif len(no) < 10 or len(no) > 10:
        no_msg = "Invalid Number"
        list = new_list
    elif int(no) in new_list:
        no_msg = "Already registered"
        list = new_list

    name = name_var.get()

    text.insert(END, name + " " + no_msg + " ")
    print(no_msg)
    conn.commit()
    conn.close()

# button:

btn = Button(root, text='Submit', command=action)
btn.grid(row=3, column=0, columnspan=2, pady=10, padx=10, ipadx=90)

root.mainloop()