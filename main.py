try:
    import Image
except ImportError:
    from PIL import Image
import pytesseract
import os
cwd = os.getcwd()

import logging

logger = logging.getLogger("main")
logger.setLevel(logging.DEBUG)
fh = logging.FileHandler("main.log")

formatter = logging.Formatter('%(asctime)s,%(name)s,%(levelname)s - %(message)s')
fh.setFormatter(formatter)

# add handler to logger object
logger.addHandler(fh)

logdebug = logger.debug
loginfo = logger.info
logwarning = logger.warning
logerror = logger.error
logcritical = logger.critical

while True:
    try:
        print("The current directory is: " + str(cwd))
        dir = input('Please enter a valid IMAGE PATH relative to the current path: ')
        #os.chdir(dir)
        #cwd = os.getcwd()
        #print("The current directory is: " + str(cwd))
        #imgpath = input('Please enter a valid IMAGE PATH relative to the current path: ')
        print('--------------------')
        print(pytesseract.image_to_string(Image.open(imgpath)))
        print('--------------------')
        input("Press ENTER to restart")
        os.system("cls")
    except Exception as e:
        logerror(str(e))
        os.system("cls")
