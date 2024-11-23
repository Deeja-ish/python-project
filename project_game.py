import random
    
def generate_story():
   
    stories = [
        {
           'Title' : 'Adventure',
            'story':""" 
            
            Once upon a time, a group of brave adventurers set out on an exciting journey through the ____. 
They were determined to find the legendary ____, that was said to bring good luck to anyone who found it.
As they ventured deeper into the jungle, they ____ past giant ____s and tall trees.
The air was hot and ____, but they didn't give up.
Suddenly, they saw a mysterious ____ appear on the trail.
The adventurers quickly ____ back to avoid it.
But eventually, they reached their destination, where they found the ____s and celebrated their success!
""",

            'word_types' : ['place', 'noun (plural)', 'verb (past tense)', 'animal', 'adjective', 'animal', 'verb (present tense)', 'noun (plural)']
        },
        {
          'Title': 'A day at Zoo',
          'story':"""
          I went to the zoo with my friend, and we saw so many amazing animals!
First, we went to the ____ to see the ____. It was so ____.
Then we ____ to the reptile house, where we saw ____ snakes!
After that, we went to the bird section and saw a giant ____flying high in the sky.
It was the best zoo visit ever, and we can't wait to go again!
""",

               'word_types' : ['place', 'animal', 'adjective', 'verb(past tense)', 'number', 'animal', ]
        },
        {
            'Title': 'The Hunted house',
            'story': """
One night, I decided to visit the old ____. I had heard so many stories about it being haunted.
When I entered, I ____ through the dark hallways. The air was so ____.
Suddenly, I heard a strange sound coming from the ____.
I quickly ____ to investigate, and I saw ____ spooky ghosts floating in the room!
I ran out of the house as fast as I could, vowing never to return.
""",
            'word_types' : [ 'noun(place)', 'verb(past tense)', 'adjective', 'place', 'verb(present tense)', 'number']
        },
        {
            'Title': 'The Superhero Day',
            'story': """
One night, I decided to visit the old ____. I had heard so many stories about it being haunted.
When I entered, I ____ through the dark hallways. The air was so ____.
Suddenly, I heard a strange sound coming from the ____.
I quickly ____ to investigate, and I saw ____ spooky ghosts floating in the room!
I ran out of the house as fast as I could, vowing never to return.
""",

            'word_types': [ 'noun(place)', 'verb(past tense)', 'adjective', 'place', 'verb(present tense)', 'number']
        },
        {
            'Title': 'A day at the beach',
            'story': """
It was a typical day in ____, until something strange happened. A villain was stealing all the ____.
Luckily, ____ showed up just in time to stop them!
The villain tried to ____, but ____ was too ____.
With one mighty punch, the villain was defeated, and the ____ was saved!
The citizens cheered, and ____ flew off into the sky.
""",
           'word_types' : ['city', 'noun(plural)', 'superhero name', 'verb(past tense)', 'superhero name', 'adjective',]
        },
        {
            'Title' : 'The Tree',
            'story' : """
The old oak stood tall and proud, its ____ branches reaching towards the sky. its leaves a ____ of green rustled
in the gentle breeze.A small bird, a ____ creature with feathers of the brightest blue, perched on a branch, singing
a ____ tune
""", 
            'word_types' : ['adjective', 'noun(colour)', 'adjective', 'adjective']
        }
    ]

    difficulty = input("Choose difficulty level (easy/medium): ")

    # Set word types based on difficulty level
    if difficulty.strip().lower() == "easy":
        # Easy: Fewer blanks with common words
        difficulty_multiplier = 0.5
    elif difficulty.strip().lower() == "medium":
        # Medium: Moderate number of blanks
        difficulty_multiplier = 1
    else:
        print("Invalid input. Defaulting to medium difficulty.")
        difficulty_multiplier = 1

 # Random select a story
    story = random.choice(stories)
  
  # Get the tittle and story
    title = story['Title']
    template = story['story']
    word_types = story['word_types']

    num_blanks = int(len(word_types) * difficulty_multiplier)

    
  # # Print the title of the story
    print(f"\nWelcome to the Fill in the blanks! Here's your random story: {title}\n")
    print("Fill in the blanks:")

 # Ask the user for inputs
    filled_story = template
    for word_type in word_types[:num_blanks]:
        user_input = input(f"Enter a {word_type}: ")
        filled_story = filled_story.replace("____", user_input, 1)

    print(f'\nHeres your story:{filled_story}\n')

         # Ask if the user wants to play again
    play_again = input("\nDo you want to play again? (yes/no): ")
    if play_again.strip().lower() == "yes":
     generate_story() 
    else:
        print("Thanks for playing! Goodbye!")
  
# start the game 
generate_story()

  
 

