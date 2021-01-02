import random
import pretty_midi
import numpy as np


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
	# text [2, 4, 1, 3]
	for i in range(len(text) - order):
		ngram = tuple(text[i:i+order])

		if ngram not in ngram_chars:
			ngram_chars[ngram] = [text[i+order]]
		else:
			ngram_chars[ngram].append(text[i+order])

	return ngram_chars

# generate
def gen_sequence(order, ngram_chars, start_word, iterations):
	result = list(start_word)
	cur_word = start_word
	for i in range(iterations):
		if cur_word not in ngram_chars:
			break
		
		char_ls = ngram_chars[cur_word]
		if not char_ls:	
			break
		
		char = random.choice(char_ls)
		result.append(char)
		cur_word = (cur_word[-1], char)

	return result


def text_to_midi(text, bpm, output_path):
	guitar_high = pretty_midi.PrettyMIDI()
	# Create an Instrument instance for a cello instrument
	guitar_program = pretty_midi.instrument_name_to_program('Acoustic Grand Piano')
	guitar = pretty_midi.Instrument(program=guitar_program)
	
	sec_beat = 60 / bpm # beat -> sec
	unit = 0.25 # the smallest unit is Sixteenth note, 1/4 beat
	start = 0


	i = 0
	while i < len(text):
		num = text[i]
		dur = unit * sec_beat

		if i + 1 < len(text):
			while text[i] == text[i+1]:
				
				i += 1
				dur += unit * sec_beat
				if i >= len(text):
					break
		note_number = int(num) + 52
		end = start + dur

		start = end
		note = pretty_midi.Note(
			velocity=100, pitch=note_number, start=start, end=end)
		guitar.notes.append(note)
		i += 1

	# Add the cello instrument to the PrettyMIDI object
	guitar_high.instruments.append(guitar)
	# Write out the MIDI data
	guitar_high.write(output_path)


if __name__ == '__main__':
	major = [0, 2, 4, 7, 9]
	example = random.choices(major, k=16)
	print('example', example)
	order = 2
	ngram_chars = gen_possiblities(example, order)
	print(ngram_chars)
	start_word = tuple(example[:2])
	result = gen_sequence(order, ngram_chars, start_word, 48)
	print('result', result)
	output_path = 'result.mid'
	text_to_midi(example, 90, 'example.mid')
	text_to_midi(result, 90, output_path)


