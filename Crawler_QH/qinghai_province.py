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
    ul = html.xpath('//li')
    print(ul[0])
    # <li class=""><a href="./202103/t20210330_113720.html" target="_blank" title=
    # "受理公示：年产5万千米中低压、防火、铝合金、光伏电线电缆项目" class="xh-highlight">
    # 受理公示：年产5万千米中低压、防火、铝合金、光伏电线电缆项目</a><b class="">2021-03-30</b></li>
    
    for li in ul:
        # print(li.xpath('./a/@href'))
        detail_url = li.xpath('./a/@href')
        # [0]从数组中取字符串，[1:]字符串去掉第一个字符.
        # print(detail_url[0][1:])
        detail_url = 'http://shj.xining.gov.cn/zwgk/xxgkml/xzsp/yslxm' + detail_url[0][1:]
        # print('FUND:----------------' + detail_url)
        detail_urls.append(detail_url)
    return detail_urls
    # http://shj.xining.gov.cn/zwgk/xxgkml/xzsp/yslxm/202103/t20210330_113720.html

# 正片开始
counter = 1
counter_total = 0
page = 0

url = 'http://shj.xining.gov.cn/zwgk/xxgkml/xzsp/yslxm/list.html'
url_list = get_pdf_urls(url)
# print(len(url_list))
# for i in url_list:
    # print(i)
# print(url_list)
for detl_url in url_list:
    # detl_url  ---  http://shj.xining.gov.cn/zwgk/xxgkml/xzsp/yslxm/202103/t20210330_113720.html
    # 取日期：/202103
    date_url = detl_url[47:54]
    resp = requests.get(detl_url)
    # ---BeautifulSoup 实现---
    # soup = BeautifulSoup(request.urlopen(detl_url), 'lxml')
    # print(soup.prettify())
    # print(soup.span)
    # spans = soup.find_all('span')
    # for spa in spans:
    #     print(spa)
    # print(resp)
    text = resp.content.decode()
    html = etree.HTML(text)
    # print(etree.tostring(html).decode())
    download_url = html.xpath('//p[@class="insertfileTag"]/a/@href')
    if download_url == [] or download_url == False:
        download_url = html.xpath("//p//a[contains(@style,'color: rgb(0, 102, 204')]/@href")
        # //div/@class="zwxxgk_ndbgwz"
    # print(download_url)
    # ['./P020210825363252401366.pdf']
    file_name = html.xpath('//p[@class="insertfileTag"]/a/@title')
    if file_name == [] or file_name == False:
        file_name = html.xpath('//p//a/@title')
    print(file_name)
    # ['./P020210825363252401366.pdf']
    title = html.xpath('//h1')
    print(title[0].text)
    # print(file_name)
    # ['西宁市南川河水生态文明建设工程（生态环境综合治理）环境影响报告表.pdf']

    # for q in download_url:
        # print(download_url)
        # print(download_url[0])
        # print(file_name)
    try:
        for pdfs in download_url:
            download_url = 'http://shj.xining.gov.cn/zwgk/xxgkml/xzsp/yslxm' + date_url + pdfs[1:]
            print('PDF下载地址：' + download_url)
            # http://shj.xining.gov.cn/zwgk/xxgkml/xzsp/yslxm/202108/P020210825363252401366.pdf
        for pdf_name in file_name:
            print('PDF名称：' + pdf_name)
            # print(type(pdf_name))
            if str(pdf_name).find('能源') != -1:
                request.urlretrieve(download_url, pdf_name)
                print('下载' + pdf_name + '成功！')
            elif str(pdf_name).find('光伏') != -1:
                # 测试
                # print(str(file_name).find('光伏'))
                # print(pdf_name)
                request.urlretrieve(download_url, pdf_name)
                print('下载' + pdf_name + '成功！')
            elif str(pdf_name).find('太阳能') != -1:
                request.urlretrieve(download_url, pdf_name)
                print('下载' + pdf_name + '成功！')
            elif str(pdf_name).find('风力') != -1:
                request.urlretrieve(download_url, pdf_name)
                print('下载' + pdf_name + '成功！')
            elif str(pdf_name).find('电力') != -1:
                request.urlretrieve(download_url, pdf_name)
                print('下载' + pdf_name + '成功！')
            else:
                print('附件内容与新能源不相关！')
    except Exception as e:
            print("发生错误，附件链接损坏！")
    # 记数：li个数
    counter += 1
    counter_total += 1
    print('- ' * 6  + str(counter) + ' -' * 6)
    # 翻页
    # 第2页 - https://shj.xining.gov.cn/zwgk/xxgkml/xzsp/yslxm/list_1.html
    if counter > 20:
        counter = 1
        page += 1
        list_url = 'https://shj.xining.gov.cn/zwgk/xxgkml/xzsp/yslxm/list_'
        url_suffix = '.html'
        next_url = list_url + str(page) + url_suffix
        print(next_url)
        url = next_url
        url_list = get_pdf_urls(url)
print('合计扫描条目数：' + str(counter_total))