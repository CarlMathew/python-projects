import html
from bs4 import BeautifulSoup
import lxml
import requests

response = requests.get(url="https://news.ycombinator.com/")
response.raise_for_status()
yc = response.text

soup = BeautifulSoup(yc, "html.parser")

answer = soup.find_all(name = "span", class_ = "titleline")

article_tag = soup.find_all(name = "a")
article_score = [upvote.getText() for upvote in soup.find_all(class_ = "score")]
article_links = []
dictionaries_news = {}
for tag in article_tag:
    tag_text = tag.get("href")
    if tag_text[:5] == "https":
        article_links.append(tag_text)
for score, link, title in zip(article_score, article_links, answer):
    dictionaries_news[title.getText()] = {"link":link, "score": int(score.split(" ")[0])}
max_number = 0
numbers = []
all_titles = []
for title, rows in dictionaries_news.items():
    numbers.append(rows["score"])
    all_titles.append(title)
    if rows["score"] > max_number:
        max_number = rows["score"]

index_number = numbers.index(max_number)
max_title = all_titles[index_number]

print(f"title:{max_title}, Info:{dictionaries_news[max_title]}")

# with open("website.html", "r") as f:
#     file = f.read()
#
# soup = BeautifulSoup(file, "html.parser")
# # print(soup)
# # print(soup.title)
# # print(soup.title.name)
# # print(soup.title.string)
# # print(soup.prettify())
# #
# all_anchor_tags = soup.findAll(name = "a")
# # print(all_anchor_tags)
# #
# # for tag in all_anchor_tags:
# #     print(tag.get("href"))
# heading = soup.find(name = "h1", id = "name")
# paragraph_2 = soup.find_all(name = "p")
# # print(paragraph_2)
# name = soup.select_one(selector=".name")
# headings = soup.select(".para2")
# print(headings)