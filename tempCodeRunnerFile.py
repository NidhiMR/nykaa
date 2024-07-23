from selenium import webdriver
from selenium.webdriver.common.by import By

# Replace with the path to your Chrome webdriver
driver = webdriver.Chrome("C:\Users\NIDHI\OneDrive\Documents\automation\chromedriver-win64\chromedriver.exe")

# Open Nykaa website
driver.get("https://www.nykaa.com/")

# Locate the search box using xpath
search_box = driver.find_element(By.XPATH, "//*[@id='headerMenu']/div[2]/div[1]/div/form/input")

# Type "lipstick" in the search box
search_box.send_keys("lipstick")

# Submit the search form (optional)
search_box.submit()

# Pause the script for a few seconds to allow the page to load
driver.implicitly_wait(5)

# Do something with the search results...

# Close the browser window
driver.quit()
