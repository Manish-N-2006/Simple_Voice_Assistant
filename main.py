import speech_recognition as sr
import pyttsx3
import pywhatkit as kit
import random as ra


engine=pyttsx3.init()
engine.setProperty("rate",150)
engine.setProperty("volume",1.0)
voice=engine.getProperty("voices")
engine.setProperty("voice",voice[1].id)
r=sr.Recognizer()
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
                print("Error")
def youtube(s):
    print("AI: Now playing ")
    engine.say("Now playing")
    engine.runAndWait()
    content=s.lower().replace("youtube","")
    kit.playonyt(content)
    return

def whatsmsg():
      
    r=sr.Recognizer()
    with sr.Microphone() as source:
        while True:
            
                        
            try:
               
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

def main():
    rep=["Hi! Nice to meet you","Good to see you","Hello!, Have a great day","Hi! Whatsapp!"]
    r=sr.Recognizer()

    with sr.Microphone() as source:
        rp=ra.choice(rep)
        print("AI: ",rp)
        engine.say(rp)
        engine.runAndWait()
        while True:
            r.adjust_for_ambient_noise(source,duration=2)
            
            print("Listening ...")
            audio=r.listen(source)
            print("Listened ...")
            
            try:
                s=r.recognize_google(audio)
                print("You:",s)
                #engine.say(s)
                #engine.runAndWait()
                if "song" in s.lower() or "youtube" in s.lower():
                    youtube(s)
                    break
                    
                
                elif "whatsapp" in s.lower() or "message" in s.lower():
                    whatsmsg()
                
                elif "end" in s.lower() or "bye" in s.lower() or "exit" in s.lower():
                    break            
                else:
                    engine.say("Error...")
                    engine.runAndWait()
                    print("Error")


            except:
                print("Sorry I can't understand, Say again.")
                engine.say("Sorry I can't understand, Say again.")
                engine.runAndWait()
        

        
main()
 
