import pygame
import tkinter as tk
from tkinter import filedialog

pygame.mixer.init()

def choose_music():
    path = filedialog.askopenfilename(
        title="Select a music file",
        filetypes=[("MP3 Files", "*.mp3"), ("All Files", "*.*")]
    )
    if path:
        label_music.config(text=f"Playing: {path.split('/')[-1]}")
        pygame.mixer.music.load(path)
        pygame.mixer.music.play()

def pause():
    pygame.mixer.music.pause()

def resume():
    pygame.mixer.music.unpause()

def stop():
    pygame.mixer.music.stop()
    label_music.config(text="No music playing")

window = tk.Tk()
window.title("MP3 Music Player")
window.geometry("320x250")
window.configure(bg="#202020")

tk.Label(window, text="MP3 Player", fg="white", bg="#202020", font=("Arial", 14, "bold")).pack(pady=10)

label_music = tk.Label(window, text="No music playing", fg="white", bg="#202020")
label_music.pack(pady=10)

btn_choose = tk.Button(window, text="Choose Music", command=choose_music, width=20, bg="#404040", fg="white")
btn_choose.pack(pady=5)

btn_pause = tk.Button(window, text="Pause", command=pause, width=20, bg="#404040", fg="white")
btn_pause.pack(pady=5)

btn_resume = tk.Button(window, text="Resume", command=resume, width=20, bg="#404040", fg="white")
btn_resume.pack(pady=5)

btn_stop = tk.Button(window, text="Stop", command=stop, width=20, bg="#404040", fg="white")
btn_stop.pack(pady=5)

window.mainloop()
