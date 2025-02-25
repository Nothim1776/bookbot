def word_counter(text):
	text_string = text.split()
	word_count = 0
	for word in text_string:
		word_count += 1
	return word_count

def letter_counter(text):
	lowered_text = text.lower()
	letter_count = {}
	for letter in lowered_text:
		if letter in letter_count:
			letter_count[letter] += 1
		else:
			letter_count[letter] = 1
	return letter_count
def sort_on(dict):
	return dict["count"]

def letter_sort(letter_count):
	letter_list = []
	for character, count in letter_count.items():
		temp_dict = {"character": character, "count": count}
		letter_list.append(temp_dict)
	letter_list.sort(reverse=True, key = sort_on)
	return letter_list
