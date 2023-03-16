the_data = input("write what you want: ")

for i in the_data:
    if i.isdigit():
        a = int(the_data)
        if a % 2 == 0:
            print(i + " це число воно парне")
        if a % 2 != 0:
            print(i + " це число воно не парне")
    if i.isalpha():
        if the_data.islower():
            print("це літера вона маленька")
        if the_data.isupper():
            print("це літера вона велика")
else:
    print("це символи")

# мабуть я щось зробив не так але воно всеж таки працює :(