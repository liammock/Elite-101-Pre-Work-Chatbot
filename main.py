def unfinished():
  print("Currently unfinished, this is a placeholder.")


def age_finder():
  number_is_correct = True
  while number_is_correct == True:
    try:
      age = input("What is your age? ")
      age_int = int(age)
      if age_int in range(1, 29):
        print("Young and fresh!")
      elif age_int in range(30, 59):
        print("Same age as my younger brother!")
      elif age_int in range(60, 79):
        print("I wish I was that young!")
      elif age_int in range(80, 999):
        print("You probably know more than I do!")
      else:
        print("Invalid age")
      number_is_correct = False
      return age
    except ValueError:
      print("Invalid input. Please enter a valid age.")


def option_one():
  unfinished()


def option_two():
  unfinished()


def option_three():
  unfinished()


def option_four():
  unfinished()


def exit(talking):
  print("Goodbye, see you soon!")
  talking = False
  return talking


def list_of_options(talking):
  print("1. Option 1")
  print("2. Option 2")
  print("3. Option 3")
  print("4. Option 4")
  print("5. Exit\n")
  try:
    selection = int(input("Please select an option: "))
    if selection == 5:
      exit(talking)
    elif selection == 1:
      option_one()
    elif selection == 2:
      option_two()
    elif selection == 3:
      option_three()
    elif selection == 4:
      option_four()
    else:
      print("\nI didn't understand that. Please try again.\n")
  except ValueError:
    print("\nI didn't understand that. Please try again.\n")


def chatbot():
  talking = True
  name = input("What is your name? ")
  age = age_finder()
  print(f"\nWhat can I help you with, {name}?\n")
  while talking == True:
    talking = list_of_options(talking)


chatbot()
