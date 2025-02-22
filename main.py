def get_book_text(path):
	with open(path) as f:
		file_contents = f.read()
		return file_contents

def pull_book():
	path = "books/frankenstein.txt"
	text = get_book_text(path)
	return(text)

def word_count():
	text = pull_book()
	words = text.split()
	num_words = 0
	for word in words:
		num_words += 1
	print(f"{num_words} words found in the document")


word_count()
