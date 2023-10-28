from selenium import webdriver 
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import time


websiteURL = 'https://humanbenchmark.com/tests/aim'

driverPath = '/Users/gannontubbs/Downloads/geckodriver'

driver = webdriver.Firefox()
driver.get(websiteURL)

# targetDiv = driver.find_element_by_xpath('//div[contains(@class, "css-1k4dpwl e6yfngs0")]')

count = 0


# css-q4kt6s e6yfngs1

# count < 10


startTargetDiv = driver.find_element(By.XPATH, '//div[contains(@class, "css-1k4dpwl e6yfngs0")]')
startTargetDiv.click()

while(count < 30):
    targetDiv = driver.find_element(By.XPATH, '//div[contains(@class, "css-ad1j3y e6yfngs2")]')
    ActionChains(driver).move_to_element(targetDiv).click().perform()

    
    count += 1


time.sleep(30)


driver.quit()