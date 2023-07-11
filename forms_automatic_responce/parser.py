import requests
from bs4 import BeautifulSoup as BS



def fetch_information(resume_url: str) -> list:
    response = requests.get(resume_url, headers={'User-agent': 'Edge/12.246'})
    html = BS(response.content, "html.parser")

    res = []


    title = html.select(".resume-block__title-text-wrapper > .bloko-header-2 > "
                        ".resume-block__title-text")[0].text
    res.append(title)




    sex_text = html.select('[data-qa="resume-personal-gender"]')[0].text
    if sex_text[0].upper() == 'M' or sex_text[0].upper() == 'М':
        sex = True
    else:
        sex = False
    res.append(sex)
    print(res)

    return res


resume_url = "https://astana.hh.kz/search/vacancy?text=Web+%D0%BF%D1%80%D0%BE%D0%B3%D1%80%D0%B0%D0%BC%D0%BC%D0%B8%D1%81%D1%82&from=suggest_post&area=159"
response = requests.get(resume_url, headers={'User-agent': 'Edge/12.246'})
html = BS(response.content, "html.parser")
row = fetch_information(resume_url)
print(row)


