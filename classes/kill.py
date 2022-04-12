class KillSwitch:

    def __init__(self, killWord:str="2006shutdown", confirmWord:str="confirm"):
        self.killWord = killWord
        self.confirmWord = confirmWord

    def listen(self):
        import speech_recognition as sr
        r = sr.Recognizer()
        text = None
        with sr.Microphone() as source:
            # print("Say something!")
            audio = r.listen(source)
        try:
            text = r.recognize_google(audio)
            # print(f"You said: {text}")
        except sr.UnknownValueError as e:
            # print(f"[ DEBUG ] {e}")
            pass
            # print("Could not understand audio")
        except sr.RequestError as e:
            print("Could not request results; {0}".format(e))

        return text.replace(" ", "") if text != None else ""


    def playWarningSound(self, audio):
        # Use a libary to play the warning sound in the background
        import winsound
        self.isPlaying = True
        for _ in range (20):
            if self.isPlaying: winsound.PlaySound(audio, winsound.SND_FILENAME)
            else: break
        self.isPlaying = False
        exit()

