# Einfache Rechneranwendung

## Beschreibung
Dieses Projekt implementiert einen einfachen Rechner in Python. Es besteht aus mehreren Modulen, die zusammenarbeiten, um mathematische Ausdrücke zu parsen, Operationen durchzuführen und Ausnahmen zu verwalten. Der Rechner unterstützt grundlegende mathematische Operationen und ist modular aufgebaut.

## Verwendung

1. **Rechner starten:**
   Führe das Hauptprogramm `main.py` aus, um den Rechner zu starten:
   ```bash
   python main.py
   ```

2. **Funktionsweise:**
   - Das Programm erwartet eine mathematische Eingabe im Format "Zahl_1 Operator Zahl_2".
   - Nach Eingabe der Daten wird das Ergebnis der Operation berechnet und ausgegeben.
   - Mögliche Operationen sind Addition, Subtraktion, Multiplikation, Division und Potenzierung. Weitere Operationen können über den Tokenizer hinzugefügt werden.

3. **Fehlerbehandlung:**
   Das Programm beinhaltet eine zentrale Fehlerbehandlung, die ungültige Eingaben erkennt und entsprechende Fehlermeldungen ausgibt.
