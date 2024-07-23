from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import random

# Path to your web driver executable inside the 'chromedriver-win64' folder
driver_path = 'chromedriver-win64/chromedriver.exe'
nykaa_url = 'https://www.nykaa.com/'

# Configure WebDriver options
chrome_options = Options()
chrome_options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36")
chrome_options.add_argument("--start-maximized")  # Open browser in maximized mode
# chrome_options.add_argument("--headless")  # Uncomment if you want to use headless mode

# Create a Service object with the path to the web driver
service = Service(driver_path)

# Initialize the webdriver with the service object and options
driver = webdriver.Chrome(service=service, options=chrome_options)

try:
    # Open the Nykaa website
    driver.get(nykaa_url)

    # Introduce a random delay to mimic human interaction
    time.sleep(random.uniform(5, 10))

    # Use WebDriverWait to wait until the "Categories" dropdown is clickable
    wait = WebDriverWait(driver, 15)
    categories_dropdown = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="category_arrowUp"]')))

    # Click on the "Categories" dropdown
    categories_dropdown.click()

    # Introduce a random delay to mimic human interaction
    time.sleep(random.uniform(5, 10))

finally:
    # Close the browser
    driver.quit()
