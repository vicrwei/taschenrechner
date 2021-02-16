
# -*- coding: iso-8859-1 -*-

while True:
    num1 = input("Gib die erste Zahl ein: ")
    operator = input("Welche Rechenoperation soll durchgeführt werden? (+,-,/.,*): ")
    num2 = input("Gib die zweite Zahl ein: ")

    num1 = int(num1)
    num2 = int(num2)

    if (operator == "+"):
        print("Deine Rechnung:", num1, " + ", num2)
        print("Ergebnis:", num1 + num2)

    elif (operator == "-"):
        print("Deine Rechnung:", num1, " - ", num2)
        print("Ergebnis:", num1 - num2)

    elif (operator == "/"):
        print("Deine Rechnung:", num1, " / ", num2)
        print("Ergebnis:", num1 / num2)

    elif (operator == "*"):
        print("Deine Rechnung:", num1, " * ", num2)
        print("Dein Ergebnis:", num1 * num2)
    else:
        print("Deine Eingaben sind nicht gültig")

    weiterrechnen = input("Willst du weiter rechnen? (Ja/Nein)")

    if weiterrechnen == 'nein':
        break