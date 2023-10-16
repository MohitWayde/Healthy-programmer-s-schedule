import datetime
import time
# from pygame import mixer
import webbrowser

# Global declaration

water = 60*60 
eyes = 25*60
exercise = 45*60 

# Functions
'''
def musicforsch(file, stopper_msg): 
    mixer.init()
    mixer.music.load(file)
    mixer.music.set_volume(0.1)
    mixer.music.play()
    while True:
        stop_music_text = input()
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
'''


def scheduler_app():
    print("schedule started at ",datetime.datetime.now())
    init_water = time.time()
    init_eyes = time.time()
    init_exercise = time.time()
    mytime = time.strftime("%H"":""%M")
    while True:
        # if  time.time()-init_water > water: 
        #     print("DON'T SKIP! WATER time .............Type wdone to stop the song")
        #     musicforsch("Besabriyaan.mp3", "wdone")
        #     logfile("Drank water at      :")
        #     init_water = time.time()
        if  time.time()-init_eyes > eyes:
            print(f"ITS COMPOUNDING HABITS!{datetime.datetime.now()} EYES EXERCISE TIME...")
            # musicforsch("Ik-vaari-aa-karaoke.mpeg", "edone")
            # musicforsch("Besabriyaan.ogg", "edone")
            webbrowser.open("https://www.google.com")
            done = input()
            if done=="ed" or done=="ED":
            # from playsound import playsound
            # playsound("Besabriyaan.mp3")
            # print(f"You've done at {datetime.datetime.now()}")
            # logfile("Eyes exercise at    :")
                print(f"You've done at {datetime.datetime.now()}")
                init_eyes = time.time()
        # if  time.time()-init_exercise > exercise:
        #     print("DON'T SKIP! PHYSICAL exercise time..Type pdone to stop the song")
        #     musicforsch("Avengers_Infinity_War_Soundtrack_-_Avengers_Theme_Suite_Alan_Silvestri[ListenVid.com].mp3", "pdone")
        #     logfile("PhMovement at       :") 
        #     init_exercise = time.time()



scheduler_app()
