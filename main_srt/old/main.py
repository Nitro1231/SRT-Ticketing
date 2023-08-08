import requests
from bs4 import BeautifulSoup

PAGE_ID = 'TK0101010000'

json_data = {
    'dptRsStnCd': '0551',
    'arvRsStnCd': '0506',
    'stlbTrnClsfCd': '05',
    'psgNum': 1,
    'seatAttCd': '015',
    'isRequest': 'Y',
    'dptRsStnCdNm': '수서',
    'arvRsStnCdNm': '서대구',
    'dptDt': '20220627',
    'dptTm': '000000',
    'chtnDvCd': 1,
    'psgInfoPerPrnb1': 1,
    'psgInfoPerPrnb5': 0,
    'psgInfoPerPrnb4': 0,
    'psgInfoPerPrnb2': 0,
    'psgInfoPerPrnb3': 0,
    'locSeatAttCd1': '000',
    'rqSeatAttCd1': '015',
    'trnGpCd': 109
}


'''
?runDt1=
&dptDt1=
&dptTm1=
&trnNo1=
&trnGpCd1=
&dptRsStnCd1=
&arvRsStnCd1=
&dptStnRunOrdr1=
&arvStnRunOrdr1=
&seatAttCd1=
&psrmClCd1=
&index1=
&scarNo1=
&chtnDvCd=1&jrnySqno=001&mode=1&psgNum=&pageId=TK0101010000
'''


def search_ticket():
    content = ''
    with requests.post(f'https://etk.srail.kr/hpg/hra/01/selectScheduleList.do?pageId={PAGE_ID}', json=json_data, stream=True) as response:
        for line in response.iter_lines():
            print(line)

def test():
    req = requests.post(f'https://etk.srail.kr/hpg/hra/01/selectPassengerResearchList.do?pageId={PAGE_ID}', json=json_data)
    print(req.content)
    return req

def search_ticket_a():
    req = requests.post(f'https://etk.srail.kr/hpg/hra/01/selectScheduleList.do?pageId={PAGE_ID}', json=json_data)
    print(req.raw)
    return req

def collect_info(content):
    sp = BeautifulSoup(content, 'html.parser')
    print(sp)
    print(sp.find_all('legend'))


#search_ticket()

test()

# req = search_ticket()


# data = collect_info(req.content)
# print(len(req.text))


'''
?runDt1=
&dptDt1=
&dptTm1=
&trnNo1=
&trnGpCd1=
&dptRsStnCd1=
&arvRsStnCd1=
&dptStnRunOrdr1=
&arvStnRunOrdr1=
&seatAttCd1=
&psrmClCd1=
&index1=
&scarNo1=
&chtnDvCd=1&jrnySqno=001&mode=1&psgNum=&pageId=TK0101010000
'''