from stats import letter_count

def get_book_text(path):
	with open(path) as f:
		file_contents = f.read()
		return file_contents

def pull_book():
	path = "books/frankenstein.txt"
	text = get_book_text(path)
	return(text)

text = pull_book()
letter_dict = letter_count(text)
print(letter_dict)
