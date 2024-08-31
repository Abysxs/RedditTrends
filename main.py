from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.edge.service import Service
from selenium.webdriver.edge.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import getpass


def main():
    url = "https://www.reddit.com/login/"
    open_reddit(url)

def open_reddit(url):
    # Correct path to your Edge WebDriver executable
    edge_driver_path = "C:/Users/ruben/webdrivers/edgedriver_win64/msedgedriver.exe"
    
    # Set up Edge options
    edge_options = Options()
    edge_options.add_argument('--ignore-certificate-errors')
    edge_options.add_argument('--ignore-ssl-errors')

    # Initialize the WebDriver with options
    service = Service(edge_driver_path)
    driver = webdriver.Edge(service=service, options=edge_options)

    driver.get(url)

    # This will wait until these fields are visible
    wait = WebDriverWait(driver, 5)
    usernameField = wait.until(EC.presence_of_element_located((By.ID, "login-username")))
    passwordField = wait.until(EC.presence_of_element_located((By.ID, "login-password")))

    time.sleep(5)

    # User inputs username and password
    usernameInput = input("Username: ")
    passwordInput = getpass.getpass("Password: ")

    # Sends the user's inputs into those field
    usernameField.send_keys(usernameInput)
    passwordField.send_keys(passwordInput)

    # Keep the browser open until manually closed
    input("Press Enter to exit and close the browser...")
    driver.quit()


if __name__ == "__main__":
    main()
