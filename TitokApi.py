from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from bs4 import BeautifulSoup
from time import sleep


class TiktokApi:
    def run(self):
        driver = webdriver.Chrome()
        driver. get ("https://www.tiktok.com/@waterdstrawhat")
        sleep(5)
        
        soup = BeautifulSoup(driver.page_source,"html.parser")
        print(soup.prettify())
        webpage = soup.find_all("div",{"class":"css-1as5cen-DivWrapper e1cg0wnj1"})
        try:
            print(vidoes)
        except:
            raise Exception( driver.page_source, "page name??")
        
t = TiktokApi()
t.run()