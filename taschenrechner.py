while True:
    try:
        num1 = int(input("Gib die erste Zahl ein: "))
        break
    except ValueError:
        print("Ups! Das war keine gültige Zahl. Versuche es noch einmal...")

oper = input("Welche Rechenoperation soll durchgeführt werden? (+,-,/.,*): ")

while True:
    try:
        num2 = int(input("Gib die zweite Zahl ein: "))
        break
    except ValueError:
        print("Ups! Das war keine gültige Zahl. Versuche es noch einmal...")

while True:
    if (oper == "+"):
        print("Deine Rechnung:", num1, " + ", num2)
        print("Ergebnis:", num1 + num2)

    elif (oper == "-"):
        print("Deine Rechnung:", num1, " - ", num2)
        print("Ergebnis:", num1 - num2)

    elif (oper == "/"):
        print("Deine Rechnung:", num1, " / ", num2)
        print("Ergebnis:", num1 / num2)

    elif (oper == "*"):
        print("Deine Rechnung:", num1, " * ", num2)
        print("Dein Ergebnis:", num1 * num2)
    else:
        print("Deine Eingaben sind nicht gültig")

    weiterrechnen = input("Willst du weiter rechnen? (Ja/Nein)")

    weiterrechnen = weiterrechnen.lower()
    if (weiterrechnen == ('nein' or 'n')):
        print("Tschüss!")
        break