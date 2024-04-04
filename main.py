from tkinter import *
from tkinter import messagebox
from random import randint, random, shuffle, choice
# import pyperclip
import json
# ---------------------------- PASSWORD GENERATOR ------------------------------- #

def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']


    password_letters = [choice(letters) for char in range(randint(8, 10))]
    password_symbols = [choice(symbols) for char in range(randint(2,4))]
    password_numbers = [choice(numbers) for char in range(randint(2, 4))]

    password_list = password_letters + password_symbols + password_numbers
    shuffle(password_list)
    password = ''.join(password_list)

    password_input.insert(0, password)
    # pyperclip.copy(password)

# print(f"Your password is: {password}")
# ---------------------------- SAVE PASSWORD ------------------------------- #

def save():
    website = website_input.get()
    username = username_input.get()
    password = password_input.get()

    new_data = {
        website : {
            'email' : username, 
            'password': password, 

        }
    }

    if len(website) == 0 or len(password)==0:
        messagebox.showerror(title='Opps', message='Please do not leave any fields empty!')

    else: 
        is_ok = messagebox.askokcancel(title= website, message=f'These are the details entered:\nEmail: {username} \n'
                           f'Password: {password}\n Is it ok to save?')

        if is_ok:
            # with  open('new_text.txt', mode='a') as file:
                # file.write(f'{website}  |  {username}  |  {password}\n')
            # with open('data.json', 'w') as data_file: #para escribir y crear formato json
                # json.dump(new_data, data_file, indent=4)
            
            
            try:
                with open('data.json', 'r') as data_file: #para leer y actualizar formato json
                    # reading old data
                    data = json.load(data_file)
                    # update new data
                    data.update(new_data) #lo actualiza en formato dict python 
                with open('data.json', 'w') as data_file: #para escribir y crear formato json
                    # saving updated data
                    json.dump(data, data_file, indent=4)
            except:
                with open('data.json', 'w') as data_file: #para escribir y crear formato json
                    # saving updated data
                    json.dump(new_data, data_file, indent=4)
                
            website_input.delete(0, END)
            password_input.delete(0, END)
            website_input.focus()

# ---------------------------- seacrh password ------------------------------- #    

def search_password():
    website = website_input.get()
    
    
    if len(website) > 0:
        try:
            with open('data.json', 'r') as data_file:
                data = json.load(data_file)
                password = data[website]['password']  
                username = data[website]['email']      
                if website in data:
                    messagebox.showinfo(title=website, message=f'Email: {username}\n'
                                        f'Password: {password}')
        except:
            messagebox.showwarning(title=website, message=f"No details for '{website}' found, try again")

    else:
        messagebox.showerror(title='Error', message='No data file found')





# ---------------------------- UI SETUP ------------------------------- #


window = Tk()
window.title('Password Manager')
window.config(padx=30, pady=50, bg= 'white')

canvas = Canvas(width=200, height=200, highlightthickness=0, bg='white')
logo_img = PhotoImage(file='logo.png')
canvas.create_image(100, 100, image = logo_img)
# timer_text = canvas.create_text(103, 130, text='00:00', fill='white', font=(FONT_NAME, 35, 'bold'))
canvas.grid(column=1, row=1)

website_label = Label(text='Website:', bg='white')
website_label.grid(column=0, row=2)

email_label = Label(text='Email/Username:', bg='white')
email_label.grid(column=0, row=3)

password_label = Label(text='Password:',  bg='white')
password_label.grid(column=0, row=4)

website_input = Entry(width=36 )
website_input.grid(column=1, row=2, pady=5)
website_input.focus()

username_input = Entry(width=55, )
username_input.grid(column=1, row=3, columnspan=2, pady=10)
username_input.insert(0, 'jaimevillalbaoyola@gmail.com')

password_input = Entry(width=36,)
password_input.grid(column=1, row=4, pady=5)

button_generate = Button(text='Generate Password', command= generate_password )
button_generate.grid(column=2, row=4)

button_add = Button(width=47, text='Add', command=save)
button_add.grid(column=1, row=5, columnspan=2, pady=5)

button_search = Button(text='Search', width=15, command=search_password)
button_search.grid(column=2, row=2)

window.mainloop()

