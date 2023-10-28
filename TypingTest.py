from selenium import webdriver 
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import time
from pynput.keyboard import Key, Controller

global keyboard
# //div[contains(@class, "letters notranslate")]


def readLetters(driver):
    letters = driver.find_elements(By.XPATH, "//span[contains(@class, 'incomplete')]")
    return letters

def buildString(letters):
    # sentence = ""
    for letter in letters:
        if(len(letter.text) == 0):
            # sentence = sentence + " "
            keyboard.type(" ")
        else:
            keyboard.type(letter.text)
            # sentence += letter.text
    # return sentence

def typeLetters(driver):
    pass



websiteURL = 'https://humanbenchmark.com/tests/typing'
driver = webdriver.Firefox()
driver.get(websiteURL)

keyboard = Controller()


letters = readLetters(driver)
sentence = buildString(letters)

print(sentence)



time.sleep(8)

driver.quit()