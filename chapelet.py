#!/usr/bin/env python3

import sys
import subprocess
import time
from pathlib import Path

# -----------------------------
# INSTALLATION DES DÉPENDANCES
# -----------------------------

def install(package):
    subprocess.check_call([sys.executable, "-m", "pip", "install", package])

try:
    import pygame
except ImportError:
    print("pygame not found, installing...")
    install("pygame")
    import pygame


# -----------------------------
# INITIALISATION AUDIO
# -----------------------------

pygame.mixer.init()

# Dossier contenant les fichiers audio
sfx = Path("sfx")

if not sfx.exists():
    print(f"Error: {sfx} folder does not exist.")
    sys.exit(1)

# -----------------------------
# FONCTIONS AUDIO
# -----------------------------

def play(file):
    path = sfx / file
    if not path.exists():
        print(f"Missing file : {file}")
        return

    pygame.mixer.music.load(str(path))
    pygame.mixer.music.play()

    while pygame.mixer.music.get_busy():
        time.sleep(0.1)


def profession():
    play("credo.wav")

def notrepere():
    play("pater.wav")

def gloire():
    play("gloria.wav")

def jevoussaluemarie():
    play("ave.wav")


def jvsm3():
    for _ in range(3):
        jevoussaluemarie()


def mystery():
    for _ in range(10):
        jevoussaluemarie()


# -----------------------------
# DÉROULEMENT DU CHAPELET
# -----------------------------

print("✝ Cross sign ✝")

profession()
notrepere()
jvsm3()
gloire()

for i in range(5):
    print(f"Mystère {i + 1}")
    notrepere()
    mystery()
    gloire()

print("🙏 The Lord be with you 🙏")
