from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep
from getpass import getpass
from open_reddit import open_reddit

def main():
    url = "https://www.reddit.com/"
    driver = open_reddit(url)
    
    # This will wait until the login button on the homepage is clickable
    wait = WebDriverWait(driver, 10)
    login_button = wait.until(EC.element_to_be_clickable((By.ID, "login-button")))
    login_button.click()

    # Wait until username and password fields in the modal are visible
    usernameField = wait.until(EC.presence_of_element_located((By.ID, "login-username")))
    passwordField = wait.until(EC.presence_of_element_located((By.ID, "login-password")))

    sleep(5)

    # User inputs username and password
    usernameInput = input("Username: ")
    passwordInput = getpass("Password: ")

    # Sends the user's inputs into those fields
    usernameField.send_keys(usernameInput)
    passwordField.send_keys(passwordInput)


    passwordField.send_keys(Keys.ENTER)

    sleep(10)

    # Keep the browser open until manually closed
    input("Press Enter to exit and close the browser...")
    driver.quit()


main()
