import numpy
import random


# markov chain

f = open('tongue_twister', 'r')
text = f.read().lower()
# print(text)

# step 1 all the ngrams count all the following char for every ngram
# step 2 generate 

# example 
# hello word
# ngram order <- 3
# hel ell llo

# step 1 and 2
order = 3

ngram_chars = {}
for i in range(len(text) - order):
	ngram = text[i:i+order]

	if ngram not in ngram_chars:
		ngram_chars[ngram] = [text[i+order]]
	else:
		ngram_chars[ngram].append(text[i+order])
# sorted_ngram_chars = {k: v for k, v in sorted(ngram_chars.items(), key=lambda item: len(item[1]))}	
# for k, v in sorted_ngram_chars.items():
# 	print(k, v)
# 	break
print(ngram_chars)
# generate
result = 'pet'
cur_word = result
iterations = 100
for i in range(iterations):
	# print('cur_word', cur_word)
	if cur_word not in ngram_chars:
		break
	
	char_ls = ngram_chars[cur_word]
	if not char_ls:	
		break
	
	char = random.choice(char_ls)
	result += char
	cur_word = result[-order:]

print(result)


