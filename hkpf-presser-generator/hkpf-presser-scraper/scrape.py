import scraper


# NOVEMBER 2014 is the first month that the police force uses the fucky old template
# url = "https://www.police.gov.hk/ppp_en/03_police_message/pr/pr_archives.html?month=201907"
# url = "https://www.police.gov.hk/ppp_en/03_police_message/pr/pr201411.html"

urls = [
    "https://www.police.gov.hk/ppp_en/03_police_message/pr/pr_archives.html?month=201911",
    "https://www.police.gov.hk/ppp_en/03_police_message/pr/pr_archives.html?month=201910",
    "https://www.police.gov.hk/ppp_en/03_police_message/pr/pr_archives.html?month=201909",
    "https://www.police.gov.hk/ppp_en/03_police_message/pr/pr_archives.html?month=201908",
    "https://www.police.gov.hk/ppp_en/03_police_message/pr/pr_archives.html?month=201907",
    "https://www.police.gov.hk/ppp_en/03_police_message/pr/pr_archives.html?month=201906"
    "https://www.police.gov.hk/ppp_en/03_police_message/pr/pr_archives.html?month=201905"
]

f = open('raw', "w+", encoding="utf-8")

for url in urls:
    result = scraper.scrape_presser(url)
    f.write(result)

f.close()
