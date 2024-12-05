def main():
  book_path = "books/frankenstein.txt"
  print(f"--- Begin report of {book_path} ---")
  text = get_book_text(book_path)
  word_count = get_word_count(text)
  print(f"{word_count} words found in the document \n")
  char_dict = get_character_count(text)
  generate_report(char_dict)
  print("--- End report ---")


def get_book_text(path):
  with open(path) as f:
    return f.read()

def get_word_count(text):
  words = text.split()
  return len(words)

def get_character_count(text):
  lowered_text = text.lower()
  character_count = {}
  for char in lowered_text:
    if char.isalpha():
      if char in character_count:
        character_count[char] += 1
      else:
        character_count[char] = 1
  return character_count

def generate_report(dict):
  char_count_list = convert_dict_to_list(dict)
  char_count_list.sort(reverse=True, key=sort_on)
  for dict in char_count_list:
    print(f"The {dict['char']} character was found {dict['count']} times")

def convert_dict_to_list(dict):
  new_list = []
  for key, value in dict.items():
    new_list.append({"char": key, "count": value})
  return new_list

def sort_on(dict):
  return dict["count"]

main()