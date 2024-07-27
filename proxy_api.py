import requests


def scrape_proxies():
    url = "https://api.proxyscrape.com/v2/?request=displayproxies&protocol=http,socks4,socks5&timeout=2000&country=all&ssl=yes&anonymity=elite"
    response = requests.get(url)
    proxies = [x.strip() for x in response.text.split("\n")]
    return proxies




