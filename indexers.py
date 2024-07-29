import requests
import markdown
from bs4 import BeautifulSoup


def scrape_trackers():
    url = "https://raw.githubusercontent.com/Shakil-Shahadat/awesome-piracy/main/Readme.md"
    all_trackers = []
    response = requests.get(url)
    md_text = response.text
    md_html = markdown.markdown(md_text)

    soup = BeautifulSoup(md_html, "html.parser")

    for heading in soup.find_all("h4"):
        if heading.text == "Public Trackers":
            next_element = heading.find_next_sibling()
            for link in next_element.find_all("a"):
                all_trackers.append(link.get("href"))
    return all_trackers
