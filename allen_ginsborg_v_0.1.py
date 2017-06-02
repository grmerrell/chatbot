import pronouncing
import random

# this is where the users input goes in
content = raw_input("""Allen ginsborg here ready to spit rhymes.  
	What mad lyric should I spit this time?>>>""")

# rhymeSayer function takes user input and pulls off the last part of 
# their line and replaces it with a random rhyming word"
# then prints what they said - the last word + a word that rhymes with the last word
def rhymeSayer(content):
	line = content.rsplit(' ', 1)[0]
	word_to_rhyme = content.rsplit(' ', 1)[-1]
	rhyme_list = pronouncing.rhymes(word_to_rhyme)
	rhyme = random.choice(rhyme_list)
	print line + ' ' + rhyme
	
rhymeSayer(content)


# next, replace the end of a line with a synonym
# then, not and an antonym

from nltk.corpus import wordnet as wn

# test
wn.synsets("small")

store = []
# lemma is different than synonym sets
# this will attach a bunch of synonyms
# to the variable syn in array store
def synonym(syn):
	for synset in wn.synsets(syn):
		for lemma in synset.lemmas():
			store.append(lemma)
	#n = len(store)

syn = 'angry'

#syn = raw_input("thesaurus time biotch!?>>>")

synonym(syn)

elements = []

# then this will break down the lemmatized versions
# of all of these words
# and store the lemmatized synonyms in a list minus their part of speech
# and repetitive index number
for index, element in enumerate(store):
	name = element.name()
	elements.append(name)

print(elements)
	
print("Now we're going to have you enter a line and i'll replace the last \
	word with a similar word that's not the same")

syn = raw_input("bro you want me to switch up your last word?>>>")

line = syn.rsplit(' ', 1)[0]
print (line)

syn = syn.rsplit(' ', 1)[-1]
print(syn)

store = []

def synonym(syn):
	for synset in wn.synsets(syn):
		for lemma in synset.lemmas():
			store.append(lemma)
	#n = len(store)

synonym(syn)

print ("checking stored object")
store

elements = []

for index, element in enumerate(store):
	name = element.name()
	elements.append(name)

stored_elements = []

for element in elements:
	if element != elements[0]:
		stored_elements.append(element)


def thesaurus_biotch(stored_elements):
	rand_thes = random.choice(stored_elements)
	print line + ' ' + rand_thes
	
thesaurus_biotch(stored_elements)


















