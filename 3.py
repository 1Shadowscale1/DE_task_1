import re
import math

def process_data(input_filepath, output_filepath):
    with open(input_filepath, 'r') as infile, open(output_filepath, 'w') as outfile:
        for line in infile:
            numbers_str = line.split()
            numbers = []
            for num_str in numbers_str:
                if num_str == "N/A":
                    numbers.append(None)
                else:
                    numbers.append(float(num_str))

            for i in range(len(numbers)):
                if numbers[i] is None:
                    left = numbers[i-1] if i > 0 else None
                    right = numbers[i+1] if i < len(numbers)-1 else None
                    if left is not None and right is not None:
                        numbers[i] = (left + right) / 2
                    elif left is not None:
                        numbers[i] = left
                    elif right is not None:
                        numbers[i] = right

            filtered_numbers = [num for num in numbers if num < 0 or (num > 0 and math.sqrt(num) > 50)]
            line_sum = sum(filtered_numbers)
            outfile.write(f"{line_sum}\n")

if __name__ == "__main__":
    input_file = "./resources/third_task.txt"
    output_file = "./3_result.txt"
    process_data(input_file, output_file)
