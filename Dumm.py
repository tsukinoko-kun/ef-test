import sys
import random
from PySide6.QtWidgets import (QApplication, QMainWindow, QWidget, QVBoxLayout,
                               QHBoxLayout, QLabel, QPushButton, QLineEdit,
                               QFrame)
from PySide6.QtCore import Qt
from PySide6.QtGui import QFont, QClipboard

# Listen mit Beleidigungen, humorvollen Sprüchen
adjektive = ["dümmste", "peinlichste", "hinterfotzigste", "dämlichste", "schwächste", "nutzloseste", "rückgradloseste", "unterbelichteste", "erbärmlichste", "lächerlichste", "hassenswerteste", "unschönste", "uninteressanteste", "talentloseste", "gesichtsloseste"]
nomen = ["Penner", "Wichser", "Arsch", "Bastard", "Idiot", "Gauner", "Lutscher", "Hornochse", "Schwanz", "Zuhälter", "Loser", "Sack", "Depp", "Vollidiot", "Lauch", "Klappspaten", "Honk", "Pfeife", "Dulli", "Knochen", "Trottel", "Schmock", "Vollpfosten", "Dödel"]
nomen2 = ["der Welt", "der Stadt", "des Universums", "deines Landes", "deiner Klasse", "deiner Firma", "deiner Familie", "deiner Freunde", "deiner Klicke", "deiner Gegend", "des Landkreises", "des ganzen Multiversums", "aller Zeiten", "aller Religionen", "aller Kulturen"]
dead = ["stirb endlich!", "hau ab!!!", "mach dass du Land gewinnst!", "Ich wünschte du wärst tot!", "verreck an Krebs", "beiß ins Gras!!", "verschwinde!!!", "stirb an Aids!!!", "verreck einfach!!!", "geh Sterben!", "leg dich auf die Schienen!", "fick dich ins Knie!"]
fuck = ["fick ich deine Frau", "piss ich auf dein Grab", "klau ich dein Auto", "rauche ich eine Havanna", "zerkratze ich dein Auto", "kacke ich auf dein Grab", "fick ich deine Schwester", "fick ich deine Mama", "fick ich deinen Hamster", "fick ich deine Goldfische", "fick ich deine Nachbarn"]
dumm = ["dummer", "nerviger", "stinkender", "dämlicher", "peinlicher", "nutzloser", "schwacher", "rückgradloser", "hinterhältiger", "dreister", "frecher", "anmaßender"]

# Dark Theme Stylesheet
DARK_STYLE = """
QMainWindow {
    background-color: #1a1a2e;
}
QLabel {
    color: #e0e0e0;
}
QLineEdit {
    background-color: #16213e;
    color: #e94560;
    border: 2px solid #0f3460;
    border-radius: 8px;
    padding: 12px;
    font-size: 16px;
    selection-background-color: #e94560;
}
QPushButton {
    border-radius: 8px;
    padding: 10px 24px;
    font-size: 14px;
    font-weight: bold;
}
QPushButton#generateBtn {
    background-color: #e94560;
    color: white;
}
QPushButton#generateBtn:hover {
    background-color: #c73650;
}
QPushButton#generateBtn:pressed {
    background-color: #a02840;
}
QPushButton#copyBtn {
    background-color: #0f3460;
    color: #e0e0e0;
}
QPushButton#copyBtn:hover {
    background-color: #1a4a7a;
}
QFrame#counterFrame {
    background-color: #16213e;
    border-radius: 6px;
}
"""

class SpruchGenerator(QMainWindow):
    def __init__(self):
        super().__init__()
        self.counter = 0
        self.setWindowTitle("Spaß-Spruch Generator")
        self.setMinimumSize(1500, 250)

        central = QWidget()
        self.setCentralWidget(central)
        layout = QVBoxLayout(central)
        layout.setSpacing(12)
        layout.setContentsMargins(30, 20, 30, 20)

        # Titel
        titel = QLabel("Klicke für eine zufällige Beleidigung:")
        titel.setFont(QFont("Arial", 14))
        titel.setAlignment(Qt.AlignCenter)
        layout.addWidget(titel)

        # Buttons nebeneinander
        btn_layout = QHBoxLayout()
        self.btn_generate = QPushButton("Satz generieren!")
        self.btn_generate.setObjectName("generateBtn")
        self.btn_generate.setFixedHeight(45)
        self.btn_generate.clicked.connect(self.generate_phrase)
        btn_layout.addWidget(self.btn_generate)

        self.btn_copy = QPushButton("Kopieren")
        self.btn_copy.setObjectName("copyBtn")
        self.btn_copy.setFixedHeight(45)
        self.btn_copy.clicked.connect(self.copy_to_clipboard)
        btn_layout.addWidget(self.btn_copy)
        layout.addLayout(btn_layout)

        # Output-Feld
        self.output = QLineEdit()
        self.output.setReadOnly(True)
        self.output.setAlignment(Qt.AlignCenter)
        self.output.setFont(QFont("Arial", 15))
        self.output.setMinimumHeight(50)
        layout.addWidget(self.output)

        # Zähler unten
        self.counter_label = QLabel("Generiert: 0")
        self.counter_label.setFont(QFont("Arial", 9))
        self.counter_label.setStyleSheet("color: #888;")
        self.counter_label.setAlignment(Qt.AlignCenter)
        layout.addWidget(self.counter_label)

    def generate_phrase(self):
        self.counter += 1
        adj = random.choice(adjektive)
        nom = random.choice(nomen)
        nom2 = random.choice(nomen2)
        dead_choice = random.choice(dead)
        fuck_choice = random.choice(fuck)
        dumb = random.choice(dumm)
        if random.randint(0, 6) == 0:
            result = f"Du bist der {adj} {nom} {nom2}, den ich kenne! {dead_choice} und wenn du weg bist, dann {fuck_choice}"
        elif random.randint(0, 6) == 1:
            result = f"Du drecks {nom} du bist der {adj} {nom2}, den ich je gesehen habe! {dead_choice} und falls du {dumb} {nom} mal stirbst oder weg bist, dann {fuck_choice}"
        elif random.randint(0, 6) == 2:
            result = f"Du {nom}, du bist der {adj} {nom2} am besten {dead_choice} du {nom} und wenn du weg bist, dann {fuck_choice} du {dumb} {nom}"
        elif random.randint(0, 6) == 3:
            result = f"Hey du {nom}, der {adj} {nom} {nom2} {dead_choice} du {nom} falls du weg bist, dann {fuck_choice} du {dumb} {nom}"
        elif random.randint(0, 6) == 4:
            result = f"{dead_choice} du {nom}, du bist der {adj} {nom} {nom2} und wenn du weg bist, dann {fuck_choice} du {dumb} {nom}"
        elif random.randint(0, 6) == 5:
            result = f"Bitte {dead_choice} du {dumb} {nom}, du bist der {adj} {nom} {nom2} falls du Tod sein solltest, dann {fuck_choice} du {dumb} {nom}"
        else:
            result = f"Du {dumb} {nom}, was denkst du wer du bist, {dead_choice} Wenn du weg bist, dann {fuck_choice} du {nom}"
        self.output.setText(result)
        self.counter_label.setText(f"Generiert: {self.counter}")

    def copy_to_clipboard(self):
        text = self.output.text()
        if text:
            clipboard = QApplication.clipboard()
            clipboard.setText(text)
            self.counter_label.setText(f"Generiert: {self.counter} | Kopiert!")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    app.setStyleSheet(DARK_STYLE)
    window = SpruchGenerator()
    window.show()
    sys.exit(app.exec())
