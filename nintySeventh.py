import pyautogui
width, height = pyautogui.size()
print pyautogui.position()
pyautogui.click()
dist = 200
pyautogui.moveTo(10, 10, duration=1)
pyautogui.moveRel(800, 0, duration=1)
pyautogui.click(7, 12, duration=2)
pyautogui.click(7, 12, duration=2)
while dist > 0:
    pyautogui.dragRel(dist, 0, duration=0.5)
    dist = dist - 25
    pyautogui.dragRel(0, dist, duration=0.5)
    pyautogui.dragRel(-dist, 0, duration=0.5)
    dist = dist - 25
    pyautogui.dragRel(0, -dist, duration=0.5)
