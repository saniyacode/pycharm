from tkinter import *
import string
import secrets

def generate_password():
    password_length = int(length_entry.get())
    if password_length < 4:
        password_result.set("Length should be at least 4 characters")
        return

    chars = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(secrets.choice(chars) for _ in range(password_length))
    password_result.set(password)

# Create the main window
root = Tk()
root.title("Password Generator")

# Variables
password_result = StringVar()

# GUI Components
label_title = Label(root, text="Password Generator", font=("Arial", 24, "bold"), fg="navy")
label_title.pack(pady=10)

label_length = Label(root, text="Enter Password Length:", font=("Arial", 12))
label_length.pack()

length_entry = Spinbox(root, from_=4, to=50, width=5, font=("Arial", 12))
length_entry.pack()

generate_button = Button(root, text="Generate Password", command=generate_password, font=("Arial", 12, "bold"), bg="green", fg="white")
generate_button.pack(pady=10)

password_label = Label(root, text="Generated Password:", font=("Arial", 16, "bold"), fg="blue")
password_label.pack()

password_display = Label(root, textvariable=password_result, font=("Arial", 14), fg="black", relief="solid", bd=2, padx=10, pady=5)
password_display.pack(pady=10, ipadx=10, ipady=5)

# Run the application
root.mainloop()
