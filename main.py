from bs4 import BeautifulSoup
import requests
import time

print("Enter the skill you don't know")
skill_not_known = input(">")


def data():
    html = requests.get(
        'https://www.timesjobs.com/candidate/job-search.html?searchType=personalizedSearch&from=submit&searchTextSrc=&searchTextText=&txtKeywords=python+&txtLocation=').text
    soup = BeautifulSoup(html, 'lxml')
    jobs = soup.find_all('li', class_="clearfix job-bx wht-shd-bx")
    with open(f'./jobs/jobs.txt', 'w') as file:
        for job in jobs:
            skills = job.find('span', class_='srp-skills').text.strip()
            if skill_not_known not in skills:
                file.write(f"Company Name: {job.find('h3').text.strip()} \n")
                file.write(
                    f"Skills Required: {skills} \n")
                file.write(
                    f"Post Age: {job.find_all('span')[-1].text.strip()} \n\n")


while __name__ == '__main__':
    data()
    sleep_time = 10  # mins
    print(f"\nSleeping for {sleep_time} minutes...")
    time.sleep(sleep_time * 60)  # ms
    print()
