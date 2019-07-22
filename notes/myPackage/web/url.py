# import decouple

# 리눅스 시스템에서는 환경변수 설정으로 저장할 것. : 환경변수화해서 저장하기 : 어느 언어에서든 상관없이 사용가능~!

def make_url(key, targetDt):
    base_url = 'http://www.kobis.or.kr/kobisopenapi/webservice/rest/boxoffice/searchDailyBoxOfficeList.json'
    url = f'{base_url}?key={key}&targetDt={targetDt}'

    return url

# package 안에서 import해서 쓰는 것까지

