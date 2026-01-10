import gymnasium as gym
import numpy as np
import random
import tkinter as tk
import time
from collections import deque
import os

# CONFIG
CELL = 100
MARGIN = 25
GRID = 5
CANVAS_W = GRID * CELL + 2 * MARGIN
CANVAS_H = GRID * CELL + 2 * MARGIN

Q_FILE = "q_table.npy"
TRAIN_EPISODES = 10000

ALPHA = 0.1       # Lernrate
GAMMA = 0.75      # Zukunftsgewichtung
EPSILON = 0.07    # Zufällige Exploration
MAX_TRAIN_ITERS = 300

# TAXI ENV
env = gym.make("Taxi-v3")

# GUI
root = tk.Tk()
root.title("Taxi Problem")
root.configure(bg="#ECEFF1")

canvas = tk.Canvas(root, width=CANVAS_W, height=CANVAS_H, bg="#FAFAFA", highlightthickness=0)
canvas.pack(pady=10)

info = tk.Label(root, text="Bereit", bg="#263238", fg="white", font=("Segoe UI", 11), padx=10, pady=6)
info.pack(fill="x", pady=(0, 10))

landmarks = [(0,0),(0,4),(4,0),(4,3)]  # R, G, Y, B

# Decode Taxi state
def decode(state):
    dest = state % 4
    state //= 4
    pass_loc = state % 5
    state //= 5
    col = state % 5
    row = state // 5
    return row, col, pass_loc, dest

# Anti-Oszillation für Q-Action
def smart_argmax(q_values):
    max_q = np.max(q_values)
    actions = np.where(q_values == max_q)[0]
    return int(np.random.choice(actions))

# Wände
def generate_random_walls(v_count=3, h_count=2):
    walls = set()
    while sum(1 for w in walls if w[0] == "v") < v_count:
        walls.add(("v", random.randint(0, GRID-1), random.randint(0, GRID-2)))
    while sum(1 for w in walls if w[0] == "h") < h_count:
        walls.add(("h", random.randint(0, GRID-2), random.randint(0, GRID-1)))
    return list(walls)

def draw_walls():
    for typ, r, c in walls:
        if typ == "v":
            x = MARGIN + (c + 1) * CELL
            y1 = MARGIN + r * CELL
            y2 = MARGIN + (r + 1) * CELL
            canvas.create_line(x, y1, x, y2, width=6, fill="#37474F")
        else:
            y = MARGIN + (r + 1) * CELL
            x1 = MARGIN + c * CELL
            x2 = MARGIN + (c + 1) * CELL
            canvas.create_line(x1, y, x2, y, width=6, fill="#37474F")

def movement_blocked(row, col, action):
    if action == 0:
        return row >= GRID-1 or ("h", row, col) in walls
    if action == 1:
        return row <= 0 or ("h", row-1, col) in walls
    if action == 2:
        return col >= GRID-1 or ("v", row, col) in walls
    if action == 3:
        return col <= 0 or ("v", row, col-1) in walls
    return False

# Spielfeld zeichnen
def draw(state):
    canvas.delete("all")
    for i in range(GRID):
        for j in range(GRID):
            x1 = MARGIN + j * CELL
            y1 = MARGIN + i * CELL
            canvas.create_rectangle(x1, y1, x1 + CELL, y1 + CELL, outline="#B0BEC5")
    draw_walls()

    row, col, p, d = decode(state)

    # Zielmarkierungen
    for i, (r, c) in enumerate(landmarks):
        canvas.create_text(MARGIN + c * CELL + 12, MARGIN + r * CELL + 10,
                           text="R G Y B".split()[i], font=("Segoe UI", 11, "bold"), fill="#455A64", anchor="nw")

    # Ziel-Kreis
    dr, dc = landmarks[d]
    cx = MARGIN + dc * CELL + CELL / 2
    cy = MARGIN + dr * CELL + CELL / 2
    rr = CELL * 0.3
    canvas.create_oval(cx-rr, cy-rr, cx+rr, cy+rr, outline="#2E7D32", width=3)

    # Passagier
    if p != 4:
        pr, pc = landmarks[p]
        canvas.create_text(MARGIN + pc * CELL + CELL / 2,
                           MARGIN + pr * CELL + CELL * 0.7,
                           text="P", font=("Segoe UI", 14, "bold"), fill="#D32F2F")

    # Taxi
    tx1 = MARGIN + col * CELL + CELL * 0.18
    ty1 = MARGIN + row * CELL + CELL * 0.18
    tx2 = tx1 + CELL * 0.64
    ty2 = ty1 + CELL * 0.64
    canvas.create_rectangle(tx1, ty1, tx2, ty2, fill="#FFD600", outline="#212121", width=2)
    canvas.create_text((tx1+tx2)/2, (ty1+ty2)/2, text="TAXI", font=("Segoe UI", 10, "bold"))

# Q-Learning Training
def train_q():
    Q = np.zeros((env.observation_space.n, env.action_space.n))
    for ep in range(TRAIN_EPISODES):
        state, _ = env.reset()
        done = False
        iters = 0
        while not done and iters < MAX_TRAIN_ITERS:
            action = env.action_space.sample() if random.random() < EPSILON else smart_argmax(Q[state])
            row, col, _, _ = decode(state)

            if action < 4 and movement_blocked(row, col, action):
                next_state = state
                reward = -10
            else:
                next_state, reward, term, trunc, _ = env.step(action)
                done = term or trunc

            Q[state, action] += ALPHA * (reward + GAMMA * np.max(Q[next_state]) - Q[state, action])
            state = next_state
            iters += 1

        if (ep + 1) % 1000 == 0:
            info.config(text=f"Training: Episode {ep+1}/{TRAIN_EPISODES}")
            root.update()

    np.save(Q_FILE, Q)
    info.config(text="Training abgeschlossen. Q-Tabelle gespeichert.")
    return Q

# Initialisierung
walls = generate_random_walls()
Q = np.load(Q_FILE) if os.path.exists(Q_FILE) else train_q()

# Spielen (Episode)
def play():
    state, _ = env.reset()
    pos_hist = deque(maxlen=6)
    total_reward = 0
    steps = 0

    for _ in range(500):
        draw(state)
        root.update()
        time.sleep(0.1)

        action = smart_argmax(Q[state])
        row, col, _, _ = decode(state)

        if action < 4 and movement_blocked(row, col, action):
            info.config(text="Kollision mit Wand — bitte Reset oder Retrain.")
            return

        state, reward, term, trunc, _ = env.step(action)
        total_reward += reward
        steps += 1

        r, c, _, _ = decode(state)
        pos_hist.append((r, c))
        if len(pos_hist) == pos_hist.maxlen and len(set(pos_hist)) == 2:
            info.config(text="Agent steckt fest — bitte Reset oder Retrain.")
            return

        if term or trunc:
            break

    info.config(text=f"Episode beendet — Schritte: {steps} | Reward: {total_reward}")

# Buttons
btn = dict(font=("Segoe UI", 11), padx=12, pady=6)
tk.Button(root, text="▶ Start", command=play, bg="#2E7D32", fg="white", **btn).pack(pady=4)
tk.Button(root, text="⟳ Neue Wände(Reset)", command=lambda: globals().update(walls=generate_random_walls()), **btn).pack()
tk.Button(root, text="⟳ Q-Tabelle retrainen(Retrain)", command=lambda: globals().update(Q=train_q()), **btn).pack(pady=(0,10))

root.mainloop()
