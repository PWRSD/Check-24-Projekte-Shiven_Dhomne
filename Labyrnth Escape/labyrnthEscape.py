import arcade

# Fenstergröße und Titel
WIDTH = 500
HEIGHT = 500
TITLE = "Labyrinth"

class StartView(arcade.View):
    def on_show(self):
        arcade.set_background_color(arcade.color.SKY_BLUE)

    def on_draw(self):
        self.clear()
        arcade.draw_text("Welcome to Labyrinth!", WIDTH // 2, HEIGHT // 2 + 40,
                         arcade.color.RED, 24, anchor_x="center")
        arcade.draw_text(" Press SPACE to Start!", WIDTH // 2, HEIGHT // 2 - 10,
                         arcade.color.DARK_BLUE, 30, anchor_x="center")

    def on_key_press(self, symbol, modifiers):
        if symbol == arcade.key.SPACE:
            game_view = GameView()
            self.window.show_view(game_view)

class GameView(arcade.View):
    def __init__(self):
        super().__init__()

        # Spieler (roter Kreis)
        self.circle = arcade.SpriteCircle(20, arcade.color.RED)
        self.circle.center_x = 85
        self.circle.center_y = 25
        self.circle_speed = 150
        self.directions = {'left': False, 'right': False, "up": False, "down": False}

        arcade.set_background_color(arcade.color.DESERT_SAND)

        # Listen für Blöcke und Münzen
        self.block_liste = arcade.SpriteList()
        self.coins_liste = arcade.SpriteList()

        # Linke Wand mit Startblock
        for i in range(10):
            block = arcade.Sprite("startblock.png" if i == 0 else "normalblock.png")
            block.center_x = 25
            block.center_y = 25 + i * 50
            block.type = "deadly"
            self.block_liste.append(block)

        # Untere Wand (außer die ersten 3 Positionen)
        for i in range(10):
            if i == 2 or i == 1 or i == 0:
                block = arcade.Sprite()
            else:
                block = arcade.Sprite("normalblock.png")
                block.center_x = i * 50
                block.center_y = 25
                block.type = "deadly"
                self.block_liste.append(block)

        # Obere Wand
        for i in range(10):
            block = arcade.Sprite("normalblock.png")
            block.center_x = i * 50
            block.center_y = 475
            block.type = "deadly"
            self.block_liste.append(block)

        # Rechte Wand mit Ziel- und Todesblöcken
        for i in range(10):
            if i == 4 or i == 5:
                block = arcade.Sprite("normalblock.png")
                block.center_x = 524
                block.center_y = 25 + i * 50
                block.type = "end"  # Zielblöcke
                self.block_liste.append(block)
            elif i == 3 or i == 6:
                block = arcade.Sprite("Ende.png")
                block.center_x = 475
                block.center_y = 25 + i * 50
                block.type = "end"
                self.block_liste.append(block)
            else:
                block = arcade.Sprite("normalblock.png")
                block.center_x = 475
                block.center_y = 25 + i * 50
                block.type = "deadly"  # tödliche Blöcke
                self.block_liste.append(block)

        # Zusätzliche Blöcke im Spielfeld
        positions = [
            (150, 250), (250, 150), (150, 150), 
            (350, 250), (350, 150), (150, 350),
            (250, 350), (350, 350), (75, -23),
            (100, -23), (250,100), (100,250), 
            (250, 150), (250,350),(400, 250),(250,400)
        ]
        for pos in positions:
            block = arcade.Sprite("normalblock.png")
            block.center_x, block.center_y = pos
            block.type = "deadly"
            self.block_liste.append(block)

        # Münzen platzieren
        self.coins_positions = [
            (85, 410), (250, 247), (415, 410), (415, 85), 
            (85, 85),(150, 410),(350, 410), (350, 85), 
            (150, 85), (100, 100), (400, 400), (400, 100),
            (100, 400), (200, 200), (300, 300), (200, 300),
            (300, 200),(250, 250), (100, 400), (100, 100), 
    
        ]
        for pos in self.coins_positions:
            coin = arcade.Sprite("coin.png")
            coin.center_x, coin.center_y = pos
            self.coins_liste.append(coin)

        self.coins_count = 0
        self.coins_Text = arcade.Text(f"Coins collected: {self.coins_count}", 5, 480,arcade.color.YELLOW, 15)

        # Timer
        self.time_elapsed = 0
        self.timer_text = arcade.Text("Time: 00:00", 5, 460, arcade.color.YELLOW, 15)

        # Musik starten
        self.music = arcade.Sound("Main music.mp3")
        self.music_player = self.music.play(volume=0.5)

        # Sound für Münzen
        self.sound = arcade.Sound(":resources:/sounds/coin1.wav")

    def on_draw(self):
        self.clear()
        self.block_liste.draw()
        self.coins_liste.draw()
        arcade.draw_sprite(self.circle)
        self.coins_Text.draw()
        self.timer_text.draw()

    def on_key_press(self, symbol, modifiers):
        if symbol == arcade.key.LEFT:
            self.directions['left'] = True
        if symbol == arcade.key.RIGHT:
            self.directions['right'] = True
        if symbol == arcade.key.UP:
            self.directions['up'] = True
        if symbol == arcade.key.DOWN:
            self.directions['down'] = True

    def on_key_release(self, symbol, modifiers):
        if symbol == arcade.key.LEFT:
            self.directions['left'] = False
        if symbol == arcade.key.RIGHT:
            self.directions['right'] = False
        if symbol == arcade.key.UP:
            self.directions['up'] = False
        if symbol == arcade.key.DOWN:
            self.directions['down'] = False

    def on_update(self, delta_time):
        # Timer aktualisieren
        self.time_elapsed += delta_time
        minutes = int(self.time_elapsed) // 60
        seconds = int(self.time_elapsed) % 60
        self.timer_text.text = f"Time: {minutes:02}:{seconds:02}"

        # Bewegung berechnen
        dx = dy = 0
        if self.directions['left']:
            dx -= self.circle_speed * delta_time
        if self.directions['right']:
            dx += self.circle_speed * delta_time
        if self.directions['up']:
            dy += self.circle_speed * delta_time
        if self.directions['down']:
            dy -= self.circle_speed * delta_time

        self.circle.center_x += dx
        self.circle.center_y += dy

        # Kollision mit Blöcken prüfen
        # Kollision mit Blöcken prüfen
        blocks_hit = arcade.check_for_collision_with_list(self.circle, self.block_liste)
        for block in blocks_hit:
            # Reaktion je nach Typ des Blocks (mit hasattr sicherstellen, dass "type" existiert)
            if hasattr(block, "type"):
                if block.type == "end":
                    if self.music_player:
                        self.music_player.pause()  # sicher Musik stoppen (play() liefert keinen echten Player ohne weiteres)
                    end_view = EndView(self.time_elapsed, self.coins_count)
                    self.window.show_view(end_view)
                    return  # beende Funktion, damit nicht mehr weiter geprüft wird
                elif block.type == "deadly":
                    if self.music_player:
                        self.music_player.pause()
                    game_over = GameOverView()
                    self.window.show_view(game_over)
                    return



        # Kollision mit Münzen prüfen
        coins_hit = arcade.check_for_collision_with_list(self.circle, self.coins_liste)
        for coin in coins_hit:
            self.coins_liste.remove(coin)
            arcade.play_sound(self.sound, volume=0.4)
            self.coins_count += 1
            self.coins_Text.text = f"coins count: {self.coins_count}"

class EndView(arcade.View):
    def __init__(self, time_elapsed,coins_collected):
        super().__init__()
        self.time_elapsed = time_elapsed
        self.coins_collected = coins_collected

    def on_show(self):
        arcade.set_background_color(arcade.color.LIGHT_GREEN)

    def on_draw(self):
        self.clear()
        minutes = int(self.time_elapsed) // 60
        seconds = int(self.time_elapsed) % 60
        arcade.draw_text("You Won!", WIDTH // 2, HEIGHT // 2 + 60,
                         arcade.color.BLACK, 32, anchor_x="center")
        arcade.draw_text(f"Time: {minutes:02}:{seconds:02}", WIDTH // 2, HEIGHT // 2 + 20,
                         arcade.color.BLACK, 20, anchor_x="center")
        arcade.draw_text(f"Coins collected: {self.coins_collected}", WIDTH // 2, HEIGHT // 2 - 20,
                         arcade.color.RED, 20, anchor_x="center")
        arcade.draw_text("Press ENTER to Restart", WIDTH // 2, HEIGHT // 2 - 60,
                         arcade.color.BLUE, 18, anchor_x="center")

    def on_key_press(self, symbol, modifiers):
        if symbol == arcade.key.ENTER:
            start_view = StartView()
            self.window.show_view(start_view)

class GameOverView(arcade.View):
    def on_show(self):
        arcade.set_background_color(arcade.color.BLACK)

    def on_draw(self):
        self.clear()
        arcade.draw_text("Game over!", WIDTH // 2, HEIGHT // 2 + 10,
                         arcade.color.RED, 36, anchor_x="center")
        arcade.draw_text("Press ENTER to try Again", WIDTH // 2, HEIGHT // 2 - 30,
                         arcade.color.WHITE, 18, anchor_x="center")

    def on_key_press(self, symbol, modifiers):
        if symbol == arcade.key.ENTER:
            start_view = StartView()
            self.window.show_view(start_view)

# Starte das Spiel nur, wenn diese Datei direkt ausgeführt wird
if __name__ == "__main__":
    window = arcade.Window(WIDTH, HEIGHT, TITLE)
    start_view = StartView()
    window.show_view(start_view)
    arcade.run()


