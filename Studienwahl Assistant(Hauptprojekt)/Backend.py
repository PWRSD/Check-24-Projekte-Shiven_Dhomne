from flask import Flask, request, jsonify, render_template
import webbrowser
import os

app = Flask(__name__)

# daten
Studienfelder = {
    "Informatik": {"math":3,"people":1,"study":2,"theory":3,"salary":3,"stress":2},
    "Ingenieurwesen": {"math":3,"people":1,"study":2,"theory":3,"salary":3,"stress":3},
    "Wirtschaft / BWL": {"math":2,"people":3,"study":2,"theory":2,"salary":3,"stress":2},
    "Medizin / Lebenswissenschaften": {"math":2,"people":3,"study":3,"theory":2,"salary":2,"stress":3},
    "Rechtswissenschaften": {"math":2,"people":3,"study":2,"theory":3,"salary":3,"stress":2},
    "Kunst / Design": {"math":1,"people":2,"study":2,"theory":2,"salary":2,"stress":1}
}

# texte
Kriterien = {
    "math":"analytischem Denken",
    "people":"Arbeit mit Menschen",
    "study":"langfristigem Lernen",
    "theory":"theoretischem Interesse",
    "salary":"finanziellen Zielen",
    "stress":"Umgang mit Druck"
}

# scoring
def bewertung(a, b):
    d = abs(a - b)
    if d == 0:
        return 3
    if d == 1:
        return 1
    return -2

# begruendung
def begruendung(antworten, scores):
    best = max(scores, key=scores.get)
    passend = []
    kritisch = []

    for k, v in antworten.items():
        diff = abs(v - Studienfelder[best][k])
        if diff == 0:
            passend.append(Kriterien[k])
        elif diff == 2:
            kritisch.append(Kriterien[k])

    text = (
        f"Das Studienfach „{best}“ passt insgesamt sehr gut zu deinem Profil. "
        f"Besonders auffällig ist die Übereinstimmung in den Bereichen {', '.join(passend)}. "
        "Diese Eigenschaften sind entscheidend für den Studienalltag und spätere berufliche Anforderungen. "
    )

    if kritisch:
        text += (
            f"Andere Studienrichtungen schneiden schlechter ab, da dort größere Unterschiede "
            f"in Bezug auf {', '.join(kritisch)} bestehen. "
        )

    text += (
        "Insgesamt spricht dein Antwortverhalten dafür, dass du dich in diesem Studienfeld "
        "sowohl fachlich als auch persönlich langfristig wohlfühlen könntest."
    )

    return text

# route
@app.route("/")
def start():
    return render_template("Frontend.html")

# api
@app.route("/evaluate", methods=["POST"])
def evaluate():
    daten = request.json
    scores = {}

    for feld, profil in Studienfelder.items():
        total = 0
        for k, v in daten.items():
            total += bewertung(v, profil[k])
        scores[feld] = total

    return jsonify({
        "scores": scores,
        "recommended": max(scores, key=scores.get),
        "explanation": begruendung(daten, scores)
    })

if __name__ == "__main__":
    if os.environ.get("WERKZEUG_RUN_MAIN") == "true":
        webbrowser.open("http://127.0.0.1:5000")
    app.run(debug=True)
