from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
import time
from selenium.webdriver.chrome.options import Options
import pyautogui

# Set Chrome options
chrome_options = Options()
chrome_options.add_argument("--start-fullscreen")
chrome_options.add_argument("--disable-notifications")

# Replace these with your Facebook credentials
email = "511169358"
password = "gadaafdi1234"

# Set up the Chrome driver with the correct service
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(options=chrome_options, service=service)

# Open Facebook
driver.get("https://www.facebook.com")

# Find the email and password input fields
email_field = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.ID, "email"))
)
password_field = driver.find_element(By.ID, "pass")

# Enter your credentials
email_field.send_keys(email)
password_field.send_keys(password)

# Submit the form
password_field.send_keys(Keys.RETURN)

# Wait for a while to let the login process complete
time.sleep(5)

driver.get("https://www.facebook.com/nato.gordiashvili")

time.sleep(10)

message_center = pyautogui.locateOnScreen("message.PNG")

center_x = message_center.left + (message_center.width/2)
center_y = message_center.top + (message_center.height/2)
center_tuple = (int(center_x), int(center_y))

pyautogui.moveTo(center_tuple)
pyautogui.click()

time.sleep(10)

text_center = pyautogui.locateOnScreen("text.PNG")

center_x = text_center.left + (text_center.width/2)
center_y = text_center.top + (text_center.height/2)
center_tuple = (int(center_x), int(center_y))

pyautogui.moveTo(center_tuple)
pyautogui.click()

pyautogui.write("es mesiji chemma programam gamoagzavna")
pyautogui.hotkey("enter")
