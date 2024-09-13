#MadLib.py
#Name:Michael Fuller
#Date:9/10/2024
#Assignment:lab1

def main():
  print("Madlib")
  #Ask user for words
  hero_name = input("Enter the name of your hero: ")
  monster = input("Enter a type of monster: ")
  weapon = input("Enter a type of weapon: ")
  magical_item = input("Enter a magical item: ")
  place= input("Enter a fantasy place: ")
  action = input("Enter an action (past tense): ")


  #Print the story with the user supplied words.
  print(f"Brave hero {hero_name} ventured into the {place}.")
  print(f"There, they encountered a terrifying {monster}, angry and ready to attack!")
  print(f"With their mighty {weapon}, {hero_name} fought fiercely, but the {monster} was too strong.")
  print(f"Just when all seemed lost, {hero_name} remembered the {magical_item} they carried.")
  print(f"With one final move, {hero_name} used the {magical_item} and {action} the {monster}, saving the {place} from destruction!")




#Call the main function if this is the file being run.
if __name__ == '__main__':
    main()
