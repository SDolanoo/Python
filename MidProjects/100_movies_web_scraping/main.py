import requests
from bs4 import BeautifulSoup

URL = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"

# Write your code below this line 👇

response = requests.get(URL)
movies_web_page = response.text
soup = BeautifulSoup(movies_web_page, "html.parser")

name = soup.find_all(name="h3", class_="title")

list_of_titles = [title.getText().encode('ascii', errors='ignore') for title in name]

with open("movies.txt", "w") as file:
    for line in list_of_titles[::-1]:
        file.write(f"{line.decode('ascii', errors='ignore')}\n")
