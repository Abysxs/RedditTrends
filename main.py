from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.edge.service import Service
from selenium.webdriver.edge.options import Options
import time

def main():
    url = "https://www.reddit.com"
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
    # Keep the browser open until manually closed
    input("Press Enter to exit and close the browser...")
    driver.quit()

if __name__ == "__main__":
    main()
