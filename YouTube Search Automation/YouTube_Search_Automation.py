from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# Launch the Chrome browser
driver = webdriver.Chrome()

# Navigate to YouTube
driver.get('https://www.youtube.com/')
time.sleep(5)

# Find the search input field and enter a query
elem = driver.find_element(By.XPATH, '//input[@id="search"]')
elem.clear()  # Clear any existing text in the search field
elem.send_keys('pamidorov dzvadzex')  # Enter the search query
time.sleep(3)

# Find and click the search button
clickButton = driver.find_element(By.ID, "search-icon-legacy")
clickButton.click()

# Wait for the search results to load
time.sleep(3)

# Find and click the first video in the search results
firstLink = driver.find_element(By.XPATH, '(//a[@id="video-title"])[1]')
firstLink.click()

# Wait for 80 seconds before closing the browser
time.sleep(80)
driver.quit()  # Close the browser

