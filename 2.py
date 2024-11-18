import re

def process_data(input_filepath, output_filepath):
  averages = []
  with open(input_filepath, 'r') as infile:
    for line in infile:
      numbers = [float(x) for x in re.findall(r'\d+\.?\d*', line)]
      positive_numbers = [num for num in numbers if num > 0]
      if positive_numbers:
        average = sum(positive_numbers) / len(positive_numbers)
        averages.append(average)
      else:
        averages.append(0)

  max_val = max(averages)
  min_val = min(averages)

  with open(output_filepath, 'w') as outfile:
    for avg in averages:
      outfile.write(f"{avg}\n")
    outfile.write("-----------\n")
    outfile.write(f"{max_val}\n")
    outfile.write(f"{min_val}\n")


if __name__ == "__main__":
  input_file = "./resources/second_task.txt"
  output_file = "./2_result.txt"
  process_data(input_file, output_file)