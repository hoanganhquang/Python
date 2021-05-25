from bs4 import BeautifulSoup
import lxml

with open("website.html", "r") as file:
    data = file.read()

soup = BeautifulSoup(data, "html.parser")
print(soup.h1.getText())
