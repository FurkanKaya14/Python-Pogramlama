#pyautogui
import pyautogui
pyautogui.moveTo(500, 500, duration=2, tween=pyautogui.easeInOutQuad)
pyautogui.moveTo(1000, 1000, duration=2,tween=pyautogui.easeInCirc)
pyautogui.moveTo(50, 50, duration=2, tween=pyautogui.easeInBounce)
pyautogui.moveTo(500, 500, duration=2, tween=pyautogui.easeOutElastic)

#cozunurluk
screenWidth, screenHeight = pyautogui.size()
print("Ekran Çözünürlüğü :", screenWidth, screenHeight)

#fare
currentMouseX, currentMouseY = pyautogui.position()
print(currentMouseX, currentMouseY)

#kare
pyautogui.moveTo(100, 250, duration=2,
                 tween=pyautogui.easeInOutQuad)

distance = 200
while distance > 0:
        pyautogui.drag(distance, 0, duration=0.5)   # move right
        distance -= 5
        pyautogui.drag(0, distance, duration=0.5)   # move down
        pyautogui.drag(-distance, 0, duration=0.5)  # move left
        distance -= 5
        pyautogui.drag(0, -distance, duration=0.5)  # move up"""

#tkinter
from tkinter import *
window = Tk()
window.title("Merhaba Python GUI")
lbl = Label(window, text="Merhaba")
lbl2 = Label(window, text="Merhaba", font=("Arial Bold", 50))
lbl.grid(column=0, row=0)
lbl2.grid(column=1, row=0)
window.geometry('500x400')
btn = Button(window, text="Tıkla")
btn.grid(column=1, row=1)
def tiklandi():
    pyautogui.moveTo(100, 100, duration=1,tween=pyautogui.easeInOutQuad)
btn2 = Button(window, text="Tıkla Renkli", bg="orange", fg="red", width=10, height=10, command=tiklandi)
btn2.grid(column=1, row=3)
txt = Entry(window, width=10)
txt.grid(column=0, row=1)
txt2 = Entry(window, width=10, font=("Courier New", 20))
txt2.grid(column=0, row=1)
window.mainloop()