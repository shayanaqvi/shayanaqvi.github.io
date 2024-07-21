from yattag import Doc
from yattag import indent
from rich.console import Console
from rich.panel import Panel
from rich.text import Text
from datetime import date
import glob
import os

doc, tag, text = Doc().tagtext()
console = Console()

files = glob.glob('*.html')
sorted_files = sorted(files, key=lambda x: int(os.path.basename(x).split('-')[0]))
date = date.today()

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

def construct_html(date, article_title, article_description):
    doc.asis('<!DOCTYPE html>')
    with tag('html'):
        doc.attr(lang="en")

        with tag('head'):
            with tag('link'):
                doc.attr(rel="icon", type="image/x-icon", href="../favicon.svg")
            with tag('link'):
                doc.attr(rel="stylesheet", href="../styles.css")
            with tag('meta'):
                doc.attr(name="viewport", content="width=device-width, initial-scale=1")
            with tag('meta'):
                doc.attr(name="description", content=f"{article_description}")
            with tag('title'):
                text(f"{article_title} | Shayan Naqvi")

        with tag('body'):
            with tag('div'):
                doc.attr(id="header")
                with tag('a'):
                    doc.attr(href="../index.html")
                    text("Main Menu")
                with tag('a'):
                    doc.attr(href="../works.html")
                    text("Works")

            with tag('div'):
                doc.attr(id="content-container")

                with tag('h1'):
                    text(article_title)

                with tag('p'):
                    pass

                with tag('p'):
                    doc.attr(klass="closing")
                    text(f"This article was written on {date}. If you have any thoughts, feel free to send me an email with them. Have a nice day!")

    return indent(doc.getvalue())

# prompt for article title and description
console.print("Name your article:", style="blue")
article_title = input("→ ")
console.print("Describe your article:", style="blue")
article_description = input("→ ")
article_index = get_latest_article_index() + 1
filename = construct_filename(article_index)

with open(filename, 'w') as file:
    file.write(construct_html(date, article_title, article_description))

console.print(Panel(Text(f"{filename} created!"), style="green"))
