from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import pandas as pd
import traceback

data = pd.read_csv('./contacts.csv')
phone_numbers = data['PhoneNumber'].tolist()

print(phone_numbers)

driver = webdriver.Chrome()
driver.get('https://web.whatsapp.com/')

input('Press any key after scanning QR code and logging in...')

for number in phone_numbers:
    try:
        url = f'https://web.whatsapp.com/send?phone={number}'
        driver.get(url)

        # Wait for the chat window to load
        chat_box = WebDriverWait(driver, 30).until(
            EC.presence_of_element_located((By.XPATH, '//div[@class="_1awRl copyable-text selectable-text"]')))

        # Enter a message and send it
        message_box = WebDriverWait(driver, 30).until(
            EC.presence_of_element_located((By.XPATH, '//div[@class="_3FRCZ copyable-text selectable-text"]')))
        message_box.send_keys('This is a test message while testing a bot')

        send_button = WebDriverWait(driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, '//span[@data-testid="send"]')))
        send_button.click()

        print(f"Message sent to {number}")

    except Exception as e:
        print(f"Error sending message to {number}: {str(e)}")
        print(traceback.format_exc())

driver.quit()