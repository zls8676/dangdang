from bs4 import BeautifulSoup

if __name__ == "__main__":
    text = '''
    <div>
        <ul>
             <li class="item-0">
               <a href="link1.html">first item</a>
               <a href="link1.html">数据库</a>
             </li>
             <li class="item-1">
               <a href="link2.html">second item</a>
               <a href="link2.html">22222</a>
             </li>
         </ul>
     </div>
    '''
    bs = BeautifulSoup(text,"lxml")
    li_arr = bs.find("ul").contents
    # print((li_arr[1].contents[1].string))
    for i in range(1,len(li_arr)-1,2):
        title = li_arr[i].contents[1].string
        price = li_arr[i].contents[3].string
        print(title + "," + price)

        # for li in range():
        # title = li.contents
    # li = bs.find("li",attrs={"class":"item-1"}).contents
    # a = bs.find("a").["href"]
    # li = bs.find("ul")
    # b = a
    # print(li)
