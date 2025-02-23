from stats import word_count

def get_book_text(path):
	with open(path) as f:
		file_contents = f.read()
		return file_contents

def pull_book():
	path = "books/frankenstein.txt"
	text = get_book_text(path)
	return(text)

text = pull_book()
num_words = word_count(text)
print(f"{num_words} words found in the document")
