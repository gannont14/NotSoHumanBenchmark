from selenium import webdriver 
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import time
# //div[@class="word"]


websiteURL = 'https://humanbenchmark.com/tests/verbal-memory'

driver = webdriver.Firefox()
driver.get(websiteURL)

# select start button
startButton = driver.find_element(By.XPATH, "//button[@class='css-de05nr e19owgy710']")
startButton.click()

buttons = driver.find_elements(By.XPATH, "//button[@class='css-de05nr e19owgy710']")

seenButton = buttons[0]
newButton = buttons[1]

time.sleep(1)

wordSet = {""}
# find word, check if in set, if in set, select seen, otherwise click new
while(True):
    word = driver.find_element(By.XPATH, "//div[contains(@class, 'word')]")
    print(word)
    if word.text in wordSet:
        seenButton.click()
    else:
        wordSet.add(word.text)
        newButton.click()
    print(len(wordSet))
    time.sleep(0.05)