number_or_word = input("введіть число або слово: ")

if number_or_word.isdigit():
    a = int(number_or_word)
    print("це число")
    if a % 2 == 0:
        print("це парне число")
    else:
        print("це не парне число")
if number_or_word.isalpha():
    print("це слово")
    print(f"довжина слова {len(number_or_word)} символів")
