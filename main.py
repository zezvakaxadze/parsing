from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
import time
import runpy

# Replace these with your Facebook credentials
email = "511169358"
password = "gadaafdi1234"

# Set up the Chrome driver with the correct service
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

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

driver.get("https://www.facebook.com/groups/345682013717054/members")

time.sleep(10)

# Remove CSS and JavaScript
driver.execute_script("""
    var stylesheets = document.querySelectorAll('link[rel="stylesheet"], style');
    stylesheets.forEach(function(stylesheet) {
        stylesheet.parentNode.removeChild(stylesheet);
    });

    var scripts = document.querySelectorAll('script');
    scripts.forEach(function(script) {
        script.parentNode.removeChild(script);
    });
""")

# Scroll down to load all content
last_height = driver.execute_script("return document.body.scrollHeight")
while True:
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(2)  # Wait for new content to load
    new_height = driver.execute_script("return document.body.scrollHeight")
    if new_height == last_height:
        break
    last_height = new_height

# Save the page source
page_source = driver.page_source
with open("facebook_page.html", "w", encoding="utf-8") as file:
    file.write(page_source)

# Close the browser
driver.quit()


# Run file2.py as if it were the main program
runpy.run_path('get_link.py')
