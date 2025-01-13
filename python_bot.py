from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
import time

# Configure the WebDriver
driver = webdriver.Chrome()  # Ensure you have the right WebDriver installed

# Open the target website
driver.get("https://www.wpromote.com/contact")

# Example of filling out a form quickly
for _ in range(20):  # Number of rapid submissions
    try:
        # Find form fields and fill them out

        #define menu
        dropdown = driver.find_element(By.CLASS_NAME, "contactintro-cell")
        dropdown.click()

        #select option
        button = driver.find_element(By.XPATH, "//button[@value='partner']")
        button.click()

        #fill out the forms

        #first form
        input_field = driver.find_element(By.XPATH, "//input[@aria-label='Name']")
        input_field.send_keys("John Doe")

        #second form
        input_field = driver.find_element(By.XPATH, "//input[@aria-label='Title']")
        input_field.send_keys("Engineer")

        #third form
        input_field = driver.find_element(By.XPATH, "//input[@aria-label='Email']")
        input_field.send_keys("test@wpromote.com")

        #fourth form
        input_field = driver.find_element(By.XPATH, "//input[@aria-label='Company Name']")
        input_field.send_keys("test")

        #fifth form
        input_field = driver.find_element(By.XPATH, "//input[@aria-label='Phone']")
        input_field.send_keys("5555555555")

        #sixth form
        input_field = driver.find_element(By.XPATH, "//input[@aria-label='URL']")
        input_field.send_keys("test.com")

        #second dropdown menu
        dropdown2 = driver.find_element(By.XPATH, "//div[@class='contactintro-page' and @data-contact-section='partner']")
        dropdown2.click()

        #select option
        button = driver.find_element(By.XPATH, "//button[@value='referral']")
        button.click()

        #click submit
        submit_button = driver.find_element(By.CSS_SELECTOR, "button[type='submit'].button.button--basic")
        submit_button.click()
        # Wait briefly before the next submission
        time.sleep(1)  # Very short delay to simulate rapid actions

        # Go back to the form page if necessary
        driver.get("https://www.wpromote.com/contact")
    except Exception as e:
        print("Error during submission:", e)
        break

driver.quit()
