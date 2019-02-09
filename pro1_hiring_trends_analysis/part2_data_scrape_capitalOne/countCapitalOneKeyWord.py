from urllib import request
from bs4 import BeautifulSoup
import requests,re
import pandas as pd
import numpy as np
import csv


def getHTMLText(url):
    try:
        kv = {'user-agent': 'Mozilla/5.0'}
        r = requests.get(url, headers=kv)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        return r.text
    except:
        print('404 error!')
        return(' ')

def readFromCSV(csvFile):
    obj = []
    csv_reader = csv.reader(open(csvFile))
    # for i, rows in enumerate(csv_reader):
    #         obj.append(rows[0])
    # return obj[0:100]
    for row in csv_reader:
        if(len(row)!=0):
            obj.append(row[1])
    return obj[0:100]

def countWordsFreq(url):
    # # a specific job position's page
    # content = getHTMLText(url)
    # count = []
    # csv_reader = readFromCSV('/Users/ziyanzhu/PycharmProjects/Cuihao/result2-WF-INF.csv')
    # for i, rows in enumerate(csv_reader):
    #     num = len(re.findall(rows[0], content, re.IGNORECASE))
    #     if(num==0):
    #         count.append(0)
    #     else:
    #         count.append(num)
    # return count
    content = getHTMLText(url)
    count = []
    keywords = readFromCSV('/Users/ziyanzhu/PycharmProjects/Top Key Words Lists/m3_top_100_key_words.csv')
    for keyword in keywords:
        num = len(re.findall(keyword, content, re.IGNORECASE))
        if(num==0):
            count.append(0)
        else:
            count.append(num)
    return count[0:100]


def main():
    #urls = readFromCSV("/Users/ziyanzhu/PycharmProjects/position.csv")
    urls = [  # p1
        'https://www.capitalonecareers.com/job/new-york/commercial-real-estate-uw-i/1732/10823431',
        'https://www.capitalonecareers.com/job/edison/sr-commercial-credit-officer-middle-market-bank/1732/10818537',
        'https://www.capitalonecareers.com/job/new-york/senior-director-healthcare-services-alternate-sites-investment-research-group/1732/10818553',
        'https://www.capitalonecareers.com/job/new-orleans/anti-money-laundering-sr-manager/1732/10812506',
        'https://www.capitalonecareers.com/job/richmond/credit-review-allowance-manager/1732/10812521',
        'https://www.capitalonecareers.com/job/richmond/manager-risk-management-enterprise-services-business-risk-office/1732/10812528',
        'https://www.capitalonecareers.com/job/richmond/senior-associate-card-risk/1732/10812529',
        'https://www.capitalonecareers.com/job/richmond/risk-project-and-change-manager-principal-associate/1732/10807153',
        'https://www.capitalonecareers.com/job/richmond/senior-associate-card-risk/1732/10799863',
        'https://www.capitalonecareers.com/job/melville/manager-compliance-advisory/1732/10799873',
        'https://www.capitalonecareers.com/job/richmond/risk-manager-customer-resiliency/1732/10799876',
        'https://www.capitalonecareers.com/job/new-orleans/anti-money-laundering-supervisor/1732/10799893',
        'https://www.capitalonecareers.com/job/richmond/senior-manager-quality-and-reporting-team-lead/1732/10786437',
        'https://www.capitalonecareers.com/job/mclean/compliance-privacy-director/1732/10779895',
        'https://www.capitalonecareers.com/job/wilmington/principal-associate-consumer-credit-review-and-mra-validations/1732/10779900',
        # p2
        'https://www.capitalonecareers.com/job/mclean/privacy-compliance-advisor-manager/1732/10779887',
        'https://www.capitalonecareers.com/job/richmond/privacy-manager-us-card/1732/10779902',
        'https://www.capitalonecareers.com/job/richmond/anti-money-laundering-supervisor-transaction-monitoring-operations/1732/10768483',
        'https://www.capitalonecareers.com/job/mclean/senior-risk-associate/1732/10768491',
        'https://www.capitalonecareers.com/job/mclean/sox-senior-manager/1732/10768496',
        'https://www.capitalonecareers.com/job/richmond/sr-risk-associate/1732/10768502',
        'https://www.capitalonecareers.com/job/new-york/principal-risk-specialist/1732/10768499',
        'https://www.capitalonecareers.com/job/richmond/associate-card-risk-process-automation-rpa-developer/1732/10763295',
        'https://www.capitalonecareers.com/job/toronto/compliance-testing-manager/1732/10763313',
        'https://www.capitalonecareers.com/job/wilmington/anti-money-laundering-supervisor/1732/10757450',
        'https://www.capitalonecareers.com/job/mclean/small-business-underwriter-ii/1732/10747021',
        'https://www.capitalonecareers.com/job/richmond/principal-corporate-compliance-tester/1732/10737719',
        'https://www.capitalonecareers.com/job/plano/bro-risk-specialist-senior-associate/1732/10714658',
        'https://www.capitalonecareers.com/job/mclean/manager-market-and-liquidity-risk-oversight-strategy/1732/10714669',
        'https://www.capitalonecareers.com/job/richmond/director-card-risk/1732/10714663',
        # p3
        'https://www.capitalonecareers.com/job/mclean/audit-manager-card-audit/1732/10714664',
        'https://www.capitalonecareers.com/job/richmond/director-card-risk/1732/10714680',
        'https://www.capitalonecareers.com/job/richmond/risk-manager/1732/10708751',
        'https://www.capitalonecareers.com/job/vienna/it-applications-risk-specialist/1732/10690076',
        'https://www.capitalonecareers.com/job/new-york/enterprise-valuation-sr-associate-commercial-credit-risk-and-analytics/1732/10690054',
        'https://www.capitalonecareers.com/job/chicago/anti-money-laundering-investigator-ii-list-screening-operations/1732/10690079',
        'https://www.capitalonecareers.com/job/nottingham/senior-audit-associate/1732/10677800',
        'https://www.capitalonecareers.com/job/bethesda/commercial-real-estate-analyst/1732/10676250',
        'https://www.capitalonecareers.com/job/new-york/senior-auditor-commercial-bank-audit/1732/10676267',
        'https://www.capitalonecareers.com/job/richmond/manager-consumer-credit-policy-risk-management/1732/10670881',
        'https://www.capitalonecareers.com/job/mclean/senior-manager-cyber-technology-risk-advisor/1732/10670866',
        'https://www.capitalonecareers.com/job/richmond/principal-risk-specialist/1732/10670872',
        'https://www.capitalonecareers.com/job/mclean/security-operations-center-supervisor/1732/10663879',
        'https://www.capitalonecareers.com/job/richmond/security-operations-center-supervisor/1732/10663878',
        'https://www.capitalonecareers.com/job/richmond/security-operations-center-supervisor/1732/10663878',
        # p4
        'https://www.capitalonecareers.com/job/mclean/manager-risk-management-capital-risk-oversight/1732/10662707',
        'https://www.capitalonecareers.com/job/richmond/badging-administrator/1732/10662692',
        'https://www.capitalonecareers.com/job/richmond/senior-auditor-audit-practices/1732/10662718',
        'https://www.capitalonecareers.com/job/mclean/senior-associate-metadata-taxonomy/1732/10662705',
        'https://www.capitalonecareers.com/job/richmond/compliance-tester-iii-enterprise-services/1732/10655580',
        'https://www.capitalonecareers.com/job/richmond/principle-risk-specialist-retail-bank/1732/10648815',
        'https://www.capitalonecareers.com/job/richmond/senior-manager-risk-human-resources-business-risk-office-hr-bro/1732/10642262',
        'https://www.capitalonecareers.com/job/richmond/compliance-tester-ii-privacy/1732/10642258',
        'https://www.capitalonecareers.com/job/richmond/associate-corporate-insurance-risk-management/1732/10642274',
        'https://www.capitalonecareers.com/job/mclean/senior-auditor-audit-practices/1732/10642270',
        'https://www.capitalonecareers.com/job/mclean/sr-risk-specialist-enterprise-services-risk/1732/10642265',
        'https://www.capitalonecareers.com/job/new-york/senior-auditor-financial-crimes-compliance/1732/10613399',
        'https://www.capitalonecareers.com/job/bethesda/commercial-real-estate-managing-underwriter-i/1732/10599945',
        'https://www.capitalonecareers.com/job/richmond/senior-risk-associate-card/1732/10599942',
        'https://www.capitalonecareers.com/job/richmond/sr-risk-manager-local-governance-retail-and-direct-bank/1732/10565640',
        # p5
        'https://www.capitalonecareers.com/job/richmond/sr-risk-associate-operational-risk-business-continuity-team/1732/10565647',
        'https://www.capitalonecareers.com/job/mclean/principal-auditor-accounting/1732/10565638',
        'https://www.capitalonecareers.com/job/richmond/security-operations-center-manager/1732/10565655',
        'https://www.capitalonecareers.com/job/rolling-meadows/aml-supervisor-list-screening-operations/1732/10559967',
        'https://www.capitalonecareers.com/job/richmond/senior-manager-walmart-compliance-advisor/1732/10559959',
        'https://www.capitalonecareers.com/job/new-york/technology-risk-sr-associate-market-credit-and-liquidity-infrastructure/1732/10550962',
        'https://www.capitalonecareers.com/job/mclean/audit-manager-audit-practices-board-reporting-and-regulatory-management/1732/10550956',
        'https://www.capitalonecareers.com/job/rolling-meadows/anti-money-laundering-sr-investigator-i-complex-investigations-unit-law-enforcement-monitoring/1732/10544042',
        'https://www.capitalonecareers.com/job/bethesda/commercial-real-estate-asset-manager-v/1732/10544049',
        'https://www.capitalonecareers.com/job/richmond/digital-risk-manager/1732/10526885',
        'https://www.capitalonecareers.com/job/richmond/sr-manager-high-line-credit-risk-underwriting-small-business-card/1732/10517646',
        'https://www.capitalonecareers.com/job/mclean/sr-risk-manager-walmart-risk-office/1732/10492147',
        'https://www.capitalonecareers.com/job/chicago/senior-auditor-financial-crimes-compliance/1732/10503484',
        'https://www.capitalonecareers.com/job/richmond/sr-risk-associate-operational-risk-management/1732/10503492',
        'https://www.capitalonecareers.com/job/richmond/senior-auditor-financial-crimes-compliance/1732/10503480'

        # '',
        # '',
        # '',
        # '',
        # '',
        # '',
        # '',
        # '',
        # '',
        # '',
        # '',
        # '',
        # '',
        # '',
        # '',
    ]
    #csv_reader = csv.reader(open('/Users/ziyanzhu/PycharmProjects/Top Key Words Lists/m3_top_100_key_words.csv'))

    totalCount = []
    for i in range(100):
        totalCount.append(0)

    totalCount = np.array(totalCount)

    for url in urls:

        totalCount += np.array(countWordsFreq(url))
    keywords = readFromCSV('/Users/ziyanzhu/PycharmProjects/Top Key Words Lists/m3_top_100_key_words.csv')

    # 字典中的key值即为csv中列名
    dataframe = pd.DataFrame({'keyword':keywords,'occurence':totalCount})

    # 将DataFrame存储为csv,index表示是否显示行名，default=True
    dataframe.to_csv('/Users/ziyanzhu/PycharmProjects/capitalOne/RiskManagement_result3_75_items.csv', index=True, sep=',')
    # print(len(countWordsFreq('https://www.capitalonecareers.com/job/glen-allen/business-analyst-manager-service-and-change-delivery/1732/10648836')))
    # print(countWordsFreq('https://www.capitalonecareers.com/job/glen-allen/business-analyst-manager-service-and-change-delivery/1732/10648836'))
    #print(readFromCSV('/Users/ziyanzhu/PycharmProjects/Top Key Words Lists/m3_top_100_key_words.csv'))
main()