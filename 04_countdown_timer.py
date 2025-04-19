import time
import pyttsx3

engine = pyttsx3.init()
engine.setProperty('rate', 150)
engine.setProperty('volume', 1)
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)

def countdown_timer(seconds):
    while seconds:
        mins, secs = divmod(seconds, 60)  
        timer = f"{mins:02d}:{secs:02d}"
        print(timer, end="\r")  
        time.sleep(1)
        seconds -= 1

    engine.say("Your countdown timer has ended. Time's up!")
    engine.runAndWait()

try:
    time_input = input("Enter time in format HH MM SS → ")
    h, m, s = map(int, time_input.split())
    if h < 0 or m < 0 or s < 0:
        print("Error: Hours, minutes, and seconds cannot be negative.")
    else:
        seconds_input = h * 3600 + m * 60 + s
        countdown_timer(seconds_input)

except ValueError:
    print("Invalid input. Please make sure to enter valid integers for hours, minutes, and seconds.")
except Exception as e:
    print(f"An error occurred: {e}")