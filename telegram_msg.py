import pyautogui as pg
import time

time.sleep(3)
#print(pg.position())

pg.leftClick(1180, 1056, 1, 3)
time.sleep(1)
pg.typewrite('web.telegram.org/k/')
time.sleep(1)
pg.press('enter')
time.sleep(1)
pg.leftClick(355, 213, 1, 3)
time.sleep(1)

for i in range(3):
    pg.typewrite('SPAM MSG USING PYAUTOGUI')
    pg.press('enter')
    time.sleep(1)

print('DONE!')