from selenium import webdriver
import time

if __name__ =="__main__":
    driver = webdriver.Firefox()
    driver.get("http://www.dangdang.com")
    txt = driver.find_element_by_id("key_S")
    time.sleep(3)
    txt.send_keys("python")
    driver.find_element_by_class_name("button").click()
    time.sleep(15)
    driver.execute_script("document.documentElement.scrollTop=15000")
