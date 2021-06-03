from selenium import webdriver
from bs4 import BeautifulSoup
import pandas as pd
import matplotlib.pyplot as plt
from wordcloud import WordCloud


titleClass = "h1"
titleName = "_2IIDsE _3I-nQy"
ratingClass = "span"
ratingName = "FDDgZI"
synopsisClass = "div"
synopsisName = "_1XdgZK"

storeFrontURL = "https://www.amazon.com/gp/video/storefront"
vidDownloadURL = "/gp/video/detail"


driver = webdriver.Chrome(executable_path="chromedriver")
driver.get(storeFrontURL)


videoLinks = []
titles = []
ratings = []
synopsis = []


def scrapeText(lst, classType, className):
    findClass = soup.find_all(classType, class_=className)
    if(len(findClass) == 0):
        lst.append(None)
    else:
        for n in findClass:
            if className == ratingName:
                print("K", end="")
                lst.append(float(n.text[-3:]))
            else:
                lst.append(n.text)


elems = driver.find_elements_by_xpath("//a[@href]")
for elem in elems:
    if vidDownloadURL in elem.get_attribute("href"):
        videoLinks.append(elem.get_attribute("href"))

videoLinks = list(set(videoLinks))
print("Number of video Links: ", len(videoLinks))
# or
# videoLinks = list(dict.fromkeys(videoLinks))

for i in range(0, len(videoLinks)):
    driver.get(videoLinks[i])
    content = driver.page_source
    soup = BeautifulSoup(content)

    scrapeText(titles, titleClass, titleName)
    scrapeText(ratings, ratingClass, ratingName)
    scrapeText(synopsis, synopsisClass, synopsisName)


print("Titles len: ", len(titles), " Rating: ",
      len(ratings), " Synopsis: ", len(synopsis))
data = {"Title": titles, "Rating": ratings, "Synopsis": synopsis}
df = pd.DataFrame(data)
df.to_csv('PrimeVid.csv', index=False, encoding='utf-8')


def wordcloud(df, filename):
    if len(df) > 1:
        text = ' '.join(df.Synopsis)
        wordcloud = WordCloud().generate(text)

        plt.imshow(wordcloud, interpolation='bilinear')
        plt.axis("off")

        plt.savefig(filename+".png")


dfBelow6 = df.loc[(df['Rating']) < 6]
df6To8 = df.loc[(df['Rating']) >= 6 & (df['Rating'] < 8)]
dfAbove8 = df.loc[(df['Rating']) >= 8]

wordcloud(dfBelow6, "below6")
wordcloud(df6To8, "6To8")
wordcloud(dfAbove8, "above8")
