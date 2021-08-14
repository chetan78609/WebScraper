import time

from bs4 import BeautifulSoup
import requests

print('Enter the unfamiliar skills you are not familiar with')
unfamiliar_skills = input('>')
print('Hold on! Till We Filter it out!')

html_text = requests.get('https://www.timesjobs.com/candidate/job-search.html?searchType=personalizedSearch&from=submit&txtKeywords=python&txtLocation=').text

soup = BeautifulSoup(html_text,'lxml')
jobs = soup.find_all('li', class_ = 'clearfix job-bx wht-shd-bx')

def find_jobs():
    for index,job in enumerate(jobs):

        Published_date = job.find('span', class_='sim-posted').text
        if 'few' in Published_date:
            company_name =  job.find('h3', class_ = 'joblist-comp-name').text.replace(' ', '')
            skills = job.find('span', class_ = 'srp-skills').text.replace(' ', '')
            more_info = job.header.a['href']
            if unfamiliar_skills not in skills:
                with open(f'{index}.txt', 'w+') as f:
                    f.write(f"Company Name: {company_name.strip()} \n")
                    f.write(f"Required Skills: {skills.strip()} \n")
                    f.write(f"More Info: {more_info} \n")

            print(f"The File has been Saved : {index}")


if __name__ == '__main__':
    while True:
        find_jobs()
        time_wait = 1
        print(f'Just Wait for {time_wait} minutes')
        time.sleep(time_wait * 60)
