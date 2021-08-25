str01 = 'http://shj.xining.gov.cn/zwgk/xxgkml/xzsp/yslxm.'
str02 = str01[:-1]
print(str02)

str01 = '欧耐特线缆集团有限公司-年产5万千米中低压、防火、铝合金、光伏电线电缆项目环境影响报告表..pdf'

if str01.find('Ur Uncle'):
    # 不为0，都为True，if结果为-1
    print(str01.find('线缆'))
    print(str01.find('Ur Uncle'))