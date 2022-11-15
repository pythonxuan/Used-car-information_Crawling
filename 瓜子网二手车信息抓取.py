import requests
from bs4 import BeautifulSoup
import io
import sys
# 1.分析目标网页，确定爬取的ur1路径，headers参数
for top in range(1,51):
    ur1 = 'https://www.guazi.com/km/buy/o{}/#bread'.format(top)
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.82 Safari/537.36',
                'Cookie': 'track_id=192961679105867776; uuid=6733ad7c-fd33-43b6-cb34-c3dfc0145752; antipas=4q8598938e24g9979505394647; ganji_uuid=6003064859778167980620; lg=1; close_finance_popup=2021-03-31; user_city_id=225; cityDomain=km; sessionid=10e112e8-0f9d-4521-ba43-ef5ce1ca0f21; Hm_lvt_bf3ee5b290ce731c7a4ce7a617256354=1617160850,1617190540; Hm_lpvt_bf3ee5b290ce731c7a4ce7a617256354=1617190540; clueSourceCode=%2A%2300; cainfo=%7B%22ca_a%22%3A%22-%22%2C%22ca_b%22%3A%22-%22%2C%22ca_s%22%3A%22pz_baidu%22%2C%22ca_n%22%3A%22pcbiaoti%22%2C%22ca_medium%22%3A%22-%22%2C%22ca_term%22%3A%22-%22%2C%22ca_content%22%3A%22%22%2C%22ca_campaign%22%3A%22%22%2C%22ca_kw%22%3A%22-%22%2C%22ca_i%22%3A%22-%22%2C%22scode%22%3A%22-%22%2C%22keyword%22%3A%22-%22%2C%22ca_keywordid%22%3A%22-%22%2C%22ca_transid%22%3A%22%22%2C%22platform%22%3A%221%22%2C%22version%22%3A1%2C%22track_id%22%3A%22192961679105867776%22%2C%22display_finance_flag%22%3A%22-%22%2C%22client_ab%22%3A%22-%22%2C%22guid%22%3A%226733ad7c-fd33-43b6-cb34-c3dfc0145752%22%2C%22ca_city%22%3A%22km%22%2C%22sessionid%22%3A%2210e112e8-0f9d-4521-ba43-ef5ce1ca0f21%22%7D; preTime=%7B%22last%22%3A1617190551%2C%22this%22%3A1617160849%2C%22pre%22%3A1617160849%7D'
               }
    resp = requests.get(ur1, headers=headers)
    html = resp.content.decode()
    # 2.解析网页
    soup = BeautifulSoup(html)
    infos = soup.find('ul',{'class' : 'carlist clearfix js-top'}).find_all('li')
    # print(infos)
    with open(r'C:\Users\Administrator\Desktop\guazi\guazi.csv' , 'a' , encoding='utf-8') as f:

        for info in infos:
            leixing = info.find('h2').get_text()
            # print(leixing)
            nianfen1 = info.find('div',{'class':'t-i'}).get_text().split('|')
            nianfen = nianfen1[0]
            # print(nianfen)
            licheng = nianfen1[1]
            fuwu = '昆明'
            yuanjia = info.find('div',{'class':'t-price'}).find('em').get_text()
            # print(yuanjia)
            shoujia = info.find('div',{'class':'t-price'}).find('p').get_text()
            try:
                shoujia = info.find('div', {'class': 't-price'}).find('p').get_text()
                # print(yuanjia)
            except  AttributeError:
                yuanjia= ''
            f.write('{},{},{},{},{},{}\n'.format(leixing, nianfen, licheng, fuwu, yuanjia, shoujia))