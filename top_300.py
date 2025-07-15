from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time

# Start ChromeDriver
s = Service("C:/Users/DELL/OneDrive/Desktop/chromedriver.exe")
driver = webdriver.Chrome(service=s)

# Load the website
driver.get('https://www.failory.com/startups/india')

# Wait for content to load (can use WebDriverWait for better control)
time.sleep(15)

# Optional: Locate a specific element (not used here, so you can remove it)
# user_input = driver.find_element(By.XPATH, '//*[@id="failed-startup-text"]')

# Save full page HTML
with open('failory_india_startups.html', 'w', encoding='utf-8') as f:
    f.write(driver.page_source)

input("Press Enter to close the browser...")
driver.quit()
