# Place all files in same folder(txt file, mp3 file and this python file
import datetime
import time
from pygame import mixer
# Global declaration
water = 3480 # 58 mins
eyes = 1020 # 17 mins  
exercise = 2700 # 45mins
# Functions
def musicforsch(file, stopper_msg): 
    mixer.init()
    mixer.music.load(file)
    mixer.music.play()
    while True:
        stop_music_text = input("Enter stopper message :")
        if stop_music_text == stopper_msg:
            mixer.music.stop()
            break
            
try:
    def logfile(msg):
        with open("schedulerlog.txt","a") as f1: #create .txt file for generating log of you exercises
            mytime = time.strftime("%H"":""%M")
            f1.write(f"{msg}{mytime} : DATE & TIME {datetime.datetime.now()} \n")
except Exception as e:
    print(e)



def scheduler_app():
    
        print("schedule started")
        init_water = time.time()
        init_eyes = time.time()
        init_exercise = time.time()

        while True:
            if  time.time()-init_water > water:
                musicforsch("water.mp3", "wdone") # dont forget to change filename, paste any mp3 file in the folder where this python file is located
                logfile("Drank water at      :")
                init_water = time.time()
            if  time.time()-init_eyes > eyes:
                musicforsch("eyes.mp3", "edone") # dont forget to change filename, paste any mp3 file in the folder where this python file is located
                logfile("Eyes exercise at    :")
                init_eyes = time.time()
            if  time.time()-init_exercise > exercise:
                musicforsch("hpysicalact.mp3", "pdone") # dont forget to change filename, paste any mp3 file in the folder where this python file is located
                logfile("PhMovement at       :") 
                init_exercise = time.time()



scheduler_app()
