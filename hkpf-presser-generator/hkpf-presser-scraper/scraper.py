from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup


def scrape_presser(url):
    driver = webdriver.Chrome("E:\dev\lib\chromedriver.exe")
    driver.get(url)
    try:
        element = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CLASS_NAME, "acc-content"))
         )
    finally:
        result = ""
        soup = BeautifulSoup(driver.page_source, 'html.parser')
        contents = soup.find_all(class_="acc-content")

        for content in contents:
            paragraphs = content.find_all("p")
            for paragraph in paragraphs:
                result += paragraph.get_text()
            result += "\n"

        driver.close()
        return result