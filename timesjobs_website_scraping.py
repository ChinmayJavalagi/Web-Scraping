from bs4 import BeautifulSoup
import requests
import time

print("Put some skill that you are not familiar with")
unfamiliar_skill = input('>')
print(f'Filtering out {unfamiliar_skill}.......')
html_text = requests.get(
    'https://www.timesjobs.com/candidate/job-search.html?searchType=personalizedSearch&from=submit&txtKeywords=python&txtLocation=').text
soup = BeautifulSoup(html_text, 'lxml')
jobs = soup.find_all('li', class_='clearfix job-bx wht-shd-bx')


def find_jobs():
    for index, job in enumerate(jobs):
        experience = job.find('li').text.strip('card_travel')
        published_date = job.find('span', class_='sim-posted').span.text
        if '0' in experience:
            more_info = job.header.h2.a['href']
            company_name = job.find('h3', 'joblist-comp-name').text.strip()
            skills = job.find('span', class_='srp-skills').text.strip()
            if unfamiliar_skill not in skills:
                with open(f'posts/{index}.text', 'w') as f:
                    f.write(f"Company Name: {company_name} \n")
                    f.write(f"Required Skills: {skills} \n")
                    f.write(f"Date Published: {published_date} \n")
                    f.write(f"Experience: {experience} \n")
                    f.write(f"More Info: {more_info}")
                print(f'{index}.text file saved!')



if __name__ == '__main__':
    while True:
        find_jobs()
        time_wait = 1
        print(f'Cool Down Time: {time_wait} minutes...')
        time.sleep(time_wait * 60)
