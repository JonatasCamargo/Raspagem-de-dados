from bs4 import BeautifulSoup
import requests
import pandas

response = requests.get('https://www.timesjobs.com/candidate/job-search.html?from=submit&luceneResultSize=25&txtKeywords=python&postWeek=60&searchType=personalizedSearch&actualTxtKeywords=python&searchBy=0&rdoOperator=OR&pDate=I&sequence=1&startPage=1')

soup = BeautifulSoup(response.text, 'lxml')
jobs = soup.find_all('li', class_='clearfix job-bx wht-shd-bx')

companys = []
skills = []

for job in jobs:
    name_company = job.find('h3', class_='joblist-comp-name').text.strip().replace(' ', '')
    skill_job = job.find('span', class_='srp-skills').text.strip().replace(' ', '')

    companys.append(name_company)
    skills.append(skill_job)


python_jobs = pandas.DataFrame()
python_jobs['companys'] = companys
python_jobs['skills'] = skills

print(python_jobs)
python_jobs.to_csv('python_jobs.csv')