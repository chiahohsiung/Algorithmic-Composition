import numpy

# markov chain

f = open('test_text', 'r')
text = f.read()
print(text)
# step 1 all the ngrams count all the following char for every ngram
# step 2 generate 

# example 
# hello word
# ngram order <- 3
# hel ell llo

# step 1 and 2
order = 6

ngram_chars = {}
for i in range(len(text) - order):
	ngram = text[i:i+order]

	if ngram not in ngram_chars:
		ngram_chars[ngram] = [text[i+order]]
	else:
		ngram_chars[ngram].append(text[i+order])
	
print(ngram_chars)



