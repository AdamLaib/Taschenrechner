# Im Hauptprogramm erzeugen Sie ein Tokenizer- und ein Calculator-Objekt.
# Führen Sie dann den Ablauf
# - Wert einlesen
# - Operation erzeugen
# - Berechnung ausführen
# durch.
# Hier müssen alle auftretenden Exceptions zentral verwaltet werden.
from tokenizer import Tokenizer
from calculator import Calculator
from exceptions import *


def main():
    token = Tokenizer()
    token.add_operation('^')
    calc = Calculator(token)
    try:
        calc.read_input()
        calc.create_concrete_op()
        calc.calculate()

    except NumberFormatException as nerr:
        print(nerr)
    except OperationException as oerr:
        print(oerr)


if __name__ == '__main__':
    main()
