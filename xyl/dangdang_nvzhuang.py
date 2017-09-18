from selenium import webdriver
import time
from lxml import etree

if __name__ == "__main__":
    driver = webdriver.Firefox()
    driver.get("http://www.dangdang.com")
    txt = driver.find_element_by_id("key_S")
    time.sleep(3)
    txt.send_keys("裙子")
    driver.find_element_by_class_name("button").click()
    time.sleep(15)
    for i in range(150):
        driver.execute_script("document.documentElement.scrollTop="+str(i*100))
    time.sleep(10)
    html = etree.HTML(driver.page_source)
    imgs = html.xpath("//ul[@class='bigimg cloth_shoplist']/li//a/img/@src")

    for i in imgs:
        print(i)
