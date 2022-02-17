import requests  # python 으로 url을 가져올 수 있다

from bs4 import BeautifulSoup # html 정보를 추출

# url 가져오기 (마지막 페이지로)
indeed_result = requests.get('https://kr.indeed.com/jobs?q=python&limit=50&radius=25&start=550&vjk=4424be6fa9f5860e')

# html 가져오기
# print(indeed_result.text)

# url text를 html로 처리를 해준다
indeed_soup = BeautifulSoup(indeed_result.text,"html.parser")

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
searchCountPages = indeed_soup.find("div",{"id":"searchCountPages"})
last_page = str(searchCountPages.string).strip().split()[0][:2]
last_page = int(last_page)
print(last_page, type(last_page))

