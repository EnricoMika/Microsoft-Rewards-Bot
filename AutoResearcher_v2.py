import random
import time
import nltk
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.edge.service import Service as EdgeService
from nltk.corpus import words

# Download the vocabulary (only the first time)
nltk.download('words')

# Use english words vocabulary
word_list = words.words()

def choose_random_word():
    """Select a random word from the nltk words corpus."""
    return random.choice(word_list)

# Configuring Edge Driver (check driver path)
edge_driver_path = r"C:\\Users\\Admin\\Documents\\Microsoft Rewards Bot\\Microsoft Rewards Bot\\msedgedriver.exe" #put inside the "..." the path where you downloaded the driver:; remember to use \\ as the example
edge_options = webdriver.EdgeOptions()
edge_service = EdgeService(executable_path=edge_driver_path)
driver = webdriver.Edge(options=edge_options, service=edge_service)

# Open the search engine
driver.get("https://www.bing.com")

# List to save selected words
current_words = []

# Run research for 30 iterations
for _ in range(30):
    new_word = choose_random_word()  # Choose a new random word

        # Flip a coin: decides if maintaining the previous words or replacing them
    if random.choice([True, False]):
        current_words.append(new_word)  # Keep the previous words
    else:
        current_words = [new_word]  # Replace them with a new word

    # Join all selected words into one search string
    search_query = ' '.join(current_words)

    # Perform search in the engine
    search_box = driver.find_element("name", "q")
    search_box.clear()  # Clean up any previous words
    search_box.send_keys(search_query)
    time.sleep(1)  # Delay to simulate typing
    search_box.send_keys(Keys.RETURN)
    attesa = random.randint(5,20)
    time.sleep(attesa)  # Wait for results to load
    
# Close browser after cycle
driver.quit()
