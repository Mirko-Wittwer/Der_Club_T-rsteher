#Deine Aufgabe: Der Club-Türsteher

#Stell dir vor, du programmierst die Software für einen automatischen Türsteher an einem Club. Der Club hat eine strikte "ab 18" Regel.
#Du hast eine Liste mit dem Alter von Gästen, die eintreten möchten:
#gaeste_alter = [25, 17, 30, 16, 21]
#Dein Ziel ist es, ein Programm zu schreiben, das:
#Mit einer for-Schleife durch die Liste gaeste_alter geht, um jeden Gast einzeln zu überprüfen.
#In der Schleife eine if-else-Anweisung verwendet.
#Wenn ein Gast 18 oder älter ist, soll das Programm ausgeben: "Willkommen im Club!"
#Wenn ein Gast jünger als 18 ist, soll es ausgeben: "Du bist leider zu jung."

# Definition der Funktion, die eine Liste von Altersangaben als Eingabe (Parameter) erwartet.
# Eine Funktion bündelt Code, den man wiederverwenden kann.
def pruefe_gaeste_alter(gaeste_liste):
    """
    Diese Funktion iteriert durch eine Liste von Altersangaben.
    Für jedes Alter prüft sie, ob die Person volljährig (18 oder älter) ist
    und gibt eine entsprechende Nachricht auf der Konsole aus.

    Args:
        gaeste_liste: Eine Liste mit ganzen Zahlen, die das Alter der Gäste repräsentieren.
    """
    # Eine for-Schleife, die jeden Eintrag in der 'gaeste_liste' einzeln durchgeht.
    # In jedem Durchlauf wird der aktuelle Wert der Variable 'alter' zugewiesen.
    for alter in gaeste_liste:
        # Eine if-else-Bedingung prüft, ob das aktuelle 'alter' größer oder gleich 18 ist.
        if alter >= 18:
            # Wenn die Bedingung wahr ist (Alter ist 18+), wird diese Nachricht ausgegeben.
            print("Willkommen im Club!")
        else:
            # Wenn die Bedingung falsch ist (Alter ist unter 18), wird diese Nachricht ausgegeben.
            print("Du bist leider zu jung.")

# Erstellung einer Liste mit dem Namen 'gaeste_alter'.
# Eine Liste ist eine geordnete Sammlung von Elementen, hier die Alter der Gäste.
gaeste_alter = [25, 17, 30, 16, 21, 18]

# Aufruf der zuvor definierten Funktion 'pruefe_gaeste_alter'.
# Wir übergeben die Liste 'gaeste_alter' als Argument, damit die Funktion sie verarbeiten kann.

pruefe_gaeste_alter(gaeste_alter)
