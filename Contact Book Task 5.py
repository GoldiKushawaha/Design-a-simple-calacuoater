
# Contact Book

import tkinter as tk
from tkinter import messagebox
import json
import os

CONTACT_FILE = "contacts.json"

# Load contacts from file
def load_contacts():
    if os.path.exists(CONTACT_FILE):
        with open(CONTACT_FILE, "r") as f:
            return json.load(f)
    return []

# Save contacts to file
def save_contacts():
    with open(CONTACT_FILE, "w") as f:
        json.dump(contacts, f, indent=4)

# Add a new contact
def add_contact():
    name = name_entry.get().strip()
    phone = phone_entry.get().strip()
    email = email_entry.get().strip()
    address = address_entry.get().strip()
    
    if not name or not phone:
        messagebox.showwarning("Input Error", "Name and Phone are required.")
        return
    
    for contact in contacts:
        if contact['name'] == name:
            messagebox.showerror("Error", "Contact with this name already exists.")
            return

    contacts.append({
        "name": name,
        "phone": phone,
        "email": email,
        "address": address
    })
    save_contacts()
    clear_fields()
    view_contacts()

# View all contacts
def view_contacts():
    contact_listbox.delete(0, tk.END)
    for contact in contacts:
        contact_listbox.insert(tk.END, f"{contact['name']} - {contact['phone']}")

# Search contact
def search_contact():
    query = search_entry.get().strip().lower()
    contact_listbox.delete(0, tk.END)
    for contact in contacts:
        if query in contact['name'].lower() or query in contact['phone']:
            contact_listbox.insert(tk.END, f"{contact['name']} - {contact['phone']}")

# On selecting a contact
def on_select(event):
    try:
        index = contact_listbox.curselection()[0]
        selected = contact_listbox.get(index)
        name = selected.split(" - ")[0]
        for contact in contacts:
            if contact['name'] == name:
                name_entry.delete(0, tk.END)
                name_entry.insert(0, contact['name'])
                phone_entry.delete(0, tk.END)
                phone_entry.insert(0, contact['phone'])
                email_entry.delete(0, tk.END)
                email_entry.insert(0, contact['email'])
                address_entry.delete(0, tk.END)
                address_entry.insert(0, contact['address'])
    except IndexError:
        pass

# Update contact
def update_contact():
    name = name_entry.get().strip()
    for contact in contacts:
        if contact['name'] == name:
            contact['phone'] = phone_entry.get().strip()
            contact['email'] = email_entry.get().strip()
            contact['address'] = address_entry.get().strip()
            save_contacts()
            view_contacts()
            messagebox.showinfo("Updated", "Contact updated successfully.")
            return
    messagebox.showerror("Error", "Contact not found.")

# Delete contact
def delete_contact():
    name = name_entry.get().strip()
    for contact in contacts:
        if contact['name'] == name:
            contacts.remove(contact)
            save_contacts()
            clear_fields()
            view_contacts()
            messagebox.showinfo("Deleted", "Contact deleted successfully.")
            return
    messagebox.showerror("Error", "Contact not found.")

# Clear input fields
def clear_fields():
    name_entry.delete(0, tk.END)
    phone_entry.delete(0, tk.END)
    email_entry.delete(0, tk.END)
    address_entry.delete(0, tk.END)

# Main GUI
root = tk.Tk()
root.title("Contact Book")
root.geometry("500x500")
root.configure(bg="lightyellow")

contacts = load_contacts()

# Input Fields
tk.Label(root, text="Name:", bg="lightyellow").pack()
name_entry = tk.Entry(root, width=40)
name_entry.pack()

tk.Label(root, text="Phone:", bg="lightyellow").pack()
phone_entry = tk.Entry(root, width=40)
phone_entry.pack()

tk.Label(root, text="Email:", bg="lightyellow").pack()
email_entry = tk.Entry(root, width=40)
email_entry.pack()

tk.Label(root, text="Address:", bg="lightyellow").pack()
address_entry = tk.Entry(root, width=40)
address_entry.pack()

# Buttons
tk.Button(root, text="Add Contact", command=add_contact, bg="green", fg="white").pack(pady=5)
tk.Button(root, text="Update Contact", command=update_contact, bg="orange", fg="white").pack(pady=5)
tk.Button(root, text="Delete Contact", command=delete_contact, bg="red", fg="white").pack(pady=5)

# Search
tk.Label(root, text="Search by Name or Phone:", bg="lightyellow").pack()
search_entry = tk.Entry(root, width=30)
search_entry.pack()
tk.Button(root, text="Search", command=search_contact, bg="blue", fg="white").pack(pady=5)

# Contact List
contact_listbox = tk.Listbox(root, width=50)
contact_listbox.pack(pady=10)
contact_listbox.bind('<<ListboxSelect>>', on_select)

# Load and display contacts
view_contacts()

root.mainloop()