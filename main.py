from stats import letter_counter, letter_sort, word_counter
import sys

if len(sys.argv) != 2:
	print("Usage: python3 main.py <path_to_book>")
	sys.exit(1)

def get_book_text(path):
	with open(path) as f:
		file_contents = f.read()
		return file_contents

def pull_book():
	path = sys.argv[1]
	text = get_book_text(path)
	return(text)

text = pull_book()
letter_dict = letter_counter(text)
sorted_list = letter_sort(letter_dict)
word_count = word_counter(text)

print("========== BOOKBOT ==========")
print(f"Analyzing book found at {sys.argv[1]}.")
print("---------- Word Count ----------")
print(f"Found {word_count} total words")
print("---------- Character Count ----------")
for letter in sorted_list:
	character = letter["character"]
	if character.isalpha():
		print(f"{character}: {letter["count"]}")
