name = "Amelia Sun"
print(name)

age = 17
print(age)

height = 1.57
print(height)

print(age + height)
print(age * height)
print(height / age)

intro = name + " " + str(age)
print(intro)

print(intro.upper())
print(intro.lower())
print(intro.title())
print(intro.swapcase())

hobbies = ["Drawing","Writing","Listening to music"]
print(hobbies)

hobbies.append("Reading")
print(hobbies)

hobbies.remove("Drawing")
print(hobbies)

hobbies.reverse()
print(hobbies)

hobbies.sort()
print(hobbies)

profile = {
    "Name": name,
    "Age": age,
    "Height": height,
    "Hobbies": hobbies
}
print(profile)

profile["Favorite Color"] = "Gray"
print(profile)

del profile["Height"]
print(profile)

profile["Number of Hobbies"] = len(hobbies)
print(profile)

profile["Age"] += 1
print(profile)