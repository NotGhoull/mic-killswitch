from classes.kill import KillSwitch 

ks = KillSwitch()
shutdownType = "shutdown"


print(f"App is listening for kill word: {ks.killWord}")
# windows warning sound location
def start():
    from threading import Thread
    if ks.listen().lower() == ks.killWord.lower(): 
        print("Please confirm shutdown")
        # in another thread play the warning sound
        Thread(target=ks.playWarningSound, args=("C:\Windows\Media\Windows Balloon.wav",)).start()
        if ks.listen().lower() == ks.confirmWord.lower():
            print("Shutting down...")
            import os
            if shutdownType == "shutdown":
                os.system("shutdown -s -t 0")
            elif shutdownType == "restart":
                os.system("shutdown -r -t 0")
            elif shutdownType == "logoff":
                os.system("shutdown -l -t 0")
            else:
                exit(f"[ERROR] Unkown shutdown type: {str(shutdownType)}")
        else:
            ks.isPlaying = False
            print("Shutdown aborted")

    else: start()

start()