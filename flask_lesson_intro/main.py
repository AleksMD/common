from flask import Flask, render_template
from utils import get_data
from collections import namedtuple

app = Flask(__name__)


def html_page_db_creator(page_info_from_json):
    html_page = namedtuple('Page', 'title text')
    return {list(page.values())[0].replace(' ', '_').lower():
            html_page(*page.values()) for page in page_info_from_json}


@app.route('/')
def get_home_page():
    return render_template("home.html", data=get_data())


@app.route('/<page>')
def alarm_clock(page):
    html_pages_db = html_page_db_creator(get_data())
    if page in html_pages_db:
        html_page_data = html_page_db_creator(get_data()).get(page)
        return render_template(f"{page}.html", title=html_page_data.title,
                               text=html_page_data.text)
    else:
        return render_template(f"{page}.html")


if __name__ == "__main__":
    app.run(debug=True)
