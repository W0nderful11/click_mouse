import pynput.keyboard as keyboard
import pynput.mouse as mouse
import time

# Текст, который нужно вставить
text_to_paste = "эмуляции текста"

# Функция для эмуляции клика мыши
def click_mouse():
    mouse.Controller().click(mouse.Button.left)

# Функция для эмуляции набора текста
def type_text(text):
    for char in text:
        keyboard.Controller().press(char)  # Нажимаем клавишу
        keyboard.Controller().release(char)  # Отпускаем клавишу

# Функция для эмуляции нажатия клавиши Enter
def press_enter():
    keyboard.Controller().press(keyboard.Key.enter)
    keyboard.Controller().release(keyboard.Key.enter)

# Главная функция, которая выполняет все действия
def perform_actions():
    # Пауза 3 секунды перед началом выполнения
    print("Ожидание 3 секунды перед началом...")
    time.sleep(3)

    while True:
        click_mouse()  # Клик мышью
        type_text(text_to_paste)  # Вставка текста
        press_enter()  # Нажатие Enter
        time.sleep(5)  # Пауза 5 секунд перед следующим циклом

if __name__ == "__main__":
    perform_actions()
