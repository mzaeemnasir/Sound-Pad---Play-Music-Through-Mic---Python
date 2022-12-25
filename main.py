# Project - Play Sounds/Music Through Python (a Copy of SoundPad used for Games)


# Step 0: Install the Modules
import os

os.system("pip install -r requirements.txt")


# Step 1: Importing Modules
import pygame
import time
import keyboard
from config import sounds
import pyautogui


# Initializing Pygame
pygame.init()

push_to_talk = "v"  # Push to Talk Button

# Getting the microphone device
mic_device = pygame.mixer.get_init()

# Setting the volume to 100%
pygame.mixer.music.set_volume(0.99)


# Step 2: Defining Functions


def play_sound(sound):
    # Pressing and holding key (For Push to Talk Button)
    pyautogui.keyDown(push_to_talk)

    # Loading and Playing the sound
    pygame.mixer.music.load(sound)
    pygame.mixer.music.play()

    # Waiting for the sound to finish playing
    while pygame.mixer.music.get_busy():
        print("playing...")
        pygame.time.Clock().tick(10)

    # Releasing the key (For Push to Talk Button)
    pyautogui.keyUp(push_to_talk)


def stop_sound():
    pygame.mixer.music.stop()


# main Loop

while True:
    # When keyboard key is pressed it will press and hold key (V) after sound is will be released
    if keyboard.is_pressed("F5"):
        play_sound(sounds["muda_muda"])

    if keyboard.is_pressed("F6"):
        play_sound(sounds["nani"])

    if keyboard.is_pressed("F7"):
        play_sound(sounds["slap"])

    if keyboard.is_pressed("F8"):
        play_sound(sounds["oh_no_no"])

    if keyboard.is_pressed("ctrl + q"):
        exit()
