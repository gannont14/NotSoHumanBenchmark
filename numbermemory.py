
from selenium import webdriver 
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import time
from pynput.keyboard import Controller, Key

# //div[contains(@class, 'big-number')]


websiteURL = 'https://humanbenchmark.com/tests/number-memory'

driver = webdriver.Firefox()
driver.get(websiteURL)

keyboard = Controller()


# begin  button
begin = driver.find_element(By.XPATH, "//button[contains(@class, 'css-de05nr e19owgy710')]")
begin.click()


# find bignumber

number = driver.find_element(By.XPATH, " //div[contains(@class, 'big-number')]")

# for divClass css-1qvtbrk e19owgy78
keyboard.type(str(number))
keyboard.press(Key.enter)
keyboard.release(Key.enter)

# inputClass = driver.find_element(By.XPATH, "//div[contains(@class, 'css-1qvtbrk e19owgy78')]//input")




# looping portion
max = 10
count = 0


while count < max:
    time.sleep(1)
    while True:
        try:
            number = driver.find_element(By.XPATH, " //div[contains(@class, 'big-number')]").text
        except: 
            print("Endnum")
            break
#   break and input number into form

    keyboard.type(str(number))
    keyboard.press(Key.enter)
    keyboard.release(Key.enter)
    # set count for score you want
    count+=1

time.sleep(15)
driver.quit()
# press begin