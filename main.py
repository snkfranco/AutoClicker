import pyautogui
from time import sleep
import threading
import keyboard

class AutoClicker:
    def __init__(self, interval):
        self.interval = interval
        self.running = False

    def start_clicking(self):
        self.running = True
        while self.running:
            pyautogui.click()
            sleep(self.interval)

    def stop_clicking(self):
        self.running = False

def on_press_event(clicker):
    if not clicker.running:
        threading.Thread(target=clicker.start_clicking).start()

def on_release_event(clicker):
    clicker.stop_clicking()

if __name__ == '__main__':
    interval = float(input('Digite o intervalo que deseja entre os cliques (em segundos): '))
    clicker = AutoClicker(interval)

    print("Pressione 'q' para começar e parar o autoclicker")
    keyboard.on_press_key("alt", lambda _: on_press_event(clicker))
    keyboard.on_press_key("alt", lambda _: on_release_event(clicker))

    keyboard.wait("esc")
    print('Saindo do programa')
    