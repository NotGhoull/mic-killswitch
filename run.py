from classes.kill import KillSwitch 

ks = KillSwitch()
shutdownType = "shutdown"

# Check version
with open("version.txt", "r") as f:
    version = f.read()
    print(f"Version: {version}")
    # Check if the version text matches the github raw version.txt
    import requests
    r = requests.get("https://raw.githubusercontent.com/NotGhoull/mic-killswitch/master/version.txt")
    if r.text != version:print("[WARNING] The version of this program is outdated. Please update to the latest version.")
    else: print("Code is up to date!")
    f.close()


print(f"App is listening for kill word: {ks.killWord}")

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
