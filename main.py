### Basic Contact Book Application


print("It is your Contact Book. You can add, update, search or remove your contact book \n")

def add():
    with open("contact.txt", "a") as file:
        name = input("Name: ")
        phone = input("Phone Number: ")
        file.writelines((f"{name} : {phone}\n"))

def search():
    search_term = input("What do you want to search?")
    found_contacts = []
    
    with open("contact.txt", "r") as file:
        for line in file:
            if search_term.lower() in line.lower():
                found_contacts.append(line)
        
        if found_contacts:
            print("Found contacts: ")
            for contact in found_contacts:
                print(contact)

def update():
    old_word = input("Which word do you want to update? ")
    new_word = input("Write updated word: ")
    
    with open("contact.txt", "r") as file:
        lines = file.readlines()
        
    updated_lines = []
    for line in lines:
        if old_word in line:
            updated_line = line.replace(old_word, new_word)
            updated_lines.append(updated_line)
        else:
            updated_lines.append(line)
            
    with open("contact.txt", "w") as file:
        file.writelines(updated_lines)
        
    print("Contact updated successfully!")

def remove():
    contact_to_remove = input("Which contact do you want to remove? ")

    with open("contact.txt", "r") as file:
        lines = file.readlines()

    updated_lines = []
    removed = False
    for line in lines:
        if contact_to_remove.lower() not in line.lower():
            updated_lines.append(line)
        else:
            removed = True

    if removed:
        with open("contact.txt", "w") as file:
            file.writelines(updated_lines)
        print("Contact removed successfully.")
    else:
        print("Contact not found.")

while True:
    choice = input("1: Add contact\n2: Update contact\n3: Search contact\n4: Remove contact\nq: Quit\nYour choice: ")
    if choice == "1":
        add()
        continue
    elif choice == "2":
        update()
        continue
    elif choice == "3":
        search()
        continue
    elif choice == "4":
        remove()
        continue
    elif choice == str("q"):
        break

print("You closed phonebook!")