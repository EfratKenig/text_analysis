# text_analysis

A program that receives a text file as input
And issues a statistical report on it.

design:

analysis() function:
    Opens the file and reads its content.
    analyzes and prints statistics
    Prints their output


main function:
    takes a file name as input from the user,
    handles errors.


Error Handling:
    On file or on input errors: outputs the error and exits.


---------------------------------------------

Libraries:

   NLTK for text analysis.  [https://www.nltk.org/install.html]
    
   webcolors- for color names.
    
   collections for counter


---------------------------------------------


running example:


```C:\Users\This_user\Documents\hadasim\analysis_assignment\venv\Scripts\python.exe C:/Users/This_user/Documents/hadasim/analysis_assignment/text_analysis.py

C:/Users/This_user/Documents/hadasim/analysis_assignment/text_analysis.py

Enter a file path

dickens.txt


---------------------------------------------

number of lines:    527502.

---------------------------------------------

number of words:    5712151.

---------------------------------------------

number of unique words:  45297.

---------------------------------------------

average sentence length:  19.89728021958883 words.

---------------------------------------------

longest sentence length:    356 words, 1989characters.

---------------------------------------------

most popular word:    ('the', 292244).

---------------------------------------------

most popular non grammatical word :    ('mr', 33381).
green 783
black 1778
white 1376
red 1328
brown 386
blue 594
yellow 221
grey 140
purple 34
olive 16
snow 76
navy 13
gray 121
crimson 17
silver 37
ivory 5
tan 6
gold 43
pink 22
lime 15
coral 11
linen 20
plum 5
orange 3
tomato 1
aqua 1
chocolate 1
indigo 4
lavender 2

Process finished with exit code 0

