def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    words_count = get_count(text)
    chars_frequency = get_char_frequency(text)
    char_list = convert_frequencies_to_list(chars_frequency)
    report = get_report(char_list)
    print(report)

def get_book_text(path):
    with open(path) as f:
        return f.read()

def get_count(string):
  words = string.split()
  return len(words)

def get_char_frequency(string):
  text = string.lower()
  char_set = set(text)
  chars={}
  for char in text:
    if char in chars:
      chars[char]+=1
    else:
      chars[char]=1
  return chars

def convert_frequencies_to_list(frequencies):
  frequencies_list=[]
  for char in frequencies:
    frequencies_list.append({"character": char, "count": frequencies[char]})
  return frequencies_list

def sort_on(dict):
    return dict["count"]

def get_report(char_list):
  char_list.sort(reverse=True, key=sort_on)
  report_lines = [f'The {char["character"]} character was found {char["count"]} times' for char in char_list if char["character"].isalpha() ]
  report= "\n".join(report_lines)
  return report

main()