# encoding: UTF-8

import nltk


try:
	nltk.data.find('corpora/stopwords')
except LookupError:
	nltk.download('stopwords')


def get_stopwords_by_language(language):
    try:
    	return nltk.corpus.stopwords.words(language)
    except IOError:
    	return nltk.corpus.stopwords.words('english')
