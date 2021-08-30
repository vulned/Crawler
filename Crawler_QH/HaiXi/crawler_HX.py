import requests
from urllib import request
from lxml import etree
from bs4 import BeautifulSoup

detail_urls = []
def get_pdf_urls(url):
    resp = requests.get(url)
    # print(resp.content.decode())
    # print(resp.content.decode('utf-8'))

    text = resp.content.decode()
    # 得到HTML
    html = etree.HTML(text)
    # 使用xPath语法
    ul = html.xpath('//div[@class="new_list"]//li')
    print(ul)
    
    for li in ul:
        # print(li)
        # print(li.xpath('./a/@href'))
        detail_url = li.xpath('./a/@href')
        # [0]从数组中取字符串，[1:]字符串去掉第一个字符.
        # print(detail_url[0][1:])
        detail_url = 'http://sthjj.haixi.gov.cn' + detail_url[0]
        # print('FUND:----------------' + detail_url)
        detail_urls.append(detail_url)
    return detail_urls
    # http://shj.xining.gov.cn/zwgk/xxgkml/xzsp/yslxm/202103/t20210330_113720.html

url = 'http://sthjj.haixi.gov.cn/article/lists/category/ypzxmgg.html'
url_list = get_pdf_urls(url)
# print(url_list)

for detl_url in url_list:
    # detl_url  ---  http://shj.xining.gov.cn/zwgk/xxgkml/xzsp/yslxm/202103/t20210330_113720.html
    # 取日期：/202103
    # date_url = detl_url[47:54]
    resp = requests.get(detl_url)
    text = resp.content.decode()
    html = etree.HTML(text)
    # print(etree.tostring(html).decode())
    download_url = html.xpath('//a[@class="ke-insertfile"]/@href')
    file_name = html.xpath('//a[@class="ke-insertfile"]/span')