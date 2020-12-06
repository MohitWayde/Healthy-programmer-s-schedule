# Place all files in same folder(txt file, mp3 file and this python file
import datetime
import time
from pygame import mixer
# Global declaration
water = 40*60 #40 mins 40*60
eyes = 20*60 #20 mins 20*60
exercise = 45*60 # 45 mins 45*60
# Functions
def musicforsch(file, stopper_msg): 
    mixer.init()
    mixer.music.load(file)
    mixer.music.play()
    while True:
        stop_music_text = input()
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
    
        print("schedule started at ",datetime.datetime.now())
        init_water = time.time()
        init_eyes = time.time()
        init_exercise = time.time()

        while True:
            if  time.time()-init_water > water:
                print("DON'T SKIP! Water time .............Type wdone to stop the song")
                musicforsch("water.mp3", "wdone") # dont forget to change filename, paste any mp3 file in the folder where this python file is located
                logfile("Drank water at      :")
                init_water = time.time()
            if  time.time()-init_eyes > eyes:
                print("DON'T SKIP! Eyes exercise time......Type edone to stop the song")
                musicforsch("eyes.mp3", "edone") # dont forget to change filename, paste any mp3 file in the folder where this python file is located
                logfile("Eyes exercise at    :")
                init_eyes = time.time()
            if  time.time()-init_exercise > exercise:
                print("DON'T SKIP! physical exercise time..Type pdone to stop the song")
                musicforsch("hpysicalact.mp3", "pdone") # dont forget to change filename, paste any mp3 file in the folder where this python file is located
                logfile("PhMovement at       :") 
                init_exercise = time.time()



scheduler_app()
