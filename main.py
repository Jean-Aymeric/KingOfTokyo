from kingoftokyiodice import KingOfTokyoDice

diceBag = []
for i in range(6):
    diceBag.append(KingOfTokyoDice())

for dice in diceBag:
    print(dice.roll())
print("Quels dés voulez-vous garder ?")
userChoice = input()
userChoice = userChoice.split()
for i in range(len(userChoice)):
    diceBag[int(userChoice[i]) - 1].keep()
 
for dice in diceBag:
    print(dice.roll())
print("Quels dés voulez-vous garder ?")
userChoice = input()
userChoice = userChoice.split()
for i in range(len(userChoice)):
    diceBag[int(userChoice[i]) - 1].keep()

for dice in diceBag:
    print(dice.roll())
