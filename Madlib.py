# madlibs
# using string, input from users, capitalization, and new line

color1 = input("Enter a color: ")
animal1 = input("Enter an animal: ")
color2 = input("Enter a color: ")
animal2 = input("Enter an animal: ")
color3 = input("Enter a color: ")
animal3 = input("Enter an animal: ")
color4 = input("Enter a color: ")
animal4 = input("Enter an animal: ")
famous_person = input("Enter a celebrity: ")

madlib = f"{color1.capitalize()} {animal1.capitalize()}, {color1.capitalize()} {animal1.capitalize()}, \
What do you see? I see a {color2} {animal2} looking at me.\n\
{color2.capitalize()} {animal2.capitalize()}, {color2.capitalize()} {animal2.capitalize()}, \
What do you see? I see a {color3} {animal3} looking at me.\n\
{color3.capitalize()} {animal3.capitalize()}, {color3.capitalize()} {animal3.capitalize()}, \
What do you see? I see a {color4} {animal4} looking at me.\n\
{color4.capitalize()} {animal4.capitalize()}, {color4.capitalize()} {animal4.capitalize()}, \
What do you see? I see {famous_person.capitalize()} looking at me.\n\
{famous_person.capitalize()}, {famous_person.capitalize()}, What do you see? \
I see a {color1} {animal1}, a {color2} {animal2}, \
a {color3} {animal3}, a {color4} {animal4} looking at me."

print("Title: My Own Version of \"Brown Bear, Brown Bear, What Do You See?\"")
print(madlib)
