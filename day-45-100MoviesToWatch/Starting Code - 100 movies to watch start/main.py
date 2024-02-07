import pandas
import requests
from bs4 import BeautifulSoup

URL = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"

# Write your code below this line 👇

response = requests.get(url=URL)
web_data = response.text

soup = BeautifulSoup(web_data, "html.parser")

movies_tag = soup.findAll(name="h3", class_="title")

list_with_movies = [movie.get_text() for movie in movies_tag]
# list_with_movies = []
# for movie_tag in movies_tag:
#     list_with_movies.append(movie_tag.get_text())

list_with_movies.reverse()

with open("movies.txt", "w", encoding='utf-8') as file:
    for movie in list_with_movies:
        file.write(movie + "\n")