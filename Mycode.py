name = input ("Ваше ім'я: ")
surname = input ("Ваша прізвище: ")
rikNarodzhenya = int (input("Ваш рік народження: "))
potochniyRik = int (input("Поточний рік: "))
age = potochniyRik - rikNarodzhenya 
if age >= 18:
    print (name + " " + surname + " ви повнолітній")
else: 
    print (" ви неповнолітній")
