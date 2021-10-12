import requests
from lxml import etree


def main():
    result = requests.get("https://developer.apple.com/news/")
    if 200 == result.status_code:
        html_code = etree.HTML(result.text)
        articles = html_code.xpath("//section[@class='row-full']")
        for article in articles:
            title = article.xpath("./section/a[@class='article-title']/h2/text()")[0]
            time = article.xpath("./section/div[@class='article-text-wrapper']/p/text()")[0]
            time = time_format(time=time)
            requests.post("127.0.0.1:8080/api/apple_news",data={"title": title, "time": time})

def time_format(time):
    strlist = time.split(' ')
    print(strlist)
    if 3 == len(strlist):
        month = strlist[0]
        months = {"January": "1",
                  "February": "2",
                  "March": "3",
                  "April": "4",
                  "May": "5",
                  "June": "6",
                  "July": "7",
                  "August": "8",
                  "September": "9",
                  "October": "10",
                  "November": "11",
                  "December": "12"}
        if month in months:
            month = months[month]
        day = strlist[1]
        day = day.replace(',', '')
        year = strlist[2]
        return year + month + day

    else:
        return ""


if __name__ == '__main__':
    main()
