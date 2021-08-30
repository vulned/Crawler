# 下载中遇到的问题

## pdf文件名

<p class="insertfileTag" style="line-height: 16px; font-size: 19px; text-align: center; font-family: 宋体, SimSun;">
    <img needdownload="false" style="vertical-align: middle; margin-right: 2px; font-family: 宋体, SimSun; font-size: 19px;" src="/govapp/lib/ueditor_demo/ueditor2/dialogs/attachment/fileTypeImages/icon_pdf.gif">
    <a style="font-size: 19px; color: rgb(0, 102, 204); font-family: 宋体, SimSun;" appendix="true" otheroperation="false" href="./P020210830423761510808.pdf" title="乳制品前处理改造升级项目环评报告表.pdf" oldsrc="/protect/P0202108/P020210830/P020210830423761510808.pdf">乳制品前处理改造升级项目环评报告表.pdf</a></p>

如何找到？

> list.html
>
> > http://shj.xining.gov.cn/zwgk/xxgkml/xzsp/yslxm/list.html

反爬方式，header，cookie，session

![avatar](F:\TyporaPic/1.png)

受理公示：年产5万千米中低压、防火、铝合金、光伏电线电缆项目2021-03-30
受理公示：一类贴剂及凝胶剂医疗器械产业化项目、农用机具加工升级改造项目和大通县毛家沟年开采加工白云岩矿50万立方建设项目2021-03-29
受理公示：年产1200万块动力电池铝壳生产线建设项目和西宁市第四污水处理厂中水扩能及水质提升工程2021-03-24
受理公示：青海省大通县宝库渠灌区续建配套与节水改造工程等3个项目2021-03-22
受理公示：新增30000t/a新型有机肥扩建项目  2021-03-16
受理公示：湟中富强砂石厂项目2021-03-12
受理公示：青海甘河工业园开发建设有限公司甘河地下水修复及水污染综合治理项目2021-03-11
受理公示：青海尚峰建材有限公司建筑材料建设项目2021-03-08
受理公示：西宁市湟源县人民医院感染性疾病科（病区）建设项目2021-03-05
受理公示：一类贴剂、凝胶剂医疗器械产业化建设项目和改建修理厂房建设项目2021-02-26
受理公示：东格尔药业大通有限公司装修项目和年产7万平米定制式智能家具制造项目2021-02-20
受理公示：青海华实青稞生物科技开发有限公司研发实验室项目2021-02-05
受理公示：青海省引大济湟西干渠灌溉工程田间配套建设项目（湟中片24#、26#支渠）等2个项目2021-02-04
受理公示：青海象道物流有限公司湟源转运站项目2021-01-29
受理公示：青海坤峰建材有限公司新型建材生产线建设项目等3个项目2021-01-27
受理公示：青海力创铝业有限公司年产6万吨电工圆铝杆建设项目、西宁市粪便无害化处理厂迁建项目2021-01-25
受理公示：西宁市餐厨垃圾处理项目2021-01-18
受理公示：西宁市湟中区田家寨镇田家寨村人饮管网提升改造工程等2个项目2021-01-08
受理公示：西宁市城南污水处理厂提质改造工程2020-12-31
受理公示：湟源县2020年农村饮水管网更新改造工程等3个项目2020-12-30

### 重定向

urlretrieve

### 获取倒数第二个内容

result = html.xpath('//li[last()-1]/a')

result[0].text

# 基础

## 网页请求

### 参见：urllib_learning.py

抓取网页代码

## 网页解析（Parse）

### 参见：urlencode.py

解析传参编码

## Cookies

### 参见：requestsLib.py

### POST和GET方法

POST方法和GET方法是前端将表单中的内容提交到服务器端的方法，为了获得服务器的Response。

GET在URL中传参，POST将参数放入HTTP请求报文。