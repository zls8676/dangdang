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
    li = bs.find_all("a")
    for a in li:
        print(a.string)
