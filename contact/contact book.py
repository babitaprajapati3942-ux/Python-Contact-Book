import tkinter as tk
from tkinter import messagebox

window = tk.Tk()
window.title("Contact Book")
window.geometry("600x600")
window.resizable(False, False)

contacts = []
selected_index = -1


# Heading
tk.Label(
    window,
    text="📒 CONTACT BOOK",
    font=("Arial", 24, "bold")
).pack(pady=10)


# Form
form = tk.Frame(window)
form.pack()


tk.Label(form, text="Name:", font=("Arial", 12)).grid(row=0, column=0, padx=5, pady=5)
name_entry = tk.Entry(form, width=35, font=("Arial", 12))
name_entry.grid(row=0, column=1, padx=5, pady=5)


tk.Label(form, text="Phone:", font=("Arial", 12)).grid(row=1, column=0, padx=5, pady=5)
phone_entry = tk.Entry(form, width=35, font=("Arial", 12))
phone_entry.grid(row=1, column=1, padx=5, pady=5)


tk.Label(form, text="Email:", font=("Arial", 12)).grid(row=2, column=0, padx=5, pady=5)
email_entry = tk.Entry(form, width=35, font=("Arial", 12))
email_entry.grid(row=2, column=1, padx=5, pady=5)


tk.Label(form, text="Address:", font=("Arial", 12)).grid(row=3, column=0, padx=5, pady=5)
address_entry = tk.Entry(form, width=35, font=("Arial", 12))
address_entry.grid(row=3, column=1, padx=5, pady=5)


# Contact list
tk.Label(
    window,
    text="Contact List",
    font=("Arial", 16, "bold")
).pack(pady=8)

contact_list = tk.Listbox(
    window,
    width=55,
    height=8,
    font=("Arial", 12)
)
contact_list.pack()


def clear_fields():
    name_entry.delete(0, tk.END)
    phone_entry.delete(0, tk.END)
    email_entry.delete(0, tk.END)
    address_entry.delete(0, tk.END)


def add_contact():

    name = name_entry.get()
    phone = phone_entry.get()
    email = email_entry.get()
    address = address_entry.get()

    if name == "" or phone == "":
        messagebox.showwarning(
            "Warning",
            "Please enter Name and Phone."
        )
        return

    contacts.append({
        "name": name,
        "phone": phone,
        "email": email,
        "address": address
    })

    contact_list.insert(
        tk.END,
        name + " - " + phone
    )

    clear_fields()


def select_contact(event):

    global selected_index

    selected = contact_list.curselection()

    if selected:
        selected_index = selected[0]

        contact = contacts[selected_index]

        clear_fields()

        name_entry.insert(0, contact["name"])
        phone_entry.insert(0, contact["phone"])
        email_entry.insert(0, contact["email"])
        address_entry.insert(0, contact["address"])


def update_contact():

    if selected_index == -1:
        messagebox.showwarning(
            "Warning",
            "Select a contact first."
        )
        return

    contacts[selected_index] = {
        "name": name_entry.get(),
        "phone": phone_entry.get(),
        "email": email_entry.get(),
        "address": address_entry.get()
    }

    contact_list.delete(selected_index)

    contact_list.insert(
        selected_index,
        name_entry.get() + " - " + phone_entry.get()
    )

    clear_fields()


def delete_contact():

    global selected_index

    selected = contact_list.curselection()

    if not selected:
        messagebox.showwarning(
            "Warning",
            "Select a contact first."
        )
        return

    index = selected[0]

    contact_list.delete(index)
    contacts.pop(index)

    selected_index = -1

    clear_fields()


def search_contact():

    search = search_entry.get().lower()

    contact_list.delete(0, tk.END)

    for contact in contacts:

        if (
            search in contact["name"].lower()
            or search in contact["phone"]
            or search in contact["email"].lower()
        ):

            contact_list.insert(
                tk.END,
                contact["name"] + " - " + contact["phone"]
            )


# Buttons
button_frame = tk.Frame(window)
button_frame.pack(pady=8)

tk.Button(
    button_frame,
    text="ADD",
    width=12,
    command=add_contact
).grid(row=0, column=0, padx=5)

tk.Button(
    button_frame,
    text="UPDATE",
    width=12,
    command=update_contact
).grid(row=0, column=1, padx=5)

tk.Button(
    button_frame,
    text="DELETE",
    width=12,
    command=delete_contact
).grid(row=0, column=2, padx=5)


# Search
search_frame = tk.Frame(window)
search_frame.pack(pady=5)

search_entry = tk.Entry(
    search_frame,
    width=30,
    font=("Arial", 12)
)
search_entry.grid(row=0, column=0, padx=5)

tk.Button(
    search_frame,
    text="SEARCH",
    width=10,
    command=search_contact
).grid(row=0, column=1)


contact_list.bind(
    "<<ListboxSelect>>",
    select_contact
)


window.mainloop()