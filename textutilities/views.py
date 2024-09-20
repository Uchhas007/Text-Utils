# The file was created by Uchhas Saha

# Importing necessary modules
from django.http import HttpResponse # To send the response to the HTTP website 
from django.shortcuts import render # To handle data or file

# Index / Homepage function that'll execute all the codes in the homepage
def index(request): # Takes request argument by default to send a request/query to the web server. Similar to Self
    links = [
        r'<h1> ABOUT <h1> <a href = "/about" > About Me </a>',
        r'<h1> EXAMPLE <h1> <a href = "/ex" > Resources </a>',
    ]
    # Printing command in the homepage
    # return HttpResponse(f'<h1> Hello World! <h1>') # The Homepage should print 'Hello World'
    return HttpResponse((links)) # Should show all the links from the list

def index(request):
    p = {'name' : 'Uchhas Saha', 'place' : 'Mars', 'company': 'Wayne Enterprise'}
    return render(request, 'index.html', p)
    # syntax of render: render(request, 'name_of_template', dictionary(if any))
    # if we pass any dictionary we must say it to out HTML file to show data from dictionary

# the new similar function or method will get replaced with the old one

def analyser(request):
    # accessing data without security
    # txt = request.GET.get('text', 'default') # User input in the form will be stored here
    
    # isPunc = request.GET.get('detectPunctuation', 'off')
    # isCV = request.GET.get('detectVowel', 'off')
    # isCap = request.GET.get('noCap', 'off')
    # isCode = request.GET.get('generateCode', 'off')    
    
    # accessing data from frontend with secured URL
    txt = request.POST.get('text', 'default')
    '''
    will request GET to get the data and store it in the variable
    If any data provided then that data will be stored in 'text' variable which will be later on stored in t variable
    Else if no data provided then default value 'default' will be stored in 'text' variable which will be later on stored in t variable
    '''
    
    '''
    removepunc is the value shown in url after checking or uncheking the chekcbox.
    So we're trying to get the value if removepunc is on or not so that we can analyse the text based on that
    '''

    # isPunc = request.POST.get('detectPunctuation', 'off')
    # isCV = request.POST.get('detectVowel', 'off')
    # isCap = request.POST.get('noCap', 'off')
    # isCode = request.POST.get('generateCode', 'off')

    print(txt) # we can play with the data however we want
    # print(isPunc)
    # print(isCV)
    # print(isCap)
    # print(isCode)

    new_txt = ''
    # case_txt = []
    char_count = 0
    words_count = len(txt.split())
    for i in txt:
        if i != ' ':
            char_count += 1

    punctuations = '''  !"#$%&'()*+, -./:;<=>?@[\]^_`{|}~  '''
    punc_counter = 0
    detected_punc = ''' '''
    vowels = ['a', 'e', 'i', 'o', 'u']
    vowel_counter = 0
    consonant_counter = 0
    vowel = ''
    consonants = ''
    if txt != 'default':
        for j in txt:
            if j in punctuations:
                detected_punc += j
                punc_counter += 1
            if j in vowels:
                vowel += j
                vowel_counter += 1
            if j not in punctuations:
                new_txt += j
            if j not in vowels:
                consonant_counter += 1
                consonants += j

            # elif isCV == 'on':
                # if j in vowels:
                #     vowel += j
                #     vowel_counter += 1
                # else:
                #     consonants += j
                #     consonant_counter += 1
            # elif isCap == 'on':
                # case_txt.append(txt.upper())
                # case_txt.append(txt.lower())
                # case_txt.append(txt.capitalize())
            # elif isCode == 'on':
                # return HttpResponse('Feature Not available at this moment!')
    else:
        return render(request, 'error.html')
    params = {'inital_text': txt,
              'final_text' : new_txt,
              'total_char' : char_count,
              'total_word' : words_count,
              'punctuations' : detected_punc,
              'total_punc' : punc_counter,
              'vowels' : vowel,
              'total_vowel': vowel_counter,
              'total_consonants' : consonant_counter,
              'consonants': consonants
              }
    return render(request, 'analyser.html', params)

# def ex(request): 
    # sites = ['''For Entertainment visit: <a href = "https://www.youtube.com" > YOUTUBE </a>''',
    #          r'<h1>For Interaction </h1> <a href = "https://www.facebook.com" > FACEBOOK </a>',
    #          r'<h1>For Insight   </h1> <a href = "https://www.ted.com/talks" > TED TALK </a>',
    #          r'<h1>For Internship   </h1> <a href="https://internshala.com" > Intenship </a>'
    #          ]
    # return render (request, 'basic.html')
    # return HttpResponse((sites))

def about(request):
    ab = "Hello everyone. My name is Uchhas Saha. The website is developed by me.\nIt's a pretty basic website. This is actually my very first website.\nI made it just for fun & motivation. Motivation for something amazing!!!\nBellow are my contacts via socials. Thank You!!!"
    d = {'self':ab}
    return render(request, 'about.html', d)