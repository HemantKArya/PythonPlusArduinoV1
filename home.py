import speech_recognition as sr
import pyfirmata


def takecom():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listning....")
        audio = r.listen(source)
    try:
        print("Recognising.") 
        text = r.recognize_google(audio,language='en-in')
        print(text)
    except Exception:                #For Error handling
        print("Network connection error") 
        return "none"
    return text

board = pyfirmata.Arduino('COM3')

#it = pyfirmata.util.Iterator(board)
#it.start()
board.digital[7].mode = pyfirmata.OUTPUT
board.digital[7].write(1)
while True:
    sw = takecom().lower()
    if 'turn on' in sw or 'open' in sw:
        board.digital[7].write(0)
    else:
        board.digital[7].write(1)