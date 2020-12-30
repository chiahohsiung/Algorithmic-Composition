import random


# markov chain
# step 1 all the ngrams count all the following char for every ngram
# step 2 generate 

# example 
# hello word
# ngram order <- 3
# hel ell llo

# step 1 and 2
def gen_possiblities(text, order):
	ngram_chars = {}
	for i in range(len(text) - order):
		ngram = text[i:i+order]

		if ngram not in ngram_chars:
			ngram_chars[ngram] = [text[i+order]]
		else:
			ngram_chars[ngram].append(text[i+order])

	return ngram_chars

# generate
def gen_sequence(order, ngram_chars, start_word, iterations):
	cur_word = start_word
	for i in range(iterations):
		# print('cur_word', cur_word)
		if cur_word not in ngram_chars:
			break
		
		char_ls = ngram_chars[cur_word]
		if not char_ls:	
			break
		
		char = random.choice(char_ls)
		start_word += char
		cur_word = start_word[-order:]

	return start_word


if __name__ == '__main__':
	f = open('tongue_twister', 'r')
	text = f.read().lower()
	order = 3
	ngram_chars = gen_possiblities(text, order)
	start_word = 'pet'
	result = gen_sequence(order, ngram_chars, start_word, 100)
	print(result)


