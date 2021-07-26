import pandas as pd
import re
import requests
from bs4 import BeautifulSoup

서비스 = 10001
금융 = 10002
은행 = 10002
건설 = 10003
의료 = 10004
제약 = 10004
미디어 = 10005
광고 = 10005
문화 = 10006
예술 = 10006
디자인 = 10006
IT = 10007
정보통신 = 10007
기타 = 10008
제조 = 10009
생산 = 10009
화학 = 10009
판매 = 10010
유통 = 10010
교육 = 10011

    
service_url = 'https://www.jobkorea.co.kr/recruit/joblist?menucode=industry&industryCtgr=10001'
service_headers = {'user-agent': 'user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.77 Safari/537.36 Edg/91.0.864.37'}
req = requests.post(service_url, headers = service_headers).text
service_soup = bs(req, 'html.parser')

service_firmlist = service_soup.find_all('td', class_='tplCo')
service_firm = []
for i in service_firmlist:
    service_firm.append(i.find('a').get_text().replace('\n', '').replace('관심기업', ''))

service_titlelist = service_soup.find_all('div', class_='titBx')
service_title = []
for i in service_titlelist:
    service_title.append(i.find('a').get_text())
    service_title = service_title[:40]
    
service_teglist = service_soup.find_all('p', class_='dsc')
service_tag = []
for i in service_teglist:
    service_tag.append(i.get_text())
    service_tag = service_tag[:40]

service_df = pd.DataFrame(service_firm, columns= ['기업 이름'])
service_df['공고 제목'] = service_title
service_df['태그'] = service_tag
service_df.head()

