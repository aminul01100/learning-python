"""
business: Contact book system
functionalities:
    1. add a Contact
    2. view a Contact (provide a contact id and get the contact details)
    3. search a Contact
    4. delete a Contact
    5. update a Contact
        - there will be three methods for updating a contact's name, phone number and address separately
        - each method will take the contact id and the new value for the respective field as input and 
            update the contact details accordingly
"""

class Contact:
    def __init__(self, contact_id, name, phone_number, address=None):
        self.id = contact_id
        self.name = name
        self.phone_number = phone_number
        self.address = address

    def __str__(self):
        return f"Contact(id={self.id}, name={self.name}, phone_number={self.phone_number})"

class ContactBook:
    def __init__(self):
        self.number_of_contacts = 0
        self.contacts = dict()

    def __str__(self):
        contact_str = ""
        for contact_id, contact in self.contacts.items():
            contact_str += str(contact) + "\n"
        return f"ContactBook(number_of_contacts={self.number_of_contacts}, \
                contacts=\n{contact_str})"

    # 1. add a Contact
    def add_contact(self, name, phone_number, address=None):
        # generating the new contact id
        new_contact_id = self.number_of_contacts + 1

        # creating a new contact object and adding it to the contacts dictionary
        new_contact = Contact(new_contact_id, name, phone_number, address)
        self.contacts[new_contact_id] = new_contact

        # updating the number of contacts in the contact book
        self.number_of_contacts += 1
    
    # 2. view a Contact (provide a contact id and get the contact details)
    def get_contact(self, contact_id):
        if contact_id in self.contacts:
            return self.contacts[contact_id]
        else:
            return None

    

    # 3. search a Contact
    def search_contact(self, search_keyword):
        matched_contact_list = []
        for contact_id, contact in self.contacts.items():
            if contact.name.__contains__(search_keyword):
                matched_contact_list.append(contact)
        return matched_contact_list

    # update name
    def update_contact_name(self, contact_id, new_name):
        if contact_id in self.contacts:
            self.contacts[contact_id].name = new_name
            return True
        else:
            return False

contact_book = ContactBook()
# print("Contact Book after initialization:", contact_book)

contact_book.add_contact("Alice", "1234567890", "123 Main St")
contact_book.add_contact("Bob", "0987654321")
contact_book.add_contact("Charlie", "1112223333", "456 Elm St")
contact_book.add_contact("David", "5556667777", "789 Oak St")
contact_book.add_contact("Evan liam", "9998887777", "321 Pine St")
# print("Contact Book after adding contacts:", contact_book)

# print("Viewing contact with id 2:", contact_book.get_contact(2))
# matched_contact_list = contact_book.search_contact("li")
"""
want to develop list of the string from the contact lists
option 1:
list_of_matched_contact_info = []
for contact in matched_contact_list:
    list_of_matched_contact_info.append(str(contact))

option 2:
using list comprehension-
list_of_matched_contact_info = [str(contact) for contact in matched_contact_list] 
"""
# searching a contact with the keyword "li" and printing the matched contact details
# list_of_matched_contact_info = [str(contact) for contact in matched_contact_list]
# print("Matched contacts:", list_of_matched_contact_info)

# updating the name of the contact with id 3 to "Charlie Brown"
# updated_status = contact_book.update_contact_name(3, "Charlie Brown")
# print(contact_book.get_contact(3))

def take_input_and_add_contact():
    try:
        name = input("Please enter the contact name: ")
        phone_number = input("Please enter the contact phone number: ")
        address = input("Please enter the contact address (optional): ")
        if address == "":
            address = None

        # validating the user input for name and phone number fields
        if name == "" or phone_number == "":
            logger.error("Name and phone number are required fields. Contact cannot be added.")
            return False

        contact_book.add_contact(name, phone_number, address)
        print("Contact added successfully!")
        return True
    except Exception as e:
        logger.error(f"An error occurred while adding the contact: {e}")
        return False

def take_input_and_view_contact():
    try:
        contact_id = input("Please enter the contact id: ")
        contact_id = int(contact_id)
        contact = contact_book.get_contact(contact_id)
        if contact:
            print(f"Contact details for {contact_id}: {contact}")
        else:
            logger.error("Contact not found.")
    except Exception as e:
        logger.error(f"An error occurred while viewing the contact: {e}", exc_info=True)

import logging

logger = logging.getLogger(__name__)

while True:
    print("Here are the functionalities that a user can choose-")
    print("1. add a Contact")
    print("2. view a Contact (provide a contact id and get the contact details)")
    print("3. search a Contact")
    print("4. update a Contact Name")

    user_input = input("Please enter the number corresponding to the functionality you want to use: ")
    if user_input == "1":
        # name, phone number and address (optinal)
        _ = take_input_and_add_contact()
        continue

    elif user_input == "2":
        take_input_and_view_contact()
        continue

    