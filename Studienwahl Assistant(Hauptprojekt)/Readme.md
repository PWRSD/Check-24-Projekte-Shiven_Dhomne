# Studienauswahl Assistent

*Ein interaktives Webprojekt zur Unterstützung bei der Studienwahl*

## Projektidee

Der **Studienauswahl-Assistent** ist eine Webanwendung, die Schüler:innen dabei hilft, sich selbst besser einzuschätzen und passende Studienrichtungen zu finden.

Das Ziel des Projekts ist **nicht**, den Nutzer:innen eine Entscheidung abzunehmen, sondern sie bei der eigenen Entscheidungsfindung zu unterstützen. Durch gezielte Fragen zu Interessen, Stärken und Erwartungen entsteht am Ende eine nachvollziehbare Empfehlung mit Begründung.



## Motivation

Die Studienwahl ist für viele Schüler:innen eine große Herausforderung. Oft gibt es viele Meinungen von außen, aber wenig strukturierte Möglichkeiten, sich selbst ehrlich zu reflektieren.

Ich wollte ein Tool entwickeln, das:

* verständlich ist
* ehrlich bleibt
* keine „magische“ Entscheidung trifft
* sondern hilft, die eigenen Prioritäten klarer zu sehen

Dieses Projekt ist aus persönlichem Interesse entstanden, da ich mich selbst mit der Frage beschäftige, welcher Studienweg zu mir passt.



## Funktionsweise

Der Assistent führt die Nutzer:innen Schritt für Schritt durch einen Fragebogen.
Dabei geht es unter anderem um:

* Interesse an logischem und analytischem Denken
* Freude an Zusammenarbeit und Kommunikation
* Bereitschaft für ein langes und anspruchsvolles Studium
* Interesse an theoretischen Inhalten
* Bedeutung von Einkommen und Karriere
* Umgang mit Stress und Verantwortung

Auf Basis der Antworten werden verschiedene Studienrichtungen miteinander verglichen und am Ende übersichtlich dargestellt.



## Zentrale Funktionen

* Übersichtlicher Fragebogen mit Fortschrittsanzeige
* Sanfte Animationen zwischen den Fragen
* Zurück- und Weiter-Navigation ohne Verlust der Antworten
* Markierung der ausgewählten Antworten
* Transparente Berechnung der Ergebnisse
* Anzeige der besten drei Studienrichtungen
* Prozentuale Übereinstimmung zur besseren Einordnung
* Verständliche Begründung der Empfehlung



## Technische Umsetzung

Das Projekt wurde bewusst **ohne große Frameworks** umgesetzt, um die Funktionsweise vollständig zu verstehen.

**Frontend**

* HTML
* CSS
* JavaScript (ohne Bibliotheken)

**Backend**

* Python
* Flask

Die Kommunikation zwischen Frontend und Backend erfolgt über JSON-Anfragen.



## Bewertungssystem

Jede Studienrichtung ist anhand fester Kriterien beschrieben.
Die Antworten der Nutzer:innen werden mit diesen Profilen verglichen.

* Übereinstimmungen erhöhen die Bewertung
* kleine Abweichungen wirken sich leicht aus
* große Unterschiede senken die Bewertung deutlich

So entsteht ein **nachvollziehbares und erklärbares Ergebnis**, das keine Blackbox ist.



## Projektstruktur

```
Studienwahl Assistent(Hauptprojekt)
├── Backend.py
├── templates/
│   └── Frontend.html
└── README.md
```

## Was ich durch das Projekt gelernt habe

Durch dieses Projekt habe ich gelernt:

* wie Frontend und Backend zusammenarbeiten
* wie man Entscheidungen in Logik übersetzt
* wie wichtig eine klare Benutzerführung ist
* wie man komplexe Themen einfach erklärt
* wie viel Planung hinter scheinbar einfachen Anwendungen steckt



## Ausblick

In Zukunft könnte das Projekt erweitert werden, zum Beispiel durch:

* genauere Auswertung mehrerer Antworten pro Kriterium
* weitere Studienrichtungen
* grafische Darstellung der persönlichen Profile
* Speicherung von Ergebnissen



## Persönliche Anmerkung

Dieses Projekt steht für meine Neugier, meinen Lernwillen und mein Interesse an Technik und sinnvollen Anwendungen.
Es zeigt, wie ich versuche, reale Probleme mit Software zu lösen auch schon während meiner Schulzeit.




