from tkinter import *
from PIL import ImageTk, Image
from tkinter import messagebox
import random
import pyperclip
import json
reset_new = 0


# ---------------------------------SAVE PASSWORDS-------------------------------
def save():
    is_ok = None
    website_name = Website_Entry.get()
    email = Email_Entry.get()
    password = Password_Entry.get()
    new_data = {
        website_name: {
            "email": email,
            "password": password
        }
    }
    if email == "" or password == "" or website_name == "":
        messagebox.showwarning(title="Password Manager", message="Please don't leave the fields empty.")
    else:
        try:
            with open("new_data.json", "r") as data_file:
                data = json.load(data_file)
        except FileNotFoundError:
            with open("new_data.json", "w") as data_file:
                json.dump(new_data, data_file, indent=4)
                pyperclip.copy(password)
        else:
            with open("new_data.json", "w") as data_file:
                data.update(new_data)
                json.dump(data, data_file, indent=4)
                pyperclip.copy(password)
        finally:
            Website_Entry.delete(0, END)
            Email_Entry.delete(0, END)
            Password_Entry.delete(0, END)


# ------------------------------------------------------------------------------


# ---------------------------------PASSWORD GENERATOR-------------------------------

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
           'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q',
           'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']


def generate_password():
    global letters, numbers, symbols, reset_new
    letters_limit = random.randint(8, 10)
    symbols_limit = random.randint(2, 4)
    numbers_limit = random.randint(2, 4)
    random_letters = [random.choice(letters) for n in range(letters_limit)]
    random_numbers = [random.choice(numbers) for i in range(symbols_limit)]
    random_symbols = [random.choice(symbols) for x in range(numbers_limit)]
    password = random_letters + random_numbers + random_symbols
    random.shuffle(password)
    password = "".join(password)
    Password_Entry.insert(END, password)
    reset_new += 1
    if reset_new == 2:
        Password_Entry.delete(0, END)
        Password_Entry.insert(END, password)
        reset_new = 1


# ------------------------------------------------------------------------------
# ---------------------------- SEARCH BUTTON -----------------------------------

def search_button():
    try:
        with open("new_data.json", "r") as data_file:
            data = json.load(data_file)
            website = Website_Entry.get()
            info = data[website.title()]
            messagebox.showinfo(title="Information", message=f"""Website: {website}
Email: {info["email"]}
Password: {info["password"]}
""")
            pyperclip.copy(info["password"])

    except FileNotFoundError:
        messagebox.showerror("No Data File Found")
    except KeyError:
        if website == "":
            messagebox.showerror(title="Error Message", message="")
        else:
            messagebox.showerror(title="Error Message", message="No details for the website exists.")





# -----------------------------------------------------------------------------
window = Tk()
window.title("Password Generator")
window.config(padx=50, pady=50, bg="White")

logo_img = ImageTk.PhotoImage(Image.open("logo.png"))
canvas = Canvas(window, width=200, height=200, highlightthickness=0, bg="White")
canvas.create_image(100, 100, image=logo_img)
canvas.grid(row=0, column=1)

Website_Label = Label(window, text="Website: ", bg="white")
Website_Label.grid(row=1, column=0)
Email_Label = Label(window, text="Email/Username: ", bg="white")
Email_Label.grid(row=2, column=0)
Password_Label = Label(window, text="Password: ", bg="White")
Password_Label.grid(row=3, column=0)

Website_Entry = Entry(window, width =24, highlightthickness=0.3, borderwidth=2)
Website_Entry.grid(row=1, column=1, sticky="EW")
Email_Entry = Entry(window, width=35, highlightthickness=0.3, borderwidth=2)
Email_Entry.insert(END, "juandelacruz@example.com")
Email_Entry.grid(row=2, column=1, columnspan=2, sticky="EW")
Password_Entry = Entry(window, width=21, highlightbackground="black", highlightthickness=0.3, borderwidth=2)
Password_Entry.grid(row=3, column=1, sticky="EW", )

Search_Button = Button(window, text="Search", bg='White', width=10, command=search_button)
Search_Button.grid(row=1, column=2, sticky="EW")
Generate_Button = Button(window, text="Generate Password", bg="White", command=generate_password)
Generate_Button.grid(row=3, column=2, sticky="EW")
Add_Button = Button(window, text="Add", width=36, bg="White", borderwidth=2, command=save)
Add_Button.grid(row=4, column=1, columnspan=2)


window.mainloop()
