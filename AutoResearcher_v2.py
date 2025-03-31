import random
import time
import nltk
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.edge.service import Service as EdgeService
from nltk.corpus import words

# Scarica il vocabolario di parole solo una volta
nltk.download('words')

# Usa il vocabolario di parole inglesi
word_list = words.words()

def choose_random_word():
    """Select a random word from the nltk words corpus."""
    return random.choice(word_list)

# Configurazione del driver di Edge (verifica il percorso del driver)
edge_driver_path = r"C:\\Users\\Admin\\Documents\\Microsoft Rewards Bot\\Microsoft Rewards Bot\\msedgedriver.exe"
edge_options = webdriver.EdgeOptions()
edge_service = EdgeService(executable_path=edge_driver_path)
driver = webdriver.Edge(options=edge_options, service=edge_service)

# Apri il motore di ricerca
driver.get("https://www.bing.com")

# Lista per salvare le parole selezionate
current_words = []

# Esegui la ricerca per 30 iterazioni
for _ in range(30):
    new_word = choose_random_word()  # Scegli una nuova parola casuale

    # Lancio della moneta: decide se mantenere le parole precedenti o sostituirle
    if random.choice([True, False]):
        current_words.append(new_word)  # Mantieni tutte le parole precedenti
    else:
        current_words = [new_word]  # Sostituisci con la nuova parola

    # Unisci tutte le parole selezionate in una stringa per la ricerca
    search_query = ' '.join(current_words)

    # Esegui la ricerca nel motore
    search_box = driver.find_element("name", "q")
    search_box.clear()  # Pulisci eventuali termini precedenti
    search_box.send_keys(search_query)
    time.sleep(1)  # Ritardo per simulare la digitazione
    search_box.send_keys(Keys.RETURN)
    attesa = random.randint(5,20)
    time.sleep(attesa)  # Attendi il caricamento dei risultati

# Chiudi il browser dopo il ciclo
driver.quit()
