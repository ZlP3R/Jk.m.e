def add_any_numbers_of_arguments(*args):
  a = 0
  for i in args:
    a += i

  print(a)
add_any_numbers_of_arguments(12, 43, 54, 768, 5)