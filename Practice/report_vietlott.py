# -*- coding: utf-8 -*-
import requests
from bs4 import BeautifulSoup

request = requests.get("http://www.johnlewis.com/john-lewis-wade-office-chair-black/p447855")
content = request.content
soup = BeautifulSoup(content, "html.parser")

# <span itemprop="name">John Lewis Wade Office Chair, Black</span>
element_name = soup.find("span", {"itemprop": "name"})
print("Item: {}".format(element_name.text.strip()) )

# <span itemprop="price" class="now-price"> £99.00 </span>
element_price = soup.find("span", {"itemprop": "price", "class": "now-price"})
string_price = element_price.text.strip()
print("Price: £{}".format(float(string_price[1:])) )

request = requests.get("http://www.hanoicomputer.vn/pc-dell-vostro-3650st-7cgwc31-pyypd1-skylake-moi-nhat-kieu-dang-mini-tower/p31160.html")
content = request.content
soup = BeautifulSoup(content, "html.parser")

# <h1>PC Dell Vostro 3650MT PYYPD1 Skylake mới nhất, kiểu dáng Mini Tower</h1>
element_name = soup.find("h1")
print("Item: {}".format(element_name.text.encode('utf-8').strip()) )

# <p class="float_l red">Mã SP: PCDE215</p>
element_code = soup.find("p", {"class": "float_l red"})
print("Code: {}".format(element_code.text.encode('utf-8').strip()) )
