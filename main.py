import speech_recognition as sr
import pyttsx3
import pywhatkit as kit
import random as ra
import os
import webbrowser as wb
from youtubesearchpython import VideosSearch

apps = {
    "notepad":       ("notepad",      "notepad.exe"),
    "calculator":    ("calc",         "Calculator.exe"),
    "word":          ("winword",      "WINWORD.EXE"),
    "powerpoint":    ("powerpnt",     "POWERPNT.EXE"),
    "chrome":        ("chrome",       "chrome.exe"),
    "paint":         ("mspaint",      "mspaint.exe"),
    "file explorer": ("explorer", "explorer.exe"),
    "cmd":           ("cmd", "cmd.exe"),
    "task manager":  ("taskmgr",      "Taskmgr.exe"),
    "settings":      ("ms-settings:", ""),
    "control panel": ("control",      "control.exe"),
    "youtube":       ("https://youtube.com", ""),  
}



engine=pyttsx3.init()
engine.setProperty("rate",150)
engine.setProperty("volume",1.0)
voice=engine.getProperty("voices")
engine.setProperty("voice",voice[1].id)
'''r=sr.Recognizer()
with sr.Microphone() as source:
        
        while True:
            try:
                r.adjust_for_ambient_noise(source,duration=2)
                print("Listening ...")
                audio=r.listen(source)
                print("Listened ...")
                s=r.recognize_google(audio)
                print(s)
                engine.say("Do you want to change the input ?")
                engine.runAndWait()
                print("AI: Do you want to change the input ?")
                r.adjust_for_ambient_noise(source,duration=2)
                audio=r.listen(source)
                opt=r.recognize_google(audio)
                print("You:",opt)
                if "YES" in opt.upper():
                     continue
                else:
                     engine.save_to_file(s,"voice.wav")
                     break
            except:
                print("Error")'''
def youtube(s):
    try:
        videos = VideosSearch(s,5)
        result = videos.result()["result"][0]
        url = result["link"]
        title = result["title"]
        print("AI: Found - ",title)
        speak("Now Playing "+ title)
        wb.open(url)

    except Exception as e:
        print("AI: Error - ",e)
    return


def whatsmsg():
      
    r=sr.Recognizer()
    with sr.Microphone() as source:
        while True:
            
                        
            try:
                #r.adjust_for_ambient_noise(source,duration=2)
                #audio=r.listen(source)
                #print("AI: Please Enter the Whatsapp Number with country code for India it is +91 who do you want to send Message")
                #engine.say("Please tell the Whatsapp Number with country code for India it is +91 who do you want to send Message")
                #engine.runAndWait()
                phone_number=""
                r.adjust_for_ambient_noise(source,duration=8)
                audio=r.listen(source)
                digit=r.recognize_google(audio).strip().replace(" ","")
                phone_number+=digit
                print("You:",phone_number)
                engine.say("Enter the Phone Number with Country code")
                engine.runAndWait()
                phn=input("AI: Enter the Phone Number with Country code :\n")
                

                if not phn.startswith("+"):
                    print("AI: Invalid phone number. Please include the country code.")
                    engine.say("Invalid phone number. Please include the country code.")
                    engine.runAndWait()
                    continue
                
                print("You:", phn)
                break
            except:
                print("Error")
                engine.say("Error...")
                engine.runAndWait()
                continue

        while True:
                try:
                    print("AI: Please tell the Message you want to send")
                    engine.say("Please tell the Message you want to send")
                    engine.runAndWait()
                    r.adjust_for_ambient_noise(source,duration=2)
                    audio=r.listen(source)
                    msg=r.recognize_google(audio)
                    print("You:",msg)
                    print("Do you want to make changes in Message ?")
                    engine.say("Do you want ot make changes in Message ?")
                    engine.runAndWait()
                    r.adjust_for_ambient_noise(source,duration=2)
                    audio=r.listen(source)
                    opt=r.recognize_google(audio)
                    print("You:",opt)
                    if "NO" in opt.upper():
                        break
                    else:
                        continue
                
                except:
                    print("Error")
                    engine.say("Error...")
                    engine.runAndWait()
                    continue

        while True:
                try:
                    print("AI: Do you want send an instant message or Do you want to send message later")
                    engine.say("Do you want send an instant message or Do you want to send message later")
                    engine.runAndWait()
                    r.adjust_for_ambient_noise(source,duration=5)
                    audio=r.listen(source)
                    ch=r.recognize_google(audio)
                    print("You:",ch)

                    if "instant" in ch.lower():
                        kit.sendwhatmsg_instantly(phn, msg)
                        print("AI: Message sent Successfully :)")
                        engine.say("Message sent Successfully")
                        engine.runAndWait()
                        break

                    else:
                        print("AI: Ok")
                        engine.say("Ok")
                        while True:
                            try:
                                print("AI: Now tell the hour in 24 hour format to send message")
                                engine.say("Now tell the hour in 24 hour format to send message")
                                engine.runAndWait()
                                r.adjust_for_ambient_noise(source,duration=2)
                                audio=r.listen(source)
                                hr=int(r.recognize_google(audio).strip())
                                print("You:",hr)
                                engine.say("Do you want to change the hour ?")
                                print("Do you want to change the hour ?")

                                print("AI: Now tell the minutes to send message")
                                engine.say("Now tell the minutes to send message")
                                engine.runAndWait()
                                r.adjust_for_ambient_noise(source,duration=2)
                                audio=r.listen(source)
                                min=int(r.recognize_google(audio).strip())
                                print("You:",min)

                                kit.sendwhatmsg(phn,msg,hr,min)
                                print("AI: Message sent Successfully :)")
                                engine.say("Message sent Successfully")
                                engine.runAndWait()
                                break
                            except:
                                print("Error")
                                engine.say("Error...")
                                engine.runAndWait()
                                continue
                
                    
                except:
                    print("Error")
                    engine.say("Error...")
                    engine.runAndWait()
                    continue   
    return

def speak(text):
    engine.say(text)
    engine.runAndWait()

def open_app(s):

    s = s.lower()                          
    for app in apps:
        if f"open {app}" in s:
            process, _ = apps[app]
            if process:
                speak(f"Opening {app}")
                os.system(f"start {process}")
            else:
                speak(f"{app} can't be opened.")
            return 





def close_app(s):

    s = s.lower()      
    for app in apps:
        if f"close {app}" in s:
            _, process = apps[app]
            if process:
                speak(f"Closing {app}")
                os.system(f"taskkill /F /IM {process}")
            else:
                speak(f"{app} can't be closed directly.")
            return 
            

def main():
    print("Inside main")
    r=sr.Recognizer()

    with sr.Microphone() as source:
        
        while True:
            r.adjust_for_ambient_noise(source,duration=2)
            
            print("Listening ...")
            audio=r.listen(source)
            print("Listened ...")
            
            try:
                s=r.recognize_google(audio)
                print("You:",s)
                
                if "close" in s.lower():
                    close_app(s)
                    return                             
                
                elif "song" in s.lower() or "on youtube" in s.lower():
                    youtube(s)
                    return                    
                
                elif "whatsapp" in s.lower() or "message" in s.lower():
                    whatsmsg()

                elif "open youtube" in s.lower():
                    wb.open("https://www.youtube.com")
                    return
                              
                elif "open google" in s.lower():
                    wb.open("https://www.google.com")
                    return

                elif "open chatgpt" in s.lower():
                    wb.open("https://www.chatgpt.com")
                    return

                elif "open chatgpt" in s.lower() and "new tab" in s.lower():
                    wb.open_new_tab("https://www.chatgpt.com")
                    return
                
                elif "open github" in s.lower():
                    wb.open("https://www.github.com")
                    return
                
                elif "open github" in s.lower() and "new tab" in s.lower():
                    wb.open_new_tab("https://www.github.com")
                    return

                elif "open amazon" in s.lower():
                    wb.open("https://www.amazon.com")
                    return            

                elif "open linkedin" in s.lower():
                    wb.open("https://www.linkedin.com")
                    return
                
                elif "open gemini" in s.lower():
                    wb.open("https://gemini.google.com/app")
                    return
                
                elif "general settings" in s.lower():
                    speak("Opening general Settings")
                    os.system("start ms-settings:")
                    return
                
                elif "wi-fi settings" in s.lower():
                    speak("Opening Wifi Settings")
                    os.system("start ms-settings:network-wifi")
                    return
                
                elif "open calculator" in s.lower():
                    speak("Opening Calculator")
                    os.system("start calc")

                elif "open" in s.lower() :
                    open_app(s)
                    return
                
                            
                
                elif "end" in s.lower() or "bye" in s.lower() or "exit" in s.lower():
                    speak("Good Bye!")
                    break            
                else:
                    speak("Sorry this function is not available")
                    print("Error")
                    continue


            except:
                print("AI: Sorry I can't understand, Say again.")
                speak("Sorry I can't understand, Say again.")
                
        
r=sr.Recognizer()
with sr.Microphone() as source:
    rep=["Hi! Nice to meet you","Good to see you","Hello!, Have a great day","Hi! Whatsapp!"]
    rp=ra.choice(rep)
    print("AI: ",rp)
    speak(rp)
    while True:
            
        r.adjust_for_ambient_noise(source,duration=2)
        print("Listening ...")
        audio=r.listen(source)
        print("Listened ...")

        try:
            s=r.recognize_google(audio)
            print("You: ",s)
            if "vaspy" in s.lower():               
                
                print("AI: Yes, I'm listening !")
                speak("Yes, I'm listening !")                
                main()
            elif "exit" in s.lower() or "bye" in s.lower():
                break
            

        except:
            print("Error in main")




        

 
