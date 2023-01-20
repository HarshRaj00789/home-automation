from speak_module import speak
from speak_module import takeCommand
import controller as con
import os
 
if __name__ == "__main__":
    while True:
        query = takeCommand().lower()

        if "relay one on" in query :
            print(query)
            con.digitalpin_1.write(1)
            speak("done sir")
        elif "relay one off" in query :
            print(query)
            con.digitalpin_1.write(0)
            speak("done sir")
        elif "relay two on" in query :
            print(query)
            con.digitalpin_2.write(1)
            speak("done sir")
        elif "relay two off" in query :
            print(query)
            con.digitalpin_2.write(0)
            speak("done sir")
        elif "relay three on" in query :
            print(query)
            con.digitalpin_3.write(1)
            speak("done sir")
        elif "relay three off" in query :
            print(query)
            con.digitalpin_3.write(0)
            speak("done sir")
        elif "relay four on" in query :
            print(query)
            con.digitalpin_4.write(1)
            speak("done sir")
        elif "relay four off" in query :
            print(query)
            con.digitalpin_4.write(0)
            speak("done sir")
        elif "relay 2 on" in query :
            print(query)
            con.digitalpin_2.write(1)
            speak("done sir")
        elif "relay 2 off" in query :
            print(query)
            con.digitalpin_2.write(0)
            speak("done sir")
        elif "relay 3 on" in query :
            print(query)
            con.digitalpin_3.write(1)
            speak("done sir")
        elif "relay 3 off" in query :
            print(query)
            con.digitalpin_3.write(0)
            speak("done sir")
        elif "relay 4 on" in query :
            print(query)
            con.digitalpin_4.write(1)
            speak("done sir")
        elif "relay 4 off" in query :
            print(query)
            con.digitalpin_4.write(0)
            speak("done sir")
        elif "vision mode" in query:
            os.startfile("D:\\new life\\python project\\IOT PROJECT\\relayvision.py")
            exit()
        elif "all relay on" in query:
            con.digitalpin_1.write(1)
            con.digitalpin_2.write(1)
            con.digitalpin_3.write(1)
            con.digitalpin_4.write(1)
            speak("all relay are on")
        elif "all relay off" in query:
            con.digitalpin_1.write(0)
            con.digitalpin_2.write(0)
            con.digitalpin_3.write(0)
            con.digitalpin_4.write(0)
            speak("all relay are off")
        elif "shutdown" in query:
            quit()
       
            

            
            
            

            






            
            


     
        
        