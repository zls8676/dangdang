import requests
from  lxml import

if __name__ = "__main__":
    data = {}
    res = requests.post("https://www.lagou.com/jobs/list_python?labelWords=&fromSearch=true&suginput=")
    html = etree.HTML(res.text)
    print(res.text)