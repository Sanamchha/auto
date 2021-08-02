import pyautogui as pg
import random as r
import time as t

def start():
    ran=r.randint(1,3)
    
    pg.moveTo(188,313,r.randint(1,3),pg.easeInBounce)
    pg.click()
    pg.moveTo(342,275,r.randint(1,2))
    pg.click()
    pg.dragTo(342,689,duration=3)
    t.sleep(ran)
    pg.moveTo(1019,186,r.randint(1,3),pg.easeInOutQuad)
    pg.dragTo(1019,665,duration=3)
    t.sleep(ran)
    pg.moveTo(1350,186,r.randint(1,3),pg.easeInOutQuad)
    pg.dragTo(1350,665,duration=3)

    pg.moveTo(1019,665,r.randint(1,3),pg.easeInOutQuad)
    pg.dragTo(1019,186,duration=3)
    t.sleep(ran)
    pg.moveTo(520,744,r.randint(1,2))
    pg.click()
    t.sleep(ran)

    pg.write('thank you',interval=0.25)
    pg.press('enter')
    pg.moveTo(576,457,r.randint(1,2))
    pg.click()
    t.sleep(ran)
    pg.press('enter')
    pg.write('we dedicate our time and effort to serve you well with the features of ibotta ',interval=0.25)
    pg.hotkey('ctrl','a')
    t.sleep(ran)
    pg.write('sorry',interval=0.5)
    t.sleep(ran)

    pg.moveTo(1348,200,r.randint(1,3),pg.easeInOutQuad)
#     pg.click(clicks=5,interval=1,button='left')
    pg.moveTo(1348,697,r.randint(1,2),pg.easeInOutQuad)
    pg.dragTo(1348,200,duration=3)
    t.sleep(1)


def automation():
    pg.moveTo(543,139,duration=r.randint(1,3))
    pg.moveTo(194,149,duration=r.randint(2,3))

    pg.click()

    pg.moveTo(941,155,duration=r.randint(1,3))
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
    pg.moveTo(25,444,duration=r.randint(1,3))
    pg.click()

        #down arrow
    pg.moveTo(571,759,duration=r.randint(1,2))
    pg.click(clicks=r.randint(2,4),interval=1,button='left')

    pg.moveTo(1348,190,duration=r.randint(1,2))
    pg.dragTo(1348,720,duration=r.randint(2,3))
    pg.moveTo(776,428,duration=r.randint(2,3))
    pg.click(clicks=r.randint(2,3),interval=1,button='left')
    
    pg.click()
    pg.hotkey('ctrl','f')
    t.sleep(2)
    pg.write('any brand',interval=0.20)
    pg.press('enter')
    pg.click()

    pg.moveTo(706,17,duration=r.randint(2,4))
    pg.click(clicks=2,interval=2,button='left')

    pg.moveTo(251,95,r.randint(1,3),pg.easeInBounce)
    pg.click()
    pg.moveTo(884,306,duration=r.randint(2,3))
    pg.click()
    pg.moveTo(181,312,r.randint(1,2),pg.easeInOutQuad)
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
    
    
