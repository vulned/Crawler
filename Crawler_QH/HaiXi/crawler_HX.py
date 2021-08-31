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
    # 使用xpath语法
    ul = html.xpath('//div[@class="new_list"]//li')
    # print(ul)
    # [<Element li at 0x426cec0>, <Element li at 0x42b0b00>, <Element li at 0x426bf80>, 
    # <Element li at 0x426bf40>, <Element li at 0x426bf00>, <Element li at 0x426be80>, 
    # <Element li at 0x42b77c0>, <Element li at 0x42b7740>, <Element li at 0x42b7800>, 
    # <Element li at 0x426be00>]
    
    for li in ul:
        # print(li)
        detail_url = li.xpath('./a/@href')
        # print(li.xpath('./a/@href'))
        # ['/article/detail/id/3396.html']
        print(detail_url)
        print(detail_url[0])
        detail_url = 'http://sthjj.haixi.gov.cn' + detail_url[0]
        # print('FUND:----------------' + detail_url)
        detail_urls.append(detail_url)
    return detail_urls
    # http://shj.xining.gov.cn/zwgk/xxgkml/xzsp/yslxm/202103/t20210330_113720.html

# 主函数
page = 1
counter = 1
counter_total = 0

page = input('需要从第几页开始下载：')
url = 'http://sthjj.haixi.gov.cn/article/lists/category/ypzxmgg/p/' + page + '.html'
     # http://sthjj.haixi.gov.cn/article/lists/category/ypzxmgg/p/2.html
url_list = get_pdf_urls(url)
# print(url_list)

for detl_url in url_list:
    resp = requests.get(detl_url)
    text = resp.content.decode()
    html = etree.HTML(text)
    # print(etree.tostring(html).decode())

    # 下载地址：
    try:
        download_url = html.xpath('//a[@class="ke-insertfile"]/@href')
    except Exception as e:
        print('请检查下载地址，第' + str(page) + '页！')
    # /Uploads/Editor/2021-07-30/61035feb9e4f5.pdf
    # /Uploads/Editor/2021-07-30/61036002e3738.pdf

    # PDF文件名：
    try:
        file_name = html.xpath('//a[@class="ke-insertfile"]//span')
    except Exception as e:
        print('请查阅附件：' + download_url)
    # print(file_name[0])
    # Result：<Element li at 0x54fa440>
    print(file_name[0].text)
    # Result：
    # 关于茫崖市污水处理厂扩能改建工程环境影响报告表的批复
    # 关于锡铁山镇镇区污水处理厂及污水管网建设项目环境影响报告表的批复

    try:
        for pdfs in download_url:
             # 从：http://sthjj.haixi.gov.cn/article/detail/id/4907.html
             # 到：http://sthjj.haixi.gov.cn/Uploads/Editor/2021-07-30/61035feb9e4f5.pdf
            download_url = 'http://sthjj.haixi.gov.cn' + pdfs
            print('PDF下载地址：' + download_url)
        for pdf_name in file_name:
            print(pdf_name.text)
            # print('PDF名称：' + pdf_name[0].text)
            # print(type(pdf_name))
            download_name = pdf_name.text + '.pdf'
            if str(pdf_name.text).find('能源') != -1:
                request.urlretrieve(download_url, download_name)
                print('下载【' + pdf_name.text + '】成功！')
            elif str(pdf_name.text).find('光伏') != -1:
                request.urlretrieve(download_url, download_name)
                print('下载【' + pdf_name.text + '】成功！')
            elif str(pdf_name.text).find('太阳能') != -1:
                request.urlretrieve(download_url, download_name)
                print('下载【' + pdf_name.text + '】成功！')
            elif str(pdf_name.text).find('风力') != -1:
                request.urlretrieve(download_url, download_name)
                print('下载【' + pdf_name.text + '】成功！')
            elif str(pdf_name.text).find('电力') != -1:
                request.urlretrieve(download_url, download_name)
                print('下载【' + pdf_name.text + '】成功！')
            elif str(pdf_name.text).find('电站') != -1:
                request.urlretrieve(download_url, download_name)
                print('下载【' + pdf_name.text + '】成功！')
            else:
                print('附件内容与新能源不相关！')
    except Exception as e:
        print('第【' + str(page) + '】页、第【' + str(counter - 1) + '】条发生错误，'
            '错误文件名在：【' + download_name + '】之前!')
        # 条数记录
    counter += 1
    counter_total += 1
    print('- ' * 6  + str(counter) + ' -' * 6)
    # 翻页
    # 第1页 - http://sthjj.haixi.gov.cn/article/lists/category/ypzxmgg/p/1.html
    # 第2页 - http://sthjj.haixi.gov.cn/article/lists/category/ypzxmgg/p/2.html
    if counter > 10:
        counter = 1
        page += 1
        list_url = 'http://sthjj.haixi.gov.cn/article/lists/category/ypzxmgg/p/'
        url_suffix = '.html'
        next_url = list_url + str(page) + url_suffix
        print(next_url)
        url_list = get_pdf_urls(next_url)
print('合计扫描条目数：' + str(counter_total))