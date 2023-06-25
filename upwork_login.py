import time
import os
from pathlib import Path
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager as CM
from selenium.webdriver.common.keys import Keys

options = webdriver.ChromeOptions()
options.add_argument('--log-level=3')
options.add_argument(f"--user-data-dir={os.getcwd()}\\profile")

# USE THIS IF YOU NEED TO HAVE MULTIPLE PROFILES
options.add_argument('--profile-directory=Profile 4')
mobile_emulation = {
    "userAgent": "Mozilla/5.0 (Linux; Android 4.2.1; en-us; Nexus 5 Build/JOP40D) AppleWebKit/535.19 (KHTML, like Gecko) Chrome/90.0.1025.166 Mobile Safari/535.19"}
options.add_experimental_option("mobileEmulation", mobile_emulation)
options.add_argument(
    "user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.212 Safari/537.36")
driver = webdriver.Chrome(options=options, executable_path=CM().install())

driver.get("https://www.upwork.com/ab/account-security/login")
if driver.title.find("Login"):
    login_username = driver.find_element_by_id("login_username")
    login_username.send_keys("YOUR_EMAIL_ADRESS")
    print("Email entered")
    driver.find_element_by_id("login_password_continue").click()
    time.sleep(10)
    driver.find_element_by_id("login_google_submit").submit()
    time.sleep(10)
    driver.save_screenshot("upwork_homepage.png")
    driver.quit()
else:
    print("Login successfull")
