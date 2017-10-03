import pyautogui

pyautogui.screenshot('c:\\users\\s k sharma\\desktop\\python_practice\\screenshot1.png')

print pyautogui.locateOnScreen('c:\\users\\s k sharma\\desktop\\python_practice\\screenshot1.png')

pyautogui.moveTo(4, 696, duration=1)
pyautogui.click()
