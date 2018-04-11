from django.http import HttpResponse
from django.shortcuts import render
from operator import itemgetter

def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def count(request):
    fulltext = request.GET['fulltext']
    word_list = fulltext.split(' ')
    count = len(word_list)
    
    word = ""
    if count == 1 :
        word = " word"
    else :
        word = " words"
    
    count = str(count) + word

    word_dictionary = {}

    for word in word_list:
        word = word.upper()
        if word in word_dictionary:
            word_dictionary[word] += 1
        else:
            word_dictionary[word] = 1
    
    test = word_dictionary.items()
    word_dictionary = sorted(word_dictionary.items(), key=itemgetter(1), reverse=True)
    
    return render(request, 'count.html', {
        'fulltext': fulltext, 
        'count': count, 
        'word_dictionary': word_dictionary,
        'test': test 
        })