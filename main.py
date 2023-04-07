from pynput.keyboard import Key, Controller, Listener
import time
import os
import pyscreenshot as ImageGrab
import pytesseract

print("Program execution begins...\n")
time.sleep(5)

keyboard = Controller()

while True:
    # Step 1: Convert screenshot to string
    im = ImageGrab.grab()
    im.save('image.jpg')

    # noinspection SpellCheckingInspection
    pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract'
    string = pytesseract.image_to_string(os.getcwd()+'\\image.jpg', config='--psm 11').lower()

    print('*' * 50)
    print(string)
    print('*' * 50)

    f = open('string.txt', mode='a')
    f.write(string)

    # Step 2: Depending on what's in the screenshot, add various logic

    if "to next match" in string or "skip match" in string or "participant settings" in string:
        keyboard.press(Key.up)
        time.sleep(0.1)
        keyboard.release(Key.up)
        time.sleep(0.1)
        keyboard.press(Key.enter)
        time.sleep(0.1)
        keyboard.release(Key.enter)
    elif "you will refuse the transfer offer" in string or "you have yet to select a national team" in string:
        keyboard.press(Key.right)
        time.sleep(0.1)
        keyboard.release(Key.right)
        keyboard.press(Key.enter)
        time.sleep(0.1)
        keyboard.release(Key.enter)
    else:
        keyboard.press(Key.enter)
        time.sleep(0.1)
        keyboard.release(Key.enter)

    time.sleep(0.1)
