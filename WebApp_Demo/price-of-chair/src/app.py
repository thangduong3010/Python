# -*- coding: utf-8 -*-
import requests
from bs4 import BeautifulSoup

# request = requests.get("http://www.johnlewis.com/john-lewis-wade-office-chair-black/p447855")
# content = request.content
# soup = BeautifulSoup(content, "html.parser")
#
# # <span itemprop="name">John Lewis Wade Office Chair, Black</span>
# element_name = soup.find("span", {"itemprop": "name"})
# print("Item: {}".format(element_name.text.strip()) )
#
# # <span itemprop="price" class="now-price"> £99.00 </span>
# element_price = soup.find("span", {"itemprop": "price", "class": "now-price"})
# string_price = element_price.text.strip()
# print("Price: £{}".format(float(string_price[1:])) )
#
# request = requests.get("http://www.hanoicomputer.vn/pc-dell-vostro-3650st-7cgwc31-pyypd1-skylake-moi-nhat-kieu-dang-mini-tower/p31160.html")
# content = request.content
# soup = BeautifulSoup(content, "html.parser")
#
# # <h1>PC Dell Vostro 3650MT PYYPD1 Skylake mới nhất, kiểu dáng Mini Tower</h1>
# element_name = soup.find("h1")
# print("Item: {}".format(element_name.text.encode('utf-8').strip()) )
#
# # <p class="float_l red">Mã SP: PCDE215</p>
# element_code = soup.find("p", {"class": "float_l red"})
# print("Code: {}".format(element_code.text.encode('utf-8').strip()) )


frequency = {}
def get_lucky_number(url):
    request = requests.get(url)
    content = request.content
    soup = BeautifulSoup(content, "html.parser")

    element_name = soup.find("span")
    for tag in soup.findAll("span", attrs={'class': None, 'aria-hidden': None}):
        if tag.find("img") or tag.text.encode('utf-8').strip() in ('Ngày', 'Giờ', 'Phút', 'Giây'):
            continue
        lucky_number = tag.text.encode('utf-8')
        if lucky_number not in frequency:
            frequency[lucky_number] = 1
        else:
            frequency[lucky_number] += 1


# PAGE 1
get_lucky_number("http://vietlott.vn/vi/trung-thuong/ket-qua-trung-thuong/mega-6-45/winning-numbers/")

# PAGE 2
get_lucky_number("http://vietlott.vn/vi/trung-thuong/ket-qua-trung-thuong/mega-6-45/winning-numbers/?p=2")

# PAGE 3
get_lucky_number("http://vietlott.vn/vi/trung-thuong/ket-qua-trung-thuong/mega-6-45/winning-numbers/?p=3")

# PAGE 4
get_lucky_number("http://vietlott.vn/vi/trung-thuong/ket-qua-trung-thuong/mega-6-45/winning-numbers/?p=4")


# for value in frequency.items():
#     print("Number {}".format(value))

for key, value in sorted(frequency.iteritems(), key=lambda (k,v): (v,k)):
    print("Number {}: {} times".format(key, value))
