
print("Welcome to madLibs!\n")

while True:
    character = input("Name of the character of the story?\n").capitalize()
    verb1 = input("Please, enter a verb.\n").lower()
    verb2 = input("Please, enter another verb.\n").lower()
    adjective1 = input("Please, enter an adjective.\n").lower()
    adjective2 = input("Please, enter another adjective.\n").lower()
    destination = input("Please, enter a destination.\n").lower()

    story_template = f"""
One morning, {character} woke up feeling very {adjective1}. 
Determined to change their day, they decided to {verb1} outside. 
As they stepped out, the weather was surprisingly {adjective2}, perfect for an adventure. 
   
Without thinking twice, {character} chose to {verb2} all the way to {destination}. 
Little did they know, something incredible was about to happen..."""

    print(story_template)

    game = input("\nWould you like to play again? Yes/No\n").strip().lower()
    if game == "yes":
        print("Let's play again!")
    else:
        print("Thank you for playing")
        break


