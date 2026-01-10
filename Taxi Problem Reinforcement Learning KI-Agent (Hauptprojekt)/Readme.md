# Reinforcement Learning – Taxi-Problem mit grafischer Oberfläche

*Ein eigenständig entwickeltes Lernprojekt zu Künstlicher Intelligenz*

## Projektübersicht

Dieses Projekt ist meine eigene Umsetzung des bekannten **Taxi-Problems** aus dem Bereich **Reinforcement Learning**.
Ein autonomer Agent (das Taxi) lernt dabei, einen Passagier aufzunehmen und sicher zu seinem Ziel zu bringen.

Das Besondere an meinem Projekt ist, dass das Lernverhalten **nicht nur im Code**, sondern auch **visuell über eine grafische Oberfläche** sichtbar gemacht wird. Dadurch wird deutlich, wie sich ein lernender Algorithmus verhält – inklusive Fehlern und Verbesserungen.



## Motivation

Mich interessiert besonders, **wie Maschinen durch Erfahrung lernen** und nicht durch feste Regeln gesteuert werden.
Das Taxi-Problem ist dafür ein sehr gutes Beispiel, weil man Erfolge und Fehlentscheidungen direkt beobachten kann.

Dieses Projekt habe ich entwickelt, um:

* Reinforcement Learning praktisch zu verstehen
* mathematisches Denken mit Programmierung zu verbinden
* zu sehen, wie sich Lernparameter auf das Verhalten eines Systems auswirken



## Funktionsweise

Der Agent bewegt sich in einem 5×5-Gitter und hat folgende Aufgaben:

* den Passagier finden
* ihn aufnehmen
* Hindernisse (Wände) vermeiden
* den Passagier am richtigen Ziel absetzen

Der Lernprozess basiert auf **Q-Learning**.
Dabei merkt sich der Agent für jeden Zustand, welche Aktion langfristig den besten Nutzen bringt.



## Grafische Oberfläche

Zur besseren Nachvollziehbarkeit habe ich eine **eigene grafische Oberfläche mit Tkinter** umgesetzt.

Dargestellt werden:

* das Spielfeld
* das Taxi
* der Passagier
* das Ziel
* zufällig generierte Wände

Zusätzlich zeigt eine Statusleiste an, was gerade passiert (z. B. Training, Kollision, Abschluss einer Episode).



## Training und Verhalten des Agenten

Beim Start wird geprüft, ob bereits eine gespeicherte **Q-Tabelle** existiert.
Falls nicht, wird der Agent automatisch neu trainiert.

Wichtig zu wissen:

* Da das Lernen teilweise zufällig ist, kann es vorkommen, dass der Agent **ungünstige Strategien lernt**
* In solchen Fällen kann das Taxi häufiger gegen Wände fahren oder sich festfahren

**Empfehlung:**
Wenn das Taxi:

* häufig crasht
* sich im Kreis bewegt
* oder das Ziel nicht zuverlässig erreicht

sollte die **Q-Tabelle mehrfach neu trainiert (Retrain)** werden.
Nach einigen Trainingsdurchläufen verbessert sich das Verhalten in der Regel deutlich.



## Steuerung

Über die Buttons in der Oberfläche kann man:

* ▶ **Start** – eine Episode mit dem aktuell gelernten Verhalten starten
* ⟳ **Neue Wände (Reset)** – neue Hindernisse erzeugen
* ⟳ **Q-Tabelle retrainen (Retrain)** – den Lernprozess neu starten

So kann man direkt beobachten, wie sich erneutes Training auf das Verhalten des Agenten auswirkt.



## Technische Umsetzung

**Programmiersprache:**

* Python

**Bibliotheken:**

* gymnasium (Taxi-v3 Umgebung)
* numpy
* tkinter

**Konzepte:**

* Reinforcement Learning
* Q-Learning
* Exploration vs. Exploitation
* Zustands-Aktions-Bewertung
* grafische Visualisierung von Algorithmen



## Was ich durch das Projekt gelernt habe

Durch dieses Projekt habe ich verstanden:

* dass lernende Systeme nicht sofort perfekt funktionieren
* wie wichtig Training, Parameter und Wiederholung sind
* wie Theorie aus dem Unterricht praktisch umgesetzt werden kann
* wie man komplexe Algorithmen verständlich visualisiert

## Persönliche Anmerkung

Dieses Projekt ist bewusst **nicht perfekt**, sondern realistisch.
Es zeigt, dass Lernen – sowohl bei Menschen als auch bei Maschinen – ein Prozess ist, der Zeit, Geduld und Analyse erfordert.

Genau diese Herangehensweise möchte ich auch in Zukunft weiterentwickeln.


