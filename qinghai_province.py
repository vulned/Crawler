import requests
from urllib import request
from lxml import etree

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
    # print(ul[0])
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

url = 'http://shj.xining.gov.cn/zwgk/xxgkml/xzsp/yslxm/list.html'
url_list = get_pdf_urls(url)
# for i in url_list:
    # print(i)
# print(url_list)

for detail_url in url_list:
    # print(detail_url)
    resp = requests.get(detail_url)
    # print(resp)
    text = resp.content.decode()
    html = etree.HTML(text)
    download_url = html.xpath('//p[@class="insertfileTag"]/a/@href')
    file_name = html.xpath('//p[@class="insertfileTag"]/a/@title')
    counter = 0
    for q in download_url:
        counter += 1
        print('------ ' + str(counter) + ' ------')
        print(download_url)
        print(download_url[0])
        print(file_name)
    try:
    # ./P020210330399029703556.pdf
    # http://shj.xining.gov.cn/zwgk/xxgkml/xzsp/yslxm/202103/P020210330399029703556.pdf
        for pdfs in download_url:
            download_url = 'http://shj.xining.gov.cn/zwgk/xxgkml/xzsp/yslxm/202103' + pdfs[1:]
            # print(download_url)
            # print(file_name)
        for pdf_name in file_name:
            # print(pdf_name)
            # print(type(pdf_name))
            if str(file_name).find('光伏') != -1:
                print(str(file_name).find('光伏'))
                # print(pdf_name)
                # request.urlretrieve(download_url, pdf_name)
    except Exception as e:
            print('无附件')