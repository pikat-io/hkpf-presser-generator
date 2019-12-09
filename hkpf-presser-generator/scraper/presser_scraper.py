from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup

class PresserScraper(object):
    def scrape_new_presser(self, url):
        driver = webdriver.Chrome("E:\dev\lib\chromedriver.exe")
        driver.get(url)
        try:
            element = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.CLASS_NAME, "acc-content"))
             )
        finally:
            result = ""
            soup = BeautifulSoup(driver.page_source, 'html.parser')
            content = soup.find_all(class_="acc-content")

            for r in content:
                result += r.get_text()

            driver.close()
            return result