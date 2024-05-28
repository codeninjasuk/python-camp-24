# Define a function to gather user input with examples
def get_input(prompt, example):
    return input(f"{prompt} (e.g., {example}): ")

# Collect user inputs with examples
adjective1 = get_input("Enter an adjective", "funny")
silly_name = get_input("Enter a silly name", "Goofy")
adjective2 = get_input("Enter another adjective", "curious")
verb1 = get_input("Enter a verb", "jump")
verb_ing = get_input("Enter a verb ending in -ing", "running")
adjective3 = get_input("Enter another adjective", "sparkly")
plural_noun1 = get_input("Enter a plural noun", "cupcakes")
number = get_input("Enter a number", "7")
animal = get_input("Enter an animal", "kangaroo")
adjective4 = get_input("Enter another adjective", "colorful")
funny_sound = get_input("Enter a funny sound", "boing")
adjective5 = get_input("Enter another adjective", "giant")
noun = get_input("Enter a noun", "balloon")
verb2 = get_input("Enter another verb", "dance")
adjective6 = get_input("Enter another adjective", "wacky")
verb3 = get_input("Enter another verb", "sing")
verb4 = get_input("Enter another verb", "laugh")

# Create the story
story = f"""
Once upon a time in a {adjective1} village, there was a curious kid named {silly_name}. 
This kid had a {adjective2} pet who loved to {verb1}. 
One day, while {verb_ing} in the backyard, {silly_name} discovered a {adjective3} treasure chest filled with {plural_noun1}.

Excited, {silly_name} decided to share {number} of the {plural_noun1} with a {animal} who rode a {adjective4} unicycle. 
When the animal arrived, it made a {funny_sound} noise, and out popped a {adjective5} {noun} that could {verb2}!

From that day on, {silly_name} and the {animal} became the most {adjective6} friends in the village, known for their ability to {verb3} and make everyone {verb4} with laughter.
"""

# Print the story
print(story)
