from matplotlib.pyplot import title
from numpy import true_divide
import requests  # python 으로 url을 가져올 수 있다
from bs4 import BeautifulSoup # html 정보를 추출

LIMIT = 50
INDEED_URL = f"https://kr.indeed.com/jobs?q=python&limit={LIMIT}&radius=25"

def get_last_page():
    # url 가져오기 (마지막 페이지로)
    result = requests.get(INDEED_URL+"&start=500") # 여기서는 임의로 지정해서 세팅했다
    # html 가져오기
    # print(indeed_result.text)
    # url text를 html로 처리를 해준다
    soup = BeautifulSoup(result.text,"html.parser")
    # print(indeed_soup)
    ###############################################################

    # # 인디드 페이지 추출 1부 2부 참고
    # # 마지막 페이지를 찾기 위한 과정이지만 다른방법을 시도해보자
    # # 처리된 html에서 정보를 찾아온다
    # # tag 와 class를 이용해 가져올 html를 선택한다
    # pagination = indeed_soup.find("div",{"class": "pagination"})
    # # print(pagination)

    # pages = pagination.find_all('a')
    # # print(pages)

    # for page in pages:
    #     print(page.find("span"))

    ###############################################################


    # 마지막 페이지 추출
    searchCountPages = soup.find("div",{"id":"searchCountPages"})
    last_page = str(searchCountPages.string).strip().split()[0][:2]
    last_page = int(last_page)
    # print(last_page, type(last_page))
    return last_page



def extract_job(html): 

    title=html.find("h2",{"class":"jobTitle"}).find_all("span")[-1].string
    if html.find("span",{"class":"companyName"}) is not None:
        company_name = html.find("span",{"class":"companyName"}).string
    else:
        company_name = "미정"
    company_name=company_name.strip()
    company_location = html.find("div",{"class": "companyLocation"}).string
    job_id = html['data-jk']

    return  {'title':title,
     'company_name':company_name,
      'company_location':company_location ,
       "link":f"https://kr.indeed.com/jobs?q=python&limit={LIMIT}&radius=25&vjk={job_id}"}


def extract_indeed_jobs(last_page):
    jobs=[]
    for now_page in range(last_page):
        print(f"페이지 {now_page}\n\n")
        result=requests.get(f"{INDEED_URL}&start={now_page*LIMIT}")
        print(result.status_code)
        soup = BeautifulSoup(result.text,"html.parser")
        # results = soup.find_all("h2",{"class":"jobTitle"})
        results = soup.find_all("a",{"class":"tapItem"})
        for result in results:
            job=extract_job(result)
            jobs.append(job)

    return jobs