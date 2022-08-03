import eel
import random
import time

eel.init("codigos")

@eel.expose
def conseguir():
    time.sleep(1)
    return(random.randint(0, 1000))

@ell.expose
def conseguir():
    time.sleep(1)
    return(random.randint(0, 1000))

eel.start("index.html")

