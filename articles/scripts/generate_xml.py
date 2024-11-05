from yattag import Doc
from yattag import indent
from rich.console import Console
from rich.panel import Panel
from rich.text import Text
from datetime import datetime, timezone, timedelta
import pyperclip
import glob
import os

doc, tag, text = Doc().tagtext()
console = Console()

files = glob.glob('*.html')
sorted_files = sorted(files, key=lambda x: int(os.path.basename(x).split('-')[0]))

# get the index of the latest article
def get_latest_article_index():
    latest_filename = sorted_files[len(sorted_files) - 1].replace("./", "")
    latest_article_name = latest_filename.replace(".html", "")
    latest_article_name_array = latest_article_name.split("-")
    latest_article_index = latest_article_name_array[0]
    return int(latest_article_index)

def construct_filename(latest_article_index):
    article_title_words = []
    filename = f"{int(latest_article_index)}"

    for word in article_title.split(" "):
        article_title_words.append(word)

    for word in article_title_words:
        filename += f"-{word}"

    filename += ".html"
    return filename.lower()

def generate_xml(filename, artitle_title):
    with tag('item'):
        with tag('title'):
            text(article_title)
        with tag('link'):
            text(f"https://shayanaqvi.github.io/articles/{filename}")
        with tag('guid'):
            text(f"https://shayanaqvi.github.io/articles/{filename}")
        with tag('pubDate'):
            text(rfc_822_date)
             
    return indent(doc.getvalue())

now_utc = datetime.now(timezone.utc)
utc_offset = '+0500'
rfc_822_date = now_utc.strftime('%a, %d %b %Y %H:%M:%S ') + utc_offset

console.print("Article name:", style="blue")
article_title = input("→ ")
article_index = get_latest_article_index()
filename = construct_filename(article_index)

pyperclip.copy(generate_xml(filename, article_title))
console.print(Panel(Text(f"XML copied to clipboard!"), style="green"))



