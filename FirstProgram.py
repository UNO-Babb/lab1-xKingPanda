#FirstProgram.py
#Name:Michael Fuller
#Date:9/10/2024
#Assignment:Lab 1

def main():
  print("First Program")
  #Say hello
  print("Hello!")
  
  #Ask for the user's name
  name = input("What is your name? ")

  #Use the user's name in the program.
  print(f"Nice to meet you, {name}!")

  #Ask the user for their age.
  age = int(input("How old are you? "))

  #Tell the user what year they were born in.
  #Assume that they have not had their birthday yet this year.
  current_year = 2024
  birth_year = current_year - age

  print(f"You were born in {birth_year}, {name}.")


#Call the main function if this is the file being run.
if __name__ == '__main__':
    main()
