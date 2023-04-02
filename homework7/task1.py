phone_book = [{"name": "Serhii", "phone number": "+380634683778"},
              {"name": "Kiril", "phone number": "+380634532457"},
              {"name": "sofia", "phone number": "+380506754823"},
              {"name": "oleksandr", "phone number": "+380508945678"}]

def comand_stats():
        a = len(phone_book)
        print(f"in phone book {a} contacts")
def add_name():
        lst = {}
        lst["name"] = a
        lst["phone number"] = g
        b = input(f"enter data is correct? {lst}: ")
        if b == "yes":
            phone_book.append(lst)
            print(phone_book)
        if b == "no":
            lst["name"] = input("enter user name: ")
            lst["phone number"] = input("enter phone number: ")
            phone_book.append(lst)
            print(phone_book)
def show_contact(name):
    c = ''
    for i in phone_book:
        if name == i.get("name"):
            c = name
            print(f"Name: {i.get('name')}\nPhone number: {i.get('phone number')}")

def delete_contact(name):
    c = ''
    for i in phone_book:
        if name == i.get("name"):
            c = name
            phone_book.remove(i)

def all_names_in_book():
    for i in phone_book:
        i.get("name")
        print(i.get("name"))


while True:
    comands = input("enter comand: ")

    if comands == "add":
        a = input("enter user name: ")
        g = input("enter phone number: ")
        print(add_name())
        exit()

    if comands == "show contact":
        d = input("enter name of contact: ")
        print(show_contact(d))
        if d == "close":
            exit()

    if comands == "stats":
        print(comand_stats())
        exit()

    if comands == "delete":
        e = input("enter name of contact: ")
        print(delete_contact(e))
        print (phone_book)
        exit()

    if comands == "list":
        print(all_names_in_book())
        exit()

    if comands == "close":
        exit()



