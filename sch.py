# For final scheduler
# water_seconds = 3600
# eyes_seconds = 1800
# exercise_seconds = 2700
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
        with open("schedulerlog.txt","a") as f1:
            mytime = time.strftime("%H"":""%M")
            f1.write(f"{msg}{mytime} : DATE & TIME {datetime.datetime.now()} \n")
except Exception as e:
    print(e)



def scheduler_app():
    
        print("schedule started")
        init_water = time.time()
        init_eyes = time.time()
        init_exercise = time.time()
#         print("For WATER, I will remind you after every 1 hour")
#         print("For EYES , I will remind you after every 30 minutes")
#         print("For BODY MOVEMENT, I will remind you after every 45 minutes")
        while True:
            if  time.time()-init_water > water:
                musicforsch("Besabriyaan.mp3", "wdone")
                logfile("Drank water at      :")
                init_water = time.time()
            if  time.time()-init_eyes > eyes:
                musicforsch("Ik_Vaari_Aa.mp3", "edone")
                logfile("Eyes exercise at    :")
                init_eyes = time.time()
            if  time.time()-init_exercise > exercise:
                musicforsch("Hall-of-fame.mp3", "pdone")
                logfile("PhMovement at       :") 
                init_exercise = time.time()



scheduler_app()