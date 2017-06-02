import pronouncing
import random

content = raw_input("""Allen ginsborg here ready to spit rhymes.  
	What mad lyric should I spit this time?>>>""")


def rhymeSayer(content):
	line = content.rsplit(' ', 1)[0]
	word_to_rhyme = content.rsplit(' ', 1)[-1]
	rhyme_list = pronouncing.rhymes(word_to_rhyme)
	rhyme = random.choice(rhyme_list)
	print line + ' ' + rhyme
	
rhymeSayer(content)


