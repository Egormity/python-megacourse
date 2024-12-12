import re
from nltk.corpus import stopwords
from nltk.sentiment import SentimentIntensityAnalyzer

stopwords_english = stopwords.words("english")
analyzed = SentimentIntensityAnalyzer()

PATH = r"C:\Users\kotla\Desktop\python-megacourse\008\001 miracle-in-the-andes.txt"

with open(PATH, "r", encoding="utf-8") as file:
    book = file.read()
    

# 
# matches = book.count("Chapter")
# print(result)

# 
# pattern = r"Chapter \d+"
# matches = re.findall(pattern, book)
# print(matches)

# 
# pattern = r"[A-Z]{1}[^.]* love[^a-zA-Z]+[^.]*."
# matches = re.findall(pattern, book)
# print(len(matches))

# 
# pattern = r"[A-Z]{1}[^\n]* love[^a-zA-Z]+[^\n]*."
# matches = re.findall(pattern, book)
# print(matches[0])

# WORDS OCCURRENCES
# pattern = r"[a-zA-Z]+"
# words = re.findall(pattern, book)
# dic = {}
# for word in words:
#     w = word.lower()
#     if w in dic: dic[w] += 1
#     else: dic[w] = 1

# words_list = sorted(dic.items(), key=lambda x: x[1], reverse=True)
# print(words_list)

#
# print(stopwords_english)
# filtered_words = []
# for word, count in words_list:
#     if word not in stopwords_english:
#         filtered_words.append((word, count))

# print(filtered_words)

# MOST NEGATIVE AND POSITIVE CHAPTERS
# print(analyzed.lexicon(book))

chapters = re.split(r"Chapter \d+", book)

chapter_sentiment = []
for i, chapter in enumerate(chapters[0:1]):
    chapter_sentiment.append((f"Chapter {i + 1}", analyzed.polarity_scores(chapter)))

print(chapter_sentiment)