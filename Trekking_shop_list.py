import requests
from bs4 import BeautifulSoup
import pandas as pd
import csv

search_word = '登山　業者'
pages_num = 10 + 1
url = f'https://www.google.co.jp/search?hl=ja&num={pages_num}&q={search_word}'
request = requests.get(url)

soup = BeautifulSoup(request.content, "html.parser")
search_site_lists = soup.select('div.kCrYT > a')

search_site_list = []
url_list = []

for i in search_site_lists:
    search_site_list.append(i.text.split('www.')[0])
    url_list.append(i.attrs['href'].replace('/url?q=', '').split('/&sa=')[0])

df_title_url = pd.DataFrame({'Shop':search_site_list, 'URL':url_list})
print(df_title_url)

df_title_url.to_csv('Trekking_shop_list12.csv',encoding='shift jis', errors='ignore')


# 業者のリスト
# shop_list = []
# h3s = search_site_list.find_all('h3')
# for h3 in h3s: 
#     shop_list.append(h3.text)  
#     print(shop_list)

# 外貨名のリスト
# r_list = []
# ths = table.select('th')
# for th in ths: 
#     r_list.append(th.text)  
