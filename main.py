import random
arrayOfLetters = []
for x in range(20):
    number = random.randint(0, 2)
    if number == 0:
        letter = "R"
    elif number == 1:
        letter = "Y"
    elif number == 2:
        letter = "B"
    arrayOfLetters.append(letter)
print(arrayOfLetters)

count = 0
RLENumbers = []
RLENumbers.append(arrayOfLetters[0])
RLENumbers[0] = "1" + RLENumbers[0]
numbersInARow = 1
while count < 19:
    count = count + 1
    if arrayOfLetters[count] == RLENumbers[len(RLENumbers)-1][1]:
        numbersInARow += 1
        RLENumbers[len(RLENumbers)-1] = str(numbersInARow) + arrayOfLetters[count]
    else:
        RLENumbers.append("1" + arrayOfLetters[count])
        numbersInARow = 1
print(RLENumbers)

