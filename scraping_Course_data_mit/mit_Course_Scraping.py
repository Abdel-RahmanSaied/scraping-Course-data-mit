from bs4 import BeautifulSoup
import requests
import csv
import pandas as pd

url = "https://ocw.mit.edu/courses/6-006-introduction-to-algorithms-spring-2020/video_galleries/lecture-videos/"
base_url = "https://ocw.mit.edu/"

response = requests.get(url)
soup = BeautifulSoup(response.text , "html.parser")

file_name = soup.find("div" , attrs={"class":"max-content-width m-auto px-5 py-6"}).find("a",attrs={"class":"text-uppercase display-4 font-weight-bold m-0 text-white"}).get_text()
file_name+=".csv"

lecture_titles = soup.find_all("div" , attrs={"class":"mb-2 border-gray rounded video-gallery-card"})
lecture_links = soup.find_all("a" , attrs={"class":"video-link"})

lecture_title_list = [lecture_title.get_text().strip() for lecture_title in lecture_titles]
lecture_links_list = [base_url+lecture_link.get('href').strip() for lecture_link in lecture_links]

with open(file_name , "w" , encoding="utf-8") as file :
    fields_name = ["Lecture Name" , "Lecture Link"]
    wr = csv.DictWriter(file , fieldnames=fields_name)
    wr.writeheader()
    for item in range(len(lecture_titles)):
        wr.writerow({"Lecture Name":lecture_title_list[item] , "Lecture Link":lecture_links_list[item]})

df = pd.read_csv(file_name)
print(df)