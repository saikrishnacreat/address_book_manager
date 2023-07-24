def address_book_manager(): #main function
    file_name = '' #this is the text name
    entries = []

    while True:
        user_input = input("Enter action: ") #enter the action used to perform on the text file.
        action = user_input.split(' ')[0].lower()

        if action == 'read':
            file_name = user_input.split(' ')[1]
            entries = read_Entries(file_name)
        elif action == 'add':
            entry_info = user_input.split(', ')[1:]
            new_entry={}
            if len(entry_info) == 4:
                new_entry = {
                    'Name': entry_info[0],
                    'Email': entry_info[1],
                    'Phone': entry_info[2],
                    'Address': entry_info[3]
                }
                add_entry(entries, new_entry)
            else:
                handle_unexpected_input()
        elif action == 'remove':
            email = user_input.split(' ')[1]
            remove_entry(entries, email)
        elif action == 'update':
            entry_info = user_input.split(' ')[1:]
            if len(entry_info) == 4:
                updated_entry = {
                    'Name': entry_info[0],
                    'Email': entry_info[1],
                    'Phone': entry_info[2],
                    'Address': entry_info[3]
                }
                update_entry(entries, updated_entry)
            else:
                handle_unexpected_input()
        elif action == 'search':
            key_word = user_input.split(' ')[1]
            search_entries(entries, key_word)
        elif action == 'print':
            print_entries(entries)
        elif action == 'save':
            file_name = user_input.split(' ')[1]
            save_entries(file_name, entries)
        elif action == 'quit':
            break
        else:
            handle_unexpected_input()



def read_Entries(file_name): #function used to read entries from text file
    entries = []
    try: 
        with open(file_name, 'r') as file:
            for line in file:
                entry = line.strip().split(', ')
                entries.append({
                    'Name': entry[0],
                    'Email': entry[1],
                    'Phone': entry[2],
                    'Address': entry[3]
                })
        print("Entries read from file.")
    except FileNotFoundError:
        print("File not found. No entries read.")
    return entries


def save_entries(file_name, entries): #used to save entries in text file
    try:
        with open(file_name, 'w') as file:
            for entry in entries:
                line = f"{entry['Name']}, {entry['Email']}, {entry['Phone']}, {entry['Address']}\n"
                file.write(line)
        print("Entries saved to file.")
    except IOError:
        print("Error occurred while saving entries to file.")


def add_entry(entries, new_entry): # function used to add entries in the text file
    for entry in entries:
        if entry['Email'] == new_entry['Email']: #function checks whether the entry is new or not
            print("Email already exists. Entry not added.")
            return
    entries.append(new_entry)
    entries.sort(key=lambda x: x['Email'])
    print("Entry added successfully.")


def remove_entry(entries, email): # function used to remove entry from the text file
    for entry in entries:
        if entry['Email'] == email:
            entries.remove(entry)
            print("Entry removed successfully.")
            return
    print("Email not found. Entry not removed.")


def update_entry(entries, updated_entry): #function used to update entry in the text
    email = updated_entry['Email']
    for entry in entries:
        if entry['Email'] == email:
            entry.update(updated_entry)
            print("Entry updated successfully.")
            return
    print("Email not found. Entry not updated.")


def search_entries(entries, key_word): #function used to search the entry in the text file
    found_entries = []
    for entry in entries:
        if key_word.lower() in entry['Name'].lower() or key_word.lower() in entry['Email'].lower() or \
                key_word.lower() in entry['Phone'].lower() or key_word.lower() in entry['Address'].lower():
            found_entries.append(entry)

    if found_entries:
        print("Found entries:")
        for entry in found_entries:
            print_entry(entry)
    else:
        print("No matching entries found.")


def print_entries(entries): #function used to print the entries
    if entries:
        print("All entries:")
        for entry in entries:
            print_entry(entry)
    else:
        print("Address book is empty.")


def print_entry(entry):
    print("Name:", entry['Name'])
    print("Email:", entry['Email'])
    print("Phone:", entry['Phone'])
    print("Address:", entry['Address'])
    print()


def validate_email(email):
    if '@' in email and '.' in email:
        return True
    return False

def handle_unexpected_input(): #this function handles the unexpected errors
    print("Invalid input.Enter Valid Input. Please try again.")

address_book_manager()
