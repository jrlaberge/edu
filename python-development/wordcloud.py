import wordcloud
import numpy as np
from matplotlib import pyplot as plt
from IPython.display import display
import fileupload
import io
import sys

def calculate_frequencies(file_contents):
    # Here is a list of punctuations and uninteresting words you can use to process your text
    punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
    uninteresting_words = ["the", "a", "to", "if", "is", "it", "of", "and", "or", "an", "as", "i", "me", "my", \
    "we", "our", "ours", "you", "your", "yours", "he", "she", "him", "his", "her", "hers", "its", "they", "them", \
    "their", "what", "which", "who", "whom", "this", "that", "am", "are", "was", "were", "be", "been", "being", \
    "have", "has", "had", "do", "does", "did", "but", "at", "by", "with", "from", "here", "when", "where", "how", \
    "all", "any", "both", "each", "few", "more", "some", "such", "no", "nor", "too", "very", "can", "will", "just"]
    
    # initialize a dict
    words = {}
    
    # split file_contents into a list, iterate over it
    for word in file_contents.split():
        
        # if the current iteration isn't present in uninteresting words, then we proceed, otherwise no action taken
        if word not in uninteresting_words:
            for punc in punctuations:
                if punc in word:
                    word = word.replace(punc, '')
            if word not in words:
                words.update({word: 1})
            else:
                words[word] += 1
    
        
    
    #wordcloud
    cloud = wordcloud.WordCloud()
    cloud.generate_from_frequencies(words)
    return cloud.to_array()

# Display your wordcloud image

myimage = calculate_frequencies(file_contents)
plt.imshow(myimage, interpolation = 'nearest')
plt.axis('off')
plt.show()