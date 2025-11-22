import re
from gtts import gTTS
import pygame
import time

# Monthly limit in rupees
monthly_limit = 5000
current_spending = 0

# Initialize pygame for sound
pygame.mixer.init()

def extract_amount(text):
    """
    Extracts the amount from a transaction-like text.
    Accepts formats like: Rs 300, INR 400, ₹500, etc.
    """
    # Regex to find currency format: Rs / INR / ₹ followed by digits
    match = re.search(r'(?:Rs|INR|₹)\.?\s?(\d+)', text)
    return int(match.group(1)) if match else 0

def speak(text):
    """
    Converts the given text to speech using gTTS
    and plays it using pygame.
    """
    tts = gTTS(text=text, lang='en')
    tts.save("alert.mp3")

    pygame.mixer.music.load("alert.mp3")
    pygame.mixer.music.play()

    # Wait till the audio finishes playing
    while pygame.mixer.music.get_busy():
        time.sleep(0.1)

print("Enter transactions like: Rs 300 to Swiggy")
print("Type 'stop' to end.\n")

while True:
    sms = input("Transaction: ")

    if sms.lower() == "stop":
        break

    # Extract the amount from the entered text
    amount = extract_amount(sms)
    current_spending += amount

    print(f"Detected: ₹{amount}, Total spending: ₹{current_spending}")

    # Check if total spending exceeds the limit
    if current_spending > monthly_limit:
        speak("सावधान! आप बहुत ज्यादा खर्च कर रहे हैं। कृपया अपने खर्चे कम करें।")
        break
