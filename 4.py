import csv
import os

def process_csv(input_filepath, output_filepath, stats_filepath):
    with open(input_filepath, 'r', newline='', encoding='utf-8') as infile:
      reader = csv.DictReader(infile)
      header = reader.fieldnames
      rows = list(reader)

    # 1. Удалите столбец expiration_date
    new_header = [h for h in header if h != 'expiration_date']
    modified_rows = []
    for row in rows:
      new_row = {k: v for k, v in row.items() if k != 'expiration_date'}
      modified_rows.append(new_row)

    # 2-4. Найдите среднее, максимум и минимум по столбцу price
    prices = [float(row['price']) for row in rows if row['price']]
    average_price = sum(prices) / len(prices) if prices else 0
    max_price = max(prices) if prices else 0
    min_price = min(prices) if prices else 0

    # 5. Отфильтруйте значения по category
    filtered_rows = [row for row in modified_rows if row['category'] == 'Бакалея']

    with open(output_filepath, 'w', newline='', encoding='utf-8') as outfile:
      writer = csv.DictWriter(outfile, fieldnames=new_header)
      writer.writeheader()
      writer.writerows(filtered_rows)


    with open(stats_filepath, 'w', encoding='utf-8') as statsfile:
      statsfile.write(f"{average_price}\n")
      statsfile.write(f"{max_price}\n")
      statsfile.write(f"{min_price}\n")

if __name__ == '__main__':
    input_csv = "./resources/fourth_task.txt"
    output_csv = "./4_result.csv"
    stats_file = "./4_stats.txt"
    process_csv(input_csv, output_csv, stats_file)