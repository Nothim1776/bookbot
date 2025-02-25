from stats import letter_counter, letter_sort, word_counter

def get_book_text(path):
	with open(path) as f:
		file_contents = f.read()
		return file_contents

def pull_book():
	path = "books/frankenstein.txt"
	text = get_book_text(path)
	return(text)

text = pull_book()
letter_dict = letter_counter(text)
sorted_list = letter_sort(letter_dict)
word_count = word_counter(text)

print("========== BOOKBOT ==========")
print("Analyzing book found at books/frankenstein.txt...")
print("---------- Word Count ----------")
print(f"Found {word_count} total words")
print("---------- Character Count ----------")
for letter in sorted_list:
	character = letter["character"]
	if character.isalpha():
		print(f"{character}: {letter["count"]}")
