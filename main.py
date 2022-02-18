from indeed import get_last_page, extract_indeed_jobs

print(get_last_page())
indeed_jobs=extract_indeed_jobs(get_last_page())
# print(indeed_jobs)
# for i in range(len(indeed_jobs)):
#     if indeed_jobs[i]['company_name']=='미정':
#         print(i)
print(indeed_jobs[319],indeed_jobs[455])