import re

def process_text_file(input_path, output_path, long_words_path):
  lines = _read_file(input_path)
  words = _extract_words(lines)
  word_frequencies = _calculate_frequencies(words)
  long_word_stats = _calculate_long_word_stats(words)

  _write_frequencies_to_file(word_frequencies, output_path)
  _write_long_word_stats_to_file(long_word_stats, long_words_path)


def _read_file(file_path):
  with open(file_path, 'r', encoding="utf-8") as file:
    return file.readlines()

def _extract_words(lines):
  words = []
  for line in lines:
    cleaned_line = re.sub(r"[',?!.-]", "", line).lower().strip()
    words.extend(cleaned_line.split())
  return words

def _calculate_frequencies(words):
  word_counts = {}
  for word in words:
    if word:
      word_counts[word] = word_counts.get(word, 0) + 1
  return sorted(word_counts.items(), key=lambda item: item[1], reverse=True)

def _calculate_long_word_stats(words):
  long_words_count = sum(1 for word in words if len(word) > 4)
  total_words_count = len(words)
  proportion = long_words_count / total_words_count if total_words_count > 0 else 0
  return {
    "long_words_count": long_words_count,
    "proportion": proportion,
  }


def _write_frequencies_to_file(frequencies, file_path):
  with open(file_path, 'w', encoding='utf-8') as file:
    for word, count in frequencies:
      file.write(f"{word}:{count}\n")

def _write_long_word_stats_to_file(stats, file_path):
  with open(file_path, 'w', encoding='utf-8') as file:
    file.write(f"Words longer than 4 characters: {stats['long_words_count']}\n")
    file.write(f"Proportion: {stats['proportion']:.4f}\n") # Format proportion to 4 decimal places


if __name__ == '__main__':
  input_file = "./resources/first_task.txt"
  output_file = "./1_result.txt"
  long_words_file = "./1_result_option_4.txt"
  process_text_file(input_file, output_file, long_words_file)