import requests

from bs4 import BeautifulSoup

# get html from website
response = requests.get(url="https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/")
response.raise_for_status

# create soup
soup = BeautifulSoup(response.text, "html.parser")

# parse movie names
movies_tags = soup.find_all(name="h3", class_="title")
movies = [f"{tag.getText()}\n" for tag in movies_tags]
movies = movies[::-1]

# store movie names along with their ranking
# in movies.txt
with open("movies.txt", "w") as file:
    file.writelines(movies)