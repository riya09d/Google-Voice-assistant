import pyttsx3
import speech_recognition as sr
import webbrowser

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def google_search(query):
    url = f'https://www.google.com/search?q={query}'
    webbrowser.open(url)
    speak(f"Here are your Google search results for {query}.")

def takecommand():
    r = sr.Recognizer()  # it will try to recognize the voice
    with sr.Microphone() as source:
        print("Listening.......")
        r.pause_threshold = 1  # it will wait for a second and convert it to text
        audio = r.listen(source)
    
    try:
        print("Wait for a sec. I'm recognising......")
        query = r.recognize_google(audio, language='en-in')  # Correct parameter name
        print(f"You said: {query}")
        return query

    except Exception as e:
        print(e)
        print("Try again!")
        speak("Didn't get that, try again")
        return "None"

# Calling the function 
def voice_assistant():
    print("Hey, Welcome to Riya's Voice assistant model")
    speak("Hey, Welcome to Riya's Voice assistant model")

    speak("What would you like to search on Google?")
    print("What would you like to search on Google?")
    query = takecommand()  # Get the user's search query

    google_search(query)

# Calling the voice assistant function
voice_assistant()

