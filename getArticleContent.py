from bs4 import BeautifulSoup
import requests
import click

@click.command()
@click.option('--url', prompt="Article url", help="The article url from GNN to parse")
def getArticleText(url):
    data = requests.get(url)
    soup = BeautifulSoup(data.text, features="lxml")
    post = soup.find(attrs={"class": "td-post-content"})
    postContent = post.find_all('p')
    text = ""
    for line in range(0, len(postContent) - 1):
        """
        if (postContent[line].find("<a href") == -1):
            text += postContent[line].text
        else:
            continue
        """
        text += postContent[line].text

    print(text)
    return text

if __name__ == "__main__":
    getArticleText()

