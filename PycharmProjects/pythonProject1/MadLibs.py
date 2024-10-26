color=input("Enter a color:")
noun=input("Enter a noun:")
fruit=input("Enter a fruit:")
print()
print(f"Roses are {color}")
print(f"{noun.title()} are blue")
print(f"I love {fruit}")
print()

story="""Once upon a time in {place}, there lived a {adjective} {animal}. 
Every day, the {animal} would {verb} around {place} looking for {plural_noun}. 
One day, it met a {adjective} {creature} who said, "Let's go on an adventure!" """

place = input("Enter a place: ")
adjective = input("Enter an adjective: ")
animal = input("Enter an animal: ")
verb = input("Enter a verb: ")
plural_noun = input("Enter a plural noun: ")
creature = input("Enter a creature: ")

print("\nHere's your Mad Libs story:")
print(story.format(place=place,adjective=adjective,animal=animal,verb=verb,plural_noun=plural_noun,creature=creature))