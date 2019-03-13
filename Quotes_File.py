import requests
from bs4 import BeautifulSoup
import io
from random import choice
from csv import DictWriter,DictReader

######################################################################              WEB SCRAPER            ###################################################################################
####################################################################################################################################################################################################
#
# base_url = "http://quotes.toscrape.com"
# url = "/page/1/"
# all_quotes =[]
#
# with io.open("AuthorQuotes.csv","w",encoding="utf-8") as csv_file:
#     fieldnames = ["Author","Quote", "Link"]
#     csv_writer = DictWriter(csv_file, fieldnames = fieldnames)
#     csv_writer.writeheader()
#
#
#     while url:
#         response = requests.get(f"{base_url}{url}")
#         print(f"Now Scraping Quotes | {base_url}{url}")
#         soup = BeautifulSoup(response.text, "html.parser")
#         quotes = soup.find_all(class_="quote")
#
#         for quote in quotes:
#             speech = quote.find(class_="text").get_text(),
#             author = quote.find(class_="author").get_text(),
#             link = quote.find("a")["href"]
#             csv_writer.writerow({"Author": author, "Quote" : speech, "Link" : link})
#         next_btn = soup.find(class_="next")
#         url = next_btn.find("a")["href"] if next_btn else None
#



######################################################################              QUOTE GAME WITH CSV_FILE               ###################################################################################
####################################################################################################################################################################################################



base_url = "http://quotes.toscrape.com"
url = "/page/1/"
all_quotes =[]


with open("FamousQuotes.csv", "r",encoding="utf-8") as file:
    csv_reader = DictReader(file)

    quotes = [line for line in csv_reader]


random_picker = choice(quotes)
link = random_picker.get("Link")
random_quote = random_picker.get("Quote")
author = random_picker.get("Author")
first_letter_surname = author.split(" ")[1][0]

response = requests.get(f"{base_url}{url}")
soup = BeautifulSoup(response.text, "html.parser")
res = requests.get(f"{base_url}{link}")
soup = BeautifulSoup(res.text, 'html.parser')
birth_date = soup.find(class_= "author-born-date").get_text()
birth_place = soup.find(class_="author-born-location").get_text()

print("Here's a Quote")
print(random_quote)
print(random_picker.get("Author"))

guesses = 4
guess = ''

while True :
    if guess != author:
        guesses -= 1
    guess = input("Who was the author of this quote ? ")


    if guess == author:
        print("Congratiulations you got it!")
        break
    elif guesses == 3:
        print(f"Heres a hint : ")
        print(f"The author was born in {birth_date} and born {birth_place}")
    elif guesses == 2:
        print( f"Guesses left : {guesses}")
        print(f"Here's the first letter of the name of the Author : {author[2]}")
    elif guesses == 1:
            print(f"Here's the first letter of the Surname : {first_letter_surname}")
    else:
        print(f"You didn't get it, too bad. The answer was : {author}")
        break





















# with open('lines.csv',"r",encoding="utf-8") as file:
#     csv_reader = reader(file)
#
#     lines = [line for line in csv_reader]
#
#
# print(lines)



# quote = choice(lines)
# print("Here is a quote")
# print(quote[1])
#
#
# guesses = 4
# guess = input("Who is the author? : ")
# while guess != quote[0]:
#     print(quote[0])
#     print("That is wrong")
#     guesses -= 1
#     print(guesses)
#     if guess != quote[0]:
#         print(f"The first letter of the author is {quote[0][0]}")









# with open("Quotes.csv","w") as csv_file:
#     csv_writer = writer(csv_file)
#     csv_writer.writerow
#
#     for quote in quotes:
#         speech = quote.find(class_= "text").get_text()
#         author = quote.find(class_= "author").get_text()
#         link   = quote.find("a")["href"]
#         print(author,speech,link)
#         csv_writer.writerow([author,speech,link])














