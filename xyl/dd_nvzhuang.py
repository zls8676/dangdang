from selenium import webdriver
import time
from lxml import etree
import requests
import os

def downloan(img):
    myheader = {
        "User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) "
                      "AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.115 Safari/537.36"}
    res = requests.get(img, headers=myheader)
    arr = os.path.split(img)
    filename = arr[-1]
    with open(filename, "wb") as writer:
        writer.write(res.content)
if __name__ == "__main__":
    driver = webdriver.Firefox()
    driver.get("http://www.dangdang.com")
    txt = driver.find_element_by_id("key_S")
    # time.sleep(3)
    txt.send_keys("裙子")
    driver.find_element_by_class_name("button").click()
    time.sleep(15)
    for i in range(150):
        driver.execute_script("document.documentElement.scrollTop=" + str(i * 100))
    time.sleep(10)
    html = etree.HTML(driver.page_source)
    imgs = html.xpath("//ul[@class='bigimg cloth_shoplist']/li//a/img/@src")
    for i in imgs:
        downloan(i)
        # print(i)