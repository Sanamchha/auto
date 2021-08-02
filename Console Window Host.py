import pyautogui as pg
import random as r
import time as t

def start():
    ran=r.randint(1,3)
    
    pg.moveTo(268,285,r.randint(1,3),pg.easeInBounce)
    pg.click()
    pg.moveTo(477,287,r.randint(1,2))
    pg.click()
    pg.dragTo(477,998,duration=3)
    t.sleep(ran)
    pg.moveTo(1446,250,r.randint(1,3),pg.easeInOutQuad)
    pg.dragTo(1446,900,duration=3)
    t.sleep(ran)
    pg.moveTo(1908,250,r.randint(1,3),pg.easeInOutQuad)
    pg.dragTo(1908,900,duration=3)

    pg.moveTo(1446,900,r.randint(1,3),pg.easeInOutQuad)
    pg.dragTo(1446,250,duration=3)
    t.sleep(ran)
    pg.moveTo(972,1033,r.randint(1,2))
    pg.click()
    t.sleep(ran)

    pg.write('thank you',interval=0.25)
    pg.press('enter')
    pg.moveTo(1156,611,r.randint(1,2))
    pg.click()
    t.sleep(ran)
    pg.press('enter')
    pg.write('we dedicate our time and effort to serve you well with the features of ibotta ',interval=0.25)
    pg.hotkey('ctrl','a')
    t.sleep(ran)
    pg.write('sorry',interval=0.5)
    t.sleep(ran)

    pg.moveTo(1908,250,r.randint(1,3),pg.easeInOutQuad)
#     pg.click(clicks=5,interval=1,button='left')
    pg.moveTo(1908,900,r.randint(1,2),pg.easeInOutQuad)
    pg.dragTo(1908,250,duration=3)
    t.sleep(1)


def automation():
    pg.moveTo(952,123,duration=r.randint(1,3))
    pg.moveTo(1667,490,duration=r.randint(2,3))

    pg.click()

    pg.moveTo(952,123,duration=r.randint(1,3))
    pg.click()

        #find moderate
    pg.hotkey('ctrl','f')
    t.sleep(2)

    pg.write('moderate',interval=0.20)
    pg.press('enter')
    t.sleep(2)
    pg.hotkey('ctrl','enter')
    t.sleep(3)


        #show unchecked
    pg.moveTo(35,553,duration=r.randint(1,3))
    pg.click()

        #down arrow
    pg.moveTo(712,1068,duration=r.randint(1,2))
    pg.click(clicks=r.randint(2,4),interval=1,button='left')

    pg.moveTo(1905,306,duration=r.randint(1,2))
    pg.dragTo(1905,993,duration=r.randint(2,3))
    pg.moveTo(1234,527,duration=r.randint(2,3))
    pg.click(clicks=r.randint(2,3),interval=1,button='left')
    
    pg.click()
    pg.hotkey('ctrl','f')
    t.sleep(2)
    pg.write('any brand',interval=0.20)
    pg.press('enter')
    pg.click()

    pg.moveTo(885,20,duration=r.randint(2,4))
    pg.click(clicks=2,interval=2,button='left')

    pg.moveTo(348,117,r.randint(1,3),pg.easeInBounce)
    pg.click()
    pg.moveTo(1255,426,duration=r.randint(2,3))
    pg.click()
    pg.moveTo(257,433,r.randint(1,2),pg.easeInOutQuad)
    pg.click()
    t.sleep(r.randint(2,4))


a=1000
while (a!=0):
    if (a%2==0):
        start()
#         print('even')
    else:
        automation()
#         print('odd')
    a-=1
exit()
    
    
