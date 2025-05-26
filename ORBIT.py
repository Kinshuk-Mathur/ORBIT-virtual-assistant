import sys
import pyttsx3
import speech_recognition as sr
import webbrowser
import datetime
import wikipedia
import random

# Initialize the text-to-speech engine
engine = pyttsx3.init()
engine.setProperty("rate", 160)  # Speech rate


def speak(audio):
    """Speak out the given text using pyttsx3."""
    engine.say(audio)
    engine.runAndWait()


def command():
    """
    Listen to the user's voice input using the microphone,
    convert speech to text and return it.
    """
    content = ""
    while content == "":
        r = sr.Recognizer()
        with sr.Microphone() as source:
            print("Say something!")
            audio = r.listen(source)

        try:
            content = r.recognize_google(audio, language='en-in')
            print("Your command 😊 =  " + content)
        except Exception as e:
            print("Try again 😕 ......")
    return content


def main_content():
    """
    Main loop that continuously listens for commands and
    executes corresponding actions.
    """
    while True:
        request = command().lower()

        # Wake up command
        if "wake up" in request:
            speak("Hello Kinshuk sir! How can I help you?")

        # Music related commands
        elif "play music" in request:
            speak("Which song you want to play sir?")

        elif "pal pal" in request:
            speak("Ok! playing the song sir.")
            webbrowser.open("https://www.youtube.com/watch?v=8of5w7RgcTc&pp=ygUHcGFsIHBhbA%3D%3D")

        elif "aura song" in request:
            speak("Ok!, playing the song sir")
            webbrowser.open("https://www.youtube.com/watch?v=22znSD6r_14&pp=ygUYcGhvbmsgc29uZ3Mgbm8gY29weXJpZ2h0")

        elif "departure lane" in request:
            speak("Ok! playing the song sir.")
            webbrowser.open("https://www.youtube.com/watch?v=25cpx_ThZhg&pp=ygUOZGVwYXJ0dXJlIGxhbmU%3D")

        elif "ranjha ve" in request:
            speak("Ok! playing the song sir.")
            webbrowser.open("https://www.youtube.com/watch?v=55c6IlV7BEo&pp=ygUJcmFuamhhIHZl")

        elif "jhol" in request:
            speak("Ok! playing the song sir.")
            webbrowser.open("https://www.youtube.com/watch?v=-2RAq5o5pwc&pp=ygUEamhvbNIHCQl-CQGHKiGM7w%3D%3D")

        # Time and Date
        elif "say time" in request:
            time = datetime.datetime.now().strftime("%H:%M")
            speak("The time is " + str(time))

        elif "say date" in request:
            date = datetime.datetime.now().strftime("%d")
            speak("The date is " + str(date))

        # Add new task (Note: currently takes task from same command, may improve by asking separately)
        elif "new task" in request:
            speak("Ok! adding new task sir.")
            task = request.replace("new task", "").strip()
            if task:
                with open("todo.txt", "a") as file:
                    file.write(f"{task}\n")
                speak("Task added")

        # Play One Piece episode
        elif "one piece" in request:
            speak("Ok! sir?")
            onepe_ep = request.replace("orbit", "").replace("open one piece episode", "").strip()
            encode_ep = onepe_ep.replace(" ", "+")
            url1 = f"https://www.miruro.tv/watch?id=21&ep={encode_ep}"

            webbrowser.open(url1)
            speak(f"Playing the episode {onepe_ep} of One Piece sir. Enjoy watching sir!")

        # Open Pinterest website
        elif "pinterest" in request:
            speak("Ok! sir.")
            speak("Opening Pinterest sir!")
            url2 = "https://in.pinterest.com"
            webbrowser.open(url2)
            speak("Done sir!")

        # Google search
        elif "search google" in request:
            speak("Ok! sir")
            search_query = request.replace("orbit", "").replace("search google", "").strip()
            encoded_query = search_query.replace(" ", "+")
            url = f"https://www.google.com/search?q={encoded_query}"
            webbrowser.open(url)
            speak(f"Searching Google for: {search_query}")

        # YouTube search and open
        elif "open youtube and search" in request:
            speak("Ok! opening")
            search = request.replace("orbit", "").replace("open youtube and search", "").strip()
            e_search = search.replace(" ", "+")
            url1 = f"https://www.youtube.com/results?search_query={e_search}"
            webbrowser.open(url1)
            speak(f"Searching Youtube for: {search}")
            continue

        # Basic greeting response
        elif "how are you " in request or "how r u" in request:
            speak("I am fine sir.")
            speak("How are you sir? How can I help you Kinshuk sir!")

        # Dice rolling
        elif "roll the dice" in request or "dice" in request:
            speak("Rolling the dice, sir...")
            dice_result = random.randint(1, 6)
            print(f"You got a {dice_result}")
            speak(f"You got a {dice_result}")

        # Wikipedia information retrieval
        elif "give information" in request:
            speak("Sure sir.")
            search_query = request.replace("orbit", "").replace("give information about", "").strip()
            speak(f"Searching for {search_query}, please wait.")
            try:
                summary = wikipedia.summary(search_query, sentences=2)
            except wikipedia.DisambiguationError as e:
                summary = "Your query is ambiguous, please be more specific."
            except wikipedia.PageError:
                summary = "Sorry, I couldn't find any information on that topic."
            speak("Here's what I found:")
            print(summary)
            speak(summary)
            speak("Anything else sir?")
            continue

        # Goodbye phrases
        elif "say bye" in request:
            print("Bye!")
            speak("Bye viewers, subscribe to my creator Kinshuk. He's a cool guy.")

        # Exit command
        elif "chup" in request:
            speak("Ok! Bye sir.")
            sys.exit()


# Start the assistant
main_content()
