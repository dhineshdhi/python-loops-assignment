import json
inventory = [
    {"title": "The Alchemist", "author": "Paulo Coelho", "price": 12.99, "in_stock": True},
    {"title": "1984", "author": "George Orwell", "price": 9.99, "in_stock": True}
]

with open("inventory.json","w") as file:
    json.dump(inventory, file, indent=4)
print("file created!")

with open("inventory.json","r") as file:
   json.load(file)
print("Total Books in inventory:",len(inventory))

new_book = {"title": "Atomic Habits", "author": "James Clear", "price": 14.99, "in_stock": True}

inventory.append(new_book)

with open("inventory.json","w") as file:
    json.dump(inventory,file,indent=4)
print("New book added! and Total number of books now is:",len(inventory))