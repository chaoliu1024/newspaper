import re

from newspaper.article import Article

import newspaper
# url = 'http://fox13now.com/2013/12/30/new-year-new-laws-obamacare-pot-guns-and-drones/'
#
# article = Article(url)
#
# article.parse()
# article.authors
# article.text
# cnn_paper = newspaper.build('http://cnn.com')

url = 'http://news.163.com/17/0312/10/CFAP3Q9G000189FH.html'
a = Article(url, language='zh') # Chinese
a.download()

a.parse()

print(a.keywords)
print("===============")
print(a.title)
print("===============")
print(a.authors)
print("===============")
print(a.text[:150])

# filter_regex = re.compile(r'[^a-zA-Z0-9\ ]')
# title_text_h1 = "我与总书记议国是：建设社会稳定长治久安新AA边疆,总书记 社会稳定 全国人大代表00000ddd"
# filter_title_text_h1 = filter_regex.sub('', title_text_h1).lower()
# print(filter_title_text_h1)
#
# print(re.sub(r'[^a-zA-Z0-9\ ]', '', title_text_h1))
#
# inputStr = "hello 123 world 456"
# replacedStr = re.sub("[^\d+]", "222", inputStr)
# print(replacedStr)
