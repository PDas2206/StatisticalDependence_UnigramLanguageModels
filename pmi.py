# -*- coding: utf-8 -*-
"""
STATISTICAL DEPENDENCE

"""
import nltk
import string
import random
from nltk.book import *
from nltk.tokenize import word_tokenize
from collections import Counter
from nltk.collocations import *



choice=input("Do you want to test the independence assumption with or without punctuation in the text?\n Press 0 for without punctuation OR 1 for with punctuation: ")

# This section creates a tokenized list from the text, punctuation inclusive
if int(choice)==1:
    token_list=[]
    for line in text2:
        tokens=line.split()
        token_list.extend(tokens)

# This section creates a tokenized list from the text, punctuation removed       
if int(choice)==0:
    token_list=[]
    for line in text2:
        tokens=line.split()
        stripped_tokens = [word for word in tokens if word.isalpha()]
        token_list.extend(stripped_tokens)
    
# This section removes the tokens from the list that occur less than 10 times in the text
counts=Counter(token_list)
updated_list={key:val for key, val in counts.items() if val >= 10}
final_list=[*updated_list]

"""   
This section calculates the pmi for word pairs in the text (without infrequent words)
and also displays 20 pairs with the best and worst pmi values
"""
bigram_measures = nltk.collocations.BigramAssocMeasures()
finder_1 = BigramCollocationFinder.from_words(final_list)
scored_1 = finder_1.score_ngrams(bigram_measures.pmi)
print("--------------------------------------------------------------------")
print("PMI scores for word pairs in text after removing infrequent words")
print("--------------------------------------------------------------------")
print("20 word pairs with the highest pmi value:")
print(scored_1[:20]) 
print("20 word pairs with the lowest pmi value:")
print(scored_1[-20:]) 
print()
"""   
This section calculates the pmi for word pairs in the text (as a whole text,
including infrequent words) and also displays 20 pairs with the best and worst pmi values
"""

finder_2 = BigramCollocationFinder.from_words(token_list)
scored_2 = finder_2.score_ngrams(bigram_measures.pmi)
print("--------------------------------------------------------------------")
print("PMI scores for word pairs in text without removing infrequent words")
print("--------------------------------------------------------------------")
print("20 word pairs with the highest pmi value:")
print(scored_2[:20]) 
print("20 word pairs with the lowest pmi value:")
print(scored_2[-20:]) 