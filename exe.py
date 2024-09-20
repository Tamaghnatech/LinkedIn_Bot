from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import random

# --------------------------------------
# Step 1: LinkedIn Login Function
# --------------------------------------
def login_to_linkedin():
    """
    Automates logging into LinkedIn using the provided credentials.
    Opens Chrome, navigates to LinkedIn login page, and logs in.
    """
    # Set up ChromeDriver with the correct path
    service = Service("/usr/local/bin/chromedriver")  # Ensure the correct path to chromedriver
    driver = webdriver.Chrome(service=service)

    # Navigate to LinkedIn login page
    driver.get('https://www.linkedin.com/login')

    # Wait for the login page to load (max 10 seconds)
    wait = WebDriverWait(driver, 10)
    username = wait.until(EC.presence_of_element_located((By.NAME, 'session_key')))
    password = driver.find_element(By.NAME, 'session_password')

    # Enter your LinkedIn login credentials
    username.send_keys("nagtamaghna@gmail.com")
    password.send_keys("04011999@eric")

    # Submit the login form
    password.send_keys(Keys.RETURN)

    # Wait a few seconds to allow the login to complete
    time.sleep(5)
    return driver

# --------------------------------------
# Step 2: Search for Profiles Function
# --------------------------------------
def search_for_profiles(driver):
    """
    Automates the search for LinkedIn profiles based on specific keywords.
    """
    # Navigate to LinkedIn's search URL with keywords like 'Data Science', 'AI', and 'ML'
    search_query = "https://www.linkedin.com/search/results/people/?keywords=data%20science%20ai%20ml"
    driver.get(search_query)

    # Wait for the search results to load
    time.sleep(5)  # Adjust the sleep time as necessary

    # Scrape profile 'Connect' buttons from the search results using the refined XPath
    connect_buttons = driver.find_elements(By.XPATH, "//button[.//span[contains(text(), 'Connect')]]")

    return connect_buttons

# --------------------------------------
# Step 3: Send Connection Requests Function
# --------------------------------------
def send_connection_requests(driver, connect_buttons):
    """
    Automates sending connection requests to LinkedIn profiles found in the search results.
    """
    for button in connect_buttons[:100]:  # Limit to first 20 people for demonstration
        try:
            # Scroll to the button and click it
            driver.execute_script("arguments[0].scrollIntoView(true);", button)
            time.sleep(1)
            button.click()  # Click 'Connect' button

            # Wait for the 'Send' button to be available and click it
            time.sleep(2)

            try:
                send_button = driver.find_element(By.XPATH, "//button[contains(text(), 'Send')]")
                send_button.click()
                print("Connection request sent.")
            except:
                print("No 'Send' button, moving to next profile.")

        except Exception as e:
            print(f"Could not send connection request: {e}")

        # Random delay to avoid detection by LinkedIn
        time.sleep(random.uniform(5, 10))  # Adjust the delay as needed

# --------------------------------------
# Main Script
# --------------------------------------
if __name__ == "__main__":
    # Step 1: Login to LinkedIn
    driver = login_to_linkedin()

    # Step 2: Search for profiles with specific keywords
    connect_buttons = search_for_profiles(driver)

    # Step 3: Send connection requests to the first 20 profiles
    send_connection_requests(driver, connect_buttons)

    # Step 4: Close the browser
    input("Press Enter to close the browser...")
    driver.quit()
    
    
