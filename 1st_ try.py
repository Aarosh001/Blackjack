import random
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
user = []
comp = []
condition = True
for i in range(2):
    user.append(random.choice(cards))
    comp.append(random.choice(cards))
compdisp = comp.copy()
compdisp[0] = "*"
print(f"Your Hand : {user}")
print(f"Computer's Hand : {compdisp}")
if sum(user) == 21 and sum(comp) != 21:
    print("Blackjack!! \nYou win")
elif sum(user) == 21 and sum(comp) == 21:
    print("Push")
option = input("h for Hit, s for stand: ")
while option == "h":
    user.append(random.choice(cards))
    print(f"Your Hand : {user}")
    if sum(user) == 21 and sum(comp) != 21:
        print("Blackjack!! \nYou win")
    elif sum(user) == 21 and sum(comp) == 21:
        print("Push")
    if sum(user) > 21:
        print(f"Computer's Hand : {comp}")
        print("Bust!!")
        exit()
    option = input("h for Hit, s for stand: ")
while condition:
    add = random.choice(cards)
    if (sum(comp) + add) <= 21:
        comp.append(add)
    else:
        condition = False
print(f"Your Hand : {user}")
print(f"Computer's Hand : {comp}")
if sum(user)>sum(comp):
    print("You Win!!")
elif sum(user)==sum(comp):
    print("Push")
else:
    print("Computer Wins!!")
