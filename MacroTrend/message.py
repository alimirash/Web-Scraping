import pyautogui
import time
import random

# List of 50 lovely messages with emoji shortcodes
messages = [
    # English
    "You brighten my day with your smile. :sunny:",
    "Your kindness is a gift to the world. :gift:",
    "I'm so grateful to have you in my life. :pray:",
    "Your positivity is contagious and uplifting. :star2:",
    "You have a heart of gold. :yellow_heart:",
    "Your laughter is music to my ears. :musical_note:",
    "You inspire me to be a better person. :sparkles:",
    "Your support means the world to me. :earth_americas:",
    "You have a beautiful soul. :blossom:",
    "You deserve all the happiness in the world. :tada:",

    # Spanish
    "Iluminas mi día con tu sonrisa. :sun_with_face:",
    "Tu amabilidad es un regalo para el mundo. :gift_heart:",
    "Estoy muy agradecido de tenerte en mi vida. :folded_hands:",
    "Tu positividad es contagiosa e inspiradora. :raised_hands:",
    "Tienes un corazón de oro. :gold_heart:",
    "Tu risa es música para mis oídos. :notes:",
    "Me inspiras a ser una mejor persona. :sparkle:",
    "Tu apoyo significa el mundo para mí. :globe_with_meridians:",
    "Tienes un alma hermosa. :hibiscus:",
    "Mereces toda la felicidad del mundo. :party_popper:",

    # French
    "Tu illumines ma journée avec ton sourire. :sun_behind_small_cloud:",
    "Ta gentillesse est un cadeau pour le monde. :gift_box:",
    "Je suis si reconnaissant de t'avoir dans ma vie. :pray_tone1:",
    "Ta positivité est contagieuse et édifiante. :dizzy:",
    "Tu as un cœur en or. :orange_heart:",
    "Ton rire est une musique à mes oreilles. :musical_score:",
    "Tu m'inspires à être une meilleure personne. :glowing_star:",
    "Ton soutien signifie le monde pour moi. :earth_africa:",
    "Tu as une belle âme. :cherry_blossom:",
    "Tu mérites tout le bonheur du monde. :confetti_ball:",

    # German
    "Du erhellst meinen Tag mit deinem Lächeln. :sun_behind_rain_cloud:",
    "Deine Freundlichkeit ist ein Geschenk für die Welt. :ribbon:",
    "Ich bin so dankbar, dich in meinem Leben zu haben. :pray_tone2:",
    "Deine Positivität ist ansteckend und erhebend. :star:",
    "Du hast ein Herz aus Gold. :heart_decoration:",
    "Dein Lachen ist Musik in meinen Ohren. :musical_keyboard:",
    "Du inspirierst mich, ein besserer Mensch zu sein. :crystal_ball:",
    "Deine Unterstützung bedeutet mir die Welt. :earth_asia:",
    "Du hast eine wunderschöne Seele. :rose:",
    "Du verdienst alles Glück der Welt. :balloon:",

    # Italian
    "Illumini la mia giornata con il tuo sorriso. :partly_sunny:",
    "La tua gentilezza è un dono per il mondo. :gift_heart:",
    "Sono così grato di averti nella mia vita. :pray_tone3:",
    "La tua positività è contagiosa e edificante. :glowing_star:",
    "Hai un cuore d'oro. :sparkling_heart:",
    "La tua risata è musica per le mie orecchie. :musical_keyboard:",
    "Mi ispiri a essere una persona migliore. :dizzy:",
    "Il tuo supporto significa il mondo per me. :earth_africa:",
    "Hai un'anima bellissima. :tulip:",
    "Meriti tutta la felicità del mondo. :partying_face:"
]

# Wait for the Telegram window to open
time.sleep(5)  # Adjust this according to your system speed

# Loop to write 200 lovely messagesomaking people feeseen and heard.
for _ in range(3):
    message = random.choice(messages)  # Randomly select a message from the list
    pyautogui.write(message)
    pyautogui.press('space')  # Press Enter key
    time.sleep(0.1)  # Add a delay between each message (adjust as needed)