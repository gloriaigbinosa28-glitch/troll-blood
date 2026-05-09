import tkinter as tk
import random

root = tk.Tk()
root.title("System Glitch Simulator")
root.geometry("600x400")
root.config(bg="black")

canvas = tk.Canvas(root, bg="black", highlightthickness=0)
canvas.pack(fill="both", expand=True)

def drip():
    x = random.randint(0, 600)
    length = random.randint(20, 120)

    canvas.create_line(x, 0, x, length, fill="red", width=3)

    root.after(100, drip)

def text_glitch():
    msgs = ["SYSTEM ERROR", "GLITCH DETECTED", "MEMORY CORRUPTION"]
    canvas.create_text(
        random.randint(100, 500),
        random.randint(100, 300),
        text=random.choice(msgs),
        fill="red",
        font=("Arial", 14)
    )
    root.after(500, text_glitch)

drip()
text_glitch()

root.mainloop()