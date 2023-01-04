from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

link = input("link:")
be = input("message:")
azanyi = int(input("how many messages:"))

driver = webdriver.Chrome()
driver.get(link)

for i in range(azanyi):
    try:
        
        elem = driver.find_element("name" ,"question")
        elem.send_keys(be)
        but = driver.find_element("xpath", "/html/body/div[1]/form/button").click()
        time.sleep(1)
        butt = driver.find_element("xpath", "/html/body/div[2]/a[2]").click()
        time.sleep(2)
        
    except:
        driver.close()
        driver = webdriver.Chrome()
        time.sleep(25)
        driver.get(link)
        
