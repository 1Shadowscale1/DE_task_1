import csv
from bs4 import BeautifulSoup

def parse_html_to_csv(html_filepath, csv_filepath):
    with open(html_filepath, 'r', encoding='utf-8') as file:
        html_content = file.read()
    soup = BeautifulSoup(html_content, 'html.parser')
    table = soup.find('table', {'id': 'product-table'})

    headers = [th.text.strip() for th in table.find_all('th')]
    rows = table.find_all('tr')[1:]

    with open(csv_filepath, 'w', newline='', encoding='utf-8') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(headers)

        for row in rows:
            cells = row.find_all('td')
            row_data = []
            for cell in cells:
                text = cell.text.strip()
                row_data.append(text)
            writer.writerow(row_data)

if __name__ == '__main__':
    html_filepath = 'fifth_task.html'
    csv_filepath = 'output.csv'
    parse_html_to_csv(html_filepath, csv_filepath)