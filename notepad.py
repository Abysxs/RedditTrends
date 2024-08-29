from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.edge.service import Service
import time

def main():
    url = "https://www.reddit.com"
    open_reddit(url)

def open_reddit(url):
    # Correct path to your Edge WebDriver executable
    edge_driver_path = "C:/Users/ruben/webdrivers/edgedriver_win64/msedgedriver.exe"

    
    # Initialize the WebDriver
    service = Service(edge_driver_path)
    driver = webdriver.Edge(service=service)

    driver.get(url)

if __name__ == "__main__":
    main()