"""Practice with dictionaries."""

ice_cream: dict[str, int] = {"chocolate": 12, "vanilla": 8, "strawberry": 5}

#Adding
ice_cream["mint"] = 3
print("After adding mint:")
print(ice_cream)

#Removing
ice_cream.pop("mint")
print("After removing mint:")
print(ice_cream)

#Accessing
print(f"Number of vanilla orders: {ice_cream['vanilla']}")

#Updating a value
ice_cream["vanilla"] += 1
print("After adding one vanilla")
print(ice_cream)
print(f"Number of vanilla orders: {ice_cream['vanilla']}")

#Checking if in dictionary
print("mint" in ice_cream)
print("chocolate" in ice_cream)

#Q8
courses: dict[int, str] = dict()
courses[110] = "Intro to Programming"
courses[210] = "Data Structures"
print(courses[110])

#Q14
numbers: dict[int, int] = {1: 10, 2: 20, 3: 30}
print(numbers)

#Q15
points: dict[str, int] = {"Kris": 0, "Kaki": 10}
points["Kaki"] += 100
print(points)

#Q18
print(f"Number of vanilla orders: {ice_cream['cookie dough']}")