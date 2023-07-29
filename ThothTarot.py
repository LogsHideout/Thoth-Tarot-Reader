import random
from colorama import Fore, Style

# creates a list of cards
cards = [
      "The Fool: Represents new beginnings, potential, and spontaneity", "The Magus: Symbolizes manipulation of the elements, creativity, and manifestation", "The Priestess: Represents intuition, subconciousness, and feminine energy", "The Empress: Symbolizes fertility, abundance, and nurturing energy", "The Emperor: Represents authority, structure, and guidance",
        "The Hierphant: Symbolizes traditon, institutions, and spiritual guidance", "The Lovers: Represents partnership, choices, and harmony", "The Chariot: Represents willpower, determination, and control.", "Adjustment: Symbolizes balance, fairness, and karmic consenquences", "The Hermit: Represents solitude. introspection, and seeking inner guidance",
        "Fortune: Symbolizes destiny, changes and cycles of life", "Lust: Represents inner stength, courage, and passion", "The Hanged man: Symbolizes surrender, self-sacrifice, and gaining a new perspective", "Death: Represents transformation, endings, and rebirth", "Art: Symbolizes harmony, moderation, and blending opposing forces", "The Devil: Represents materialism, addictions, and illusions", "The Tower: Symbolizes upheaval, sudden change, and destruction of old structures",
        "The Star: Represents hope, inspiration, and inner guidance", "The Moon: Symbolizes intuition, emotions, and the subconscious mind", "The Sun: Represents vitality, positivity, and success", "Aeon: Symbolizes spiritual awakening, transformation, and self-realization", "The Universe: Represents completion, fullfillment, and integration", 
	"Ace of Wands: Represents new beginnings, creative potential, and the spark of inspiration", "Two of Wands: Symbolizes planning, forsight, and making decisions about future endeavors", "Three of Wands: Signifies enterprise, exploration and the realization of initial efforts", "Five of Wands: Symbolizes competition,conflict, and challenges that can lead to growth and improvement", "Four of Wands: Represents celebration, harmony, and the fulfillment of creative projects.", "Six of Wands: Signifies victory, public recognition, and sucess after overcoming obstacles", "Seven of Wands: Represents courage, determination, and standing up for one's beliefs in th face of opposition", "Eight of Wands: Symbolizes swift action, progress, and the rapid advancement of plans or projects", "Nine of Wands: Signifies resillence, perserverance, and the ability to keep on going despite obstacles", "Ten of Wands: Represents the burden responsibility, feeling overwhelmed, and the need to delegate or let go", "Princess of Wands: Symbolizes exploration enthusiasm, and the youthful, adventurous spirit", "Prince of Wands: Represents charismatic leadership, a daring approach, and the pursuit of vision", "Queen of Wands: Signifies confidence, independence, and the ability to inspire others with passion", "King of Wands: Symbolizes vision, charisma, and strong leadership in creative and spiritual endeavors", 
	"Ace of Cups: Represents love, emotional abundance, and the potential for deep emotional connections", "Two of Cups: Symbolizes harmony, partnership, and the coming together of two souls.", "Three of cups: Signifies celebration, friendship, and joyful gatherings with loved ones", "Four of Cups: Represents contemplation, introspection, and a need to reevaluate emotional matters.", "Five of Cups: Symbolizes loss, disappointment, and the need to reevaluate emotional matters", "Five of Cups: Symbolizes loss, dissapointment, and the need to find solace and acceptance in difficult times", "Six of Cups: Represents nostalgia, innocence, and fond memories of the past", "Seven of Cups: Represents choices, imagination, and the need to focus on realistic goals", "Eight of Cups: Symbolizes a turning point, the search for deeper meaning, and the journey to find ones true self", "Nine of Cups: signifies emotional fullfillment, contentment, and having one's wishes granted", "Ten of Cups: Represents happiness, harmony, and emotional fullfillment within family and relationships", "Princess of Cups: Symbolizes sensitivity, artistic expression, and the exploration of emotions", "Prince of Cups: Signifies introspection, emotional depth, and the need to balance emotions", "Queen of Cups: Represents empathy, compassion, and the nurturing of others and oneself", "King of Cups: Symbolizes emotional maturity, wisdom, and the ability to handle emotions with grace and understanding",
	"Ace of Disks: Represents the potential for material and financial growth, new opportunities, and the seed of prosperity", "Two of Disks: Symbolizes balance, adaptability, and the need to juggle different aspects of life effectively", "Three of Disks: Signifies teamwork, collaboration, and the successful realization of a shared goal or project", "Four of Disks: Represents stability, security, and the need to establish solid foundations in material matters", "Five of Disks: Symbolizes financial challenges, loss, and the need to seek support during difficult times", "Six of Disks: Signifies generosity, success, and the rewards of sharing one's abundance with others", "Seven of Disks: Represents assessment, patience, and the ned to reevaluate long-term goals and progress", "Eight of Disks: Symbolizes dilligence, skill development, and the steady progress towards mastery", "Nine of Disks: Signifies material gain, self sufficiency, and the manifestation of long-term efforts", "Ten of Disks: Represents wealth, family prosperity, and the fullfillment of material and generational ambitions", "Princess of Disks: Symbolizes practicality, growth, and the nurturing of ones dreams and aspirations", "Prince of disks: Signifies determination, responsibility, and the ability to manifest ideas into the physical world", "Queen of Disks: Represents abundance, nurturing, and the wise management of resources", "King of Disks: Symbolizes prosperity, stability, and the ability to provide for oneself and others with practicality and wisdom",
	"Ace of Swords: Represents mental clarity, breakthroughs, and the power of the mind to cut through illusions", "Two of Swords: Symbolizes indecision, the need to make a choice, and finding balance between opposing forces", "Three of Swords: Signifies heartache, emotional pain, and th need to confront and heal from difficult emotions", "Four of Swords: Represents rest, contemplation, and the need for a mental break or time to recover", "Five of Swords: Symbolizes conflict, defeat, and the imprtance of considering the impact of actions on others", "Six of Swords: Signifies transition, moving away from troubles, and embarking on a journey torwards peace", "Seven of Swords: Represents deception, cunning, and the need to be cautious of hidden motives", "Eight of Swords: Symbolizes feeling trapped, limiting beliefs, and the importance of finding inner strength", "Nine of Swords: Signifies anxiety, nightmares, and the need to address and release mental burdens", "Ten of Swords: Represents the end of a difficult cycle, acceptance of change, and the potential for renewal", "Princess of Swords: Symbolizes curiosity, intellect, and the pursuit through communication", "Prince of Swords: Signifies determination, decisivness, and th ability to take swift action", "Queen of Swords: Represents clear perception, independence, and the wisdom to make fair judgments", "King of Swords: Symbolizes intellectual power, leadership, and the ability to communicate with authority"
]

# function to randomly select the cards
def get_tarot_card():
    if len(cards) == 0:
        return "No more cards remaining."
    card = random.choice(cards)
    cards.remove(card)
    return card
# main function for reading
def tarot_reading():
    print(Fore.YELLOW + Style.BRIGHT + "Welcome to thoth tarot reader ☥ \nplease note interpretations can vary depending on the reading.")
    while True:
        question = input("Ask a question or type quit to exit: ")
        if question.lower() == "quit":
            break
        else:
            num_cards = int(input("Enter the number of cards you would like to draw (4-8 recommended): "))
            print(Fore.CYAN + Style.BRIGHT + "\nTarot cards drawn for your question:")
            for _ in range(num_cards):
                tarot_card = get_tarot_card()
                print(tarot_card + "\n")
            print(Fore.YELLOW + Style.BRIGHT) 

# run tarot reading
tarot_reading()





