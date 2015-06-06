import requests
from histogram import Histogram
from urllib.parse import urlparse
from bs4 import BeautifulSoup


def get_html(url):
    return requests.get(url).text


def domain_from_url(url):
    parsed = urlparse(url)
    return parsed[0] + "://" + parsed[1]

REGISTER = "http://register.start.bg"
HEADERS = {
 "User-Agent":
 "User-Agent: Mozilla/5.0 (Windows NT 6.1)" +
 "AppleWebKit/537.36" +
 "(KHTML, like Gecko)" +
 "Chrome/41.0.2228.0 Safari/537.36"
}


def find_links():
    visited = set()
    h = Histogram()
    soup = BeautifulSoup(get_html(REGISTER))
    links = [link.get("href") for link in soup.find_all("a")]

    for link in links:
        if link is not None and "link.php" in link:
            try:
                target_url = REGISTER + "/" + link
                r = requests.head(target_url,
                                  headers=HEADERS,
                                  allow_redirects=True,
                                  timeout=10)
                h.add(r.headers["Server"])

                target_url = domain_from_url(r.url)
                if target_url not in visited:
                    visited.add(target_url)
            except Exception:
                print("Exception caught!")
    result = []

    for server, count in h.histogram.items():
        result.append("{}: {}".format(server, count))

    with open("result.txt", "w") as f:
        f.write("\n".join(result))
