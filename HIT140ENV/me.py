print("Md Mahir ")
surname = "Islam"
print(surname)
surname = "Mr." + surname
print(surname)
buddies = ["Sadik", "Meher", "Kapil"]
for buddy in buddies:
    print(buddy)
profile = {
    "title": "Mr.",
    "surname": "Islam",
    "firstname": "Md Mahir",
    "myBuddies": ["Sadik", "Meher", "Kapil"]
}  
for buddy in profile["myBuddies"]:
    print(buddy)
with open("mybuddies.txt", "r") as file:
    for line in file:
        print(line.strip())
# with open("mybuddies.txt", "a") as file:
#    file.write("Andrew")
def printMultiplesofThree():
    for i in range(1, 6):
        print(i * 3)
        
printMultiplesofThree()
def printMultiplesofThree(count):
    for i in range(1, count + 1):
        print(i * 3)
        
printMultiplesofThree(5)
printMultiplesofThree(10)

