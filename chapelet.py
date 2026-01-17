#!/usr/bin/env python3

import argparse
import time
from pathlib import Path
import pygame

parser = argparse.ArgumentParser(
    description="Rosary recitation"
)

parser.add_argument(
    "-full",
    action="store_true",
    help="Pray the full rosary"
)

parser.add_argument(
    "-classic",
    action="store_true",
    help="Classic rosary (Joyful, Sorrowful, Glorious only)"
)

args = parser.parse_args()

pygame.mixer.init()

BASE_DIR = Path(__file__).parent
SFX_DIR = BASE_DIR / "sfx"

def play(file):
    path = SFX_DIR / file
    if not path.exists():
        print(f"Missing audio file: {file}")
        return

    pygame.mixer.music.load(str(path))
    pygame.mixer.music.play()

    while pygame.mixer.music.get_busy():
        time.sleep(0.1)

def profession():
    play("profession.wav")

def notrepere():
    play("notrepere.wav")

def gloire():
    play("gloire.wav")

def jevoussaluemarie():
    play("jvsm.wav")

def jvsm3():
    for _ in range(3):
        jevoussaluemarie()

def decade():
    for _ in range(10):
        jevoussaluemarie()

JOYFUL = [
    "The Annunciation",
    "The Visitation",
    "The Nativity",
    "The Presentation",
    "The Finding in the Temple",
]

SORROWFUL = [
    "The Agony in the Garden",
    "The Scourging at the Pillar",
    "The Crowning with Thorns",
    "The Carrying of the Cross",
    "The Crucifixion",
]

GLORIOUS = [
    "The Resurrection",
    "The Ascension",
    "The Descent of the Holy Spirit",
    "The Assumption",
    "The Coronation of Mary",
]

LUMINOUS = [
    "The Baptism of Christ",
    "The Wedding at Cana",
    "The Proclamation of the Kingdom",
    "The Transfiguration",
    "The Institution of the Eucharist",
]

def chaplet_with_mysteries(mysteries, chaplet_name):
    print(f"\n📿 {chaplet_name} Mysteries 📿\n")

    profession()
    notrepere()
    jvsm3()
    gloire()

    for i, mystery_name in enumerate(mysteries, start=1):
        print(f"— Mystery {i}: {mystery_name}")
        notrepere()
        decade()
        gloire()

if __name__ == "__main__":

    if args.full:
        if args.classic:
            print("🙏 Classic Full Rosary (3 Chaplets)\n")
            chaplet_with_mysteries(JOYFUL, "Joyful")
            chaplet_with_mysteries(SORROWFUL, "Sorrowful")
            chaplet_with_mysteries(GLORIOUS, "Glorious")
        else:
            print("🙏 Full Rosary (4 Chaplets)\n")
            chaplet_with_mysteries(JOYFUL, "Joyful")
            chaplet_with_mysteries(SORROWFUL, "Sorrowful")
            chaplet_with_mysteries(GLORIOUS, "Glorious")
            chaplet_with_mysteries(LUMINOUS, "Luminous")
    else:
        print("🙏 Single Chaplet\n")
        chaplet_with_mysteries(JOYFUL, "Joyful")

    print("\n✝ End of prayer ✝\n")
