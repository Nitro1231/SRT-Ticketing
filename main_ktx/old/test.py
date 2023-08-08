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


def download_file():
    local_filename = './test.html'

    with requests.post(f'https://etk.srail.kr/hpg/hra/01/selectScheduleList.do?pageId={PAGE_ID}', json=json_data, stream=True) as r:
        r.raise_for_status()
        with open(local_filename, 'wb') as f:
            for chunk in r.iter_content(chunk_size=8192): 
                # If you have chunk encoded response uncomment if
                # and set chunk_size parameter to None.
                #if chunk: 
                f.write(chunk)
    return local_filename

download_file()