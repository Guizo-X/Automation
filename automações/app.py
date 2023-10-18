import pyautogui as pa
import time


pa.press('win')
pa.write('chrome')
pa.press('enter')
time.sleep(3)
pa.click(x=421, y=340)
time.sleep(3)
pa.write("https://www.leagueofgraphs.com/pt/")
pa.press('enter')
time.sleep(4)
pa.click(x=1040, y=104)
pa.write("Ghost rid3r")
time.sleep(3)
pa.press('Down')
pa.press('enter')
