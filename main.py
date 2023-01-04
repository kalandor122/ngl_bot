from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

link = input("link:")
be = input("mit:")
azanyi = int(input("hányszor:"))

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
        if i / 5 == True:
            driver.close()
            driver = webdriver.Chrome()
            driver.get(link)

            elem = driver.find_element("name" ,"question")
            elem.send_keys(be)
            but = driver.find_element("xpath", "/html/body/div[1]/form/button").click()
            time.sleep(1)
            butt = driver.find_element("xpath", "/html/body/div[2]/a[2]").click()
            time.sleep(2)
    except:
        driver.close()
        driver = webdriver.Chrome()
        driver.get(link)
        
