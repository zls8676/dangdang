from bs4 import BeautifulSoup

if __name__ = "__main__":
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
    li_all = bs.find("ul").contents
    for i in range(1,len(li_all)-1,2):
        title = li_all[i].contents[1].string
        price = li_arr[i].contents[1].string
        print(title + "," + prine)