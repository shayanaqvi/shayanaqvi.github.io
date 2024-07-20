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

date = date.today()

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
console.print("Filename for this article:", style="blue")
filename = input("→ ")
filename = f"{filename}.html"

with open(filename, 'w') as file:
    file.write(construct_html(date, article_title, article_description))

console.print(Panel(Text(f"{filename} created!"), style="green"))
