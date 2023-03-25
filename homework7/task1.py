phone_book = {"name": "Serhii", "last name": "Polischuk", "phone number": "+380634683778"}
user_comands = input("enter the command: ")
if user_comands == "stats":
    print(len(phone_book))
if user_comands == "add":
    add_name = input("enter name: ")
    add_second_name = input("enter last name: ")
    add_phone_number = input("enter phone number: ")
    phone_book.update({"name of second user": add_name, "last name of second user": add_second_name, "phone number of second user": add_phone_number})
    print(phone_book)
if user_comands == "del":
    delete_comands = input("enter what you want to delete: ")
    if delete_comands == "delete name":
        del phone_book["name"]
    if delete_comands == "delete last name":
        del phone_book["last name"]
    if delete_comands == "delete phone number":
        del phone_book["phone number"]
    if delete_comands == "delete name of second user":
        del phone_book["name of second user"]
    if delete_comands == "delete last name of second user":
        del phone_book["last name of second user"]
    if delete_comands == "delete phone number of second user":
        del phone_book["phone number of second user"]
    print(phone_book)
if user_comands == "show name":
    print(phone_book.get("name"))
    print(phone_book.get("last name"))
    print(phone_book.get("phone number"))
