import requests
from lxml import etree

def get_detail_urls(url):
    url01 = 'http://shj.xining.gov.cn/zwgk/xxgkzn/'
    url02 = 'http://shj.xining.gov.cn/images/jquery.SuperSlide.2.1.1.js'
    url03 = 'http://shj.xining.gov.cn/zwgk/xxgkml/xzsp/yslxm/list.html'

    # resp = requests.get(url01)
    # print(resp.cookies)
    # print(resp.cookies.get_dict)

    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.90 Safari/537.36 Edg/89.0.774.63'
    }

    resp = requests.get(url03)
    # print(resp.content.decode())
    # print(resp.content.decode('utf-8'))

    text = resp.content.decode()
    # 得到HTML
    html = etree.HTML(text)
    # 使用xPath语法
    ul = html.xpath('//li')
    # print(ul[0])
    # <li class=""><a href="./202103/t20210330_113720.html" target="_blank" title="受理公示：年产5万千米中低压、防火、铝合金、光伏电线电缆项目" class="xh-highlight">受理公示：年产5万千米中低压、防火、铝合金、光伏电线电缆项目</a><b class="">2021-03-30</b></li>
    for li in ul:
        # print(li.xpath('./a/@href'))
        detail_url = li.xpath('./a/@href')
        # [0]从数组中取字符串，[1:]字符串去掉第一个字符.
        # print(detail_url[0][1:])
        detail_url = 'http://shj.xining.gov.cn/zwgk/xxgkml/xzsp/yslxm' + detail_url[0][1:]
        print(detail_url)
    # http://shj.xining.gov.cn/zwgk/xxgkml/xzsp/yslxm/202103/t20210330_113720.html