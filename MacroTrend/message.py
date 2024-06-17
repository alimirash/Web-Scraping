import pyautogui
import time
import random

# List of 50 lovely messages
messages = [
    "You are a ray of sunshine that brightens my day.",
    "Your kindness and compassion inspire me every day.",
    "You have a heart of gold, and it shines through in everything you do.",
    "Your smile can light up the darkest of rooms.",
    "You are a beautiful soul, inside and out.",
    "I'm grateful for your presence in my life.",
    "Your positivity is contagious, and it lifts my spirits.",
    "You have a way of making even the simplest moments special.",
    "Your strength and resilience are truly admirable.",
    "You deserve all the happiness and love in the world.",
    "Your laughter is music to my ears, and it fills me with joy.",
    "You are an amazing person, and I'm lucky to know you.",
    "Your support means more to me than words can express.",
    "You have a beautiful and caring nature that touches the lives of many.",
    "Your determination and perseverance are truly inspiring.",
    "You are a wonderful human being, and the world is better with you in it.",
    "Your warmth and generosity create a ripple effect of kindness.",
    "You have a way of making the ordinary feel extraordinary.",
    "Your intelligence and wit never cease to impress me.",
    "You bring so much light and love into my life.",
    "Your patience and understanding are truly remarkable.",
    "You have a beautiful soul that shines through in everything you do.",
    "Your creativity and imagination are boundless sources of inspiration.",
    "You have a way of making people feel valued and appreciated.",
    "Your empathy and compassion make you a truly special person.",
    "You are a shining example of what it means to be a good human being.",
    "Your presence in my life is a constant source of joy and comfort.",
    "You have a way of making even the most challenging situations seem manageable.",
    "Your kindness and generosity know no bounds.",
    "You are an incredible person, and I'm lucky to have you in my life.",
    "Your smile brightens even the darkest of days.",
    "Your courage and bravery are truly admirable.",
    "You have a beautiful and pure heart that radiates kindness.",
    "Your positive energy is contagious and uplifting.",
    "You have a way of making people feel seen and heard.",
    "Your compassion and empathy make the world a better place.",
    "You are a beautiful soul, inside and out.",
    "Your determination and perseverance are truly inspiring.",
    "You have a way of making every moment feel special.",
    "Your kindness and generosity touch the lives of many.",
    "You are an amazing person, and I'm grateful to have you in my life.",
    "Your warmth and genuine nature make you a truly wonderful friend.",
    "You have a beautiful and caring heart that shines through in everything you do.",
    "Your positivity and optimism are truly contagious.",
    "You have a way of making people feel valued and appreciated.",
    "Your intelligence and wit never cease to impress me.",
    "You are a beautiful soul, and the world is better with you in it.",
    "Your kindness and compassion inspire me every day.",
    "You have a heart of gold, and it shows in everything you do.",
    "Your presence in my life is a constant source of joy and happiness."
]

# Wait for the Telegram window to open
time.sleep(5)  # Adjust this according to your system speed

# Loop to write 200 lovely messagesomaking people feeseen and heard.
for _ in range(600):
    message = random.choice(messages)  # Randomly select a message from the list
    pyautogui.write(message)
    pyautogui.press('enter')  # Press Enter key
    time.sleep(0.2)  # Add a delay between each message (adjust as needed)