import requests
from bs4 import BeautifulSoup

def parse_json_to_html(api_url, html_filepath):
    response = requests.get(api_url)
    data = response.json()

    soup = BeautifulSoup("<html><head><title>Users Data</title></head><body></body></html>", 'html.parser')
    body = soup.body

    table = soup.new_tag("table")
    table.append(soup.new_tag("thead"))
    thead = table.find("thead")

    first_item = data[0]
    tr_head = soup.new_tag("tr")
    for key in first_item.keys():
      th = soup.new_tag("th")
      th.string = key.title()
      tr_head.append(th)

    thead.append(tr_head)
    table.append(soup.new_tag("tbody"))
    tbody = table.find("tbody")

    for user in data:
        tr = soup.new_tag("tr")
        for value in user.values():
            td = soup.new_tag("td")
            td.string = str(value)
            tr.append(td)
        tbody.append(tr)


    body.append(table)

    with open(html_filepath, 'w', encoding='utf-8') as f:
        f.write(str(soup))

if __name__ == '__main__':
    api_url = "https://jsonplaceholder.typicode.com/users"
    html_filepath = "./6_result.html"
    parse_json_to_html(api_url, html_filepath)