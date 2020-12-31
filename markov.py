import random
import pretty_midi

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
		if cur_word not in ngram_chars:
			break
		
		char_ls = ngram_chars[cur_word]
		if not char_ls:	
			break
		
		char = random.choice(char_ls)
		start_word += char
		cur_word = start_word[-order:]

	return start_word


def text_to_midi(text, bpm, output_path):
	guitar_high = pretty_midi.PrettyMIDI()
	# Create an Instrument instance for a cello instrument
	guitar_program = pretty_midi.instrument_name_to_program('Acoustic Grand Piano')
	guitar = pretty_midi.Instrument(program=guitar_program)
	
	sec_beat = 60 / bpm # beat -> sec
	unit = 0.25 # the smallest unit is Sixteenth note, 1/4 beat
	start = 0
	for num in text:

		note_number = int(num) + 40
		end = start + unit * sec_beat
		print('start, end', start, end)
		start = end
		note = pretty_midi.Note(
			velocity=100, pitch=note_number, start=start, end=end)
		guitar.notes.append(note)
	
	# Add the cello instrument to the PrettyMIDI object
	guitar_high.instruments.append(guitar)
	# Write out the MIDI data
	guitar_high.write(output_path)


if __name__ == '__main__':
	example = '0044007744774400'
	order = 2
	ngram_chars = gen_possiblities(example, order)
	start_word = '00'
	result = gen_sequence(order, ngram_chars, start_word, 10)
	print(result)
	output_path = 'test_2.mid'
	text_to_midi(result, 60, output_path)


