import pronouncing
import random
import nltk
import os
import re
from nltk.corpus import wordnet as wn

# Add local path to corpus data
dir_path = os.path.dirname(os.path.realpath(__file__))
nltk.data.path.append(dir_path + "/nltk_data/")

#################################################################
# Common functions ##############################################
#################################################################

def rhymeSayer(content):
    """
		Takes user input and pulls off the last part of their line
		and replaces it with a random rhyming word then returns
		what they said - the last word + a word that rhymes with the last word
	"""
    if not content:
        return ''

    content_array = content.rsplit(' ', 1)
    if len(content_array) > 1:
        line = content_array[0]
    else:
        line = ''

    word_to_rhyme = re.sub('[^a-zA-Z]+','', content_array[-1])
    rhyme_list = pronouncing.rhymes(word_to_rhyme)

    if not rhyme_list:
        return ''

    rhyme = random.choice(rhyme_list)
    return line + ' ' + rhyme


def synonym(syn):
    line = syn.rsplit(' ', 1)[0]
    syn = syn.rsplit(' ', 1)[-1]

    print(syn)

    store = []
    for synset in wn.synsets(syn):
        for lemma in synset.lemmas():
            store.append(lemma)
    store

    elements = []

    for index, element in enumerate(store):
        elements.append(element.name())

    stored_elements = []

    for element in elements:
        if element != elements[0]:
            stored_elements.append(element)

    rand_thes = random.choice(stored_elements)
    return line + ' ' + rand_thes


#################################################################
# /Common functions #############################################
#################################################################

#################################################################
# Command line interface ########################################
#################################################################

def main():
    content = raw_input("""Allen ginsborg here ready to spit rhymes.
    	What mad lyric should I spit this time?>>>""")

    content_with_rhymes = rhymeSayer(content)
    print(content_with_rhymes)

    # next, replace the end of a line with a synonym
    # then, not and an antonym

    print("Now we're going to have you enter a line and i'll replace the last \
    	word with a similar word that's not the same")

    syn = raw_input("bro you want me to switch up your last word?>>>")

    synonymized_words = synonym(syn)
    print(synonymized_words)

#################################################################
# /Command line interface #######################################
#################################################################
