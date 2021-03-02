import speech_recognition as sr
import pyttsx3 as pt 
import pywhatkit as kit
import datetime
import wikipedia
import pyjokes as joke
import PyPDF2 as pdf

book = open('Angular.pdf', 'rb')
pdfReader = pdf.PdfFileReader(book)
pages = pdfReader.numPages

listener = sr.Recognizer()
engine = pt.init()
rate = engine.getProperty('rate')   # getting details of current speaking rate
engine.setProperty('rate', 150)   

def talk(text):
    engine.say(text)
    engine.runAndWait()
  
def read_pdf():
    for num in range(0, pages):
        page = pdfReader.getPage(num)
        text = page.extractText()
        talk(text)
        
def take_command():
    try:
        with sr.Microphone() as source:
            print('Listening....')
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            command = command.lower().replace('alexa','')
            if 'alexa' in command:  
                print(command)
    except:
        print('no command got....')
        command = ''  
    return command  

def run_alexa():
    command = take_command()
    if 'play' in command:
        command = command.replace('play', '').replace('on youtube','')
        talk('Playing' + command)
        kit.playonyt(command)
    elif 'time' in command:
        time = datetime.datetime.now().strftime('%I:%M %p')
        print(time)
        talk('Currently time is ' + time)
    elif 'google' in command:
        command = command.replace('on google', '').replace('search', '').replace('could you please','')
        print(command)
        kit.search(command)
    elif 'wikipedia' in command:
        data = command.replace('on wikipedia', '').replace('search', '').replace('could you please','')
        print(data)
        info = wikipedia.summary(data,2)
        print(info)
        talk(info)
    elif 'joke' in command:
        talk(joke.get_joke())
    elif 'read' in command:
        read_pdf()
    elif 'thank' in command:
        talk('your welcome, tell me how can i help you ')
    elif bool(command):
        print(command)
        talk('Sorry i dont understand, Please say again..')
        print('Executed')

talk('Hello there, welcome to Alexa')
while True:    
    run_alexa()