# put your code here.

file_in = open("test.txt")

def word_count(file_in):
    """This function is meant to that opens a file, 
    and counts how many times each space-separated word occurs in that file
    """
    word_count = {}

    #strips the new line and splits on the spaces
    for line in file_in:
        line = line.rstrip()
        words = line.split(" ")
        
        #loops through words to check if word is key in word_count dictionary
        for word in words:
           
           if word not in word_count:
               word_count[word] =1
           else:
               word_count[word] +=1

    # print word_count dictionary as key, value
    for key, value in word_count.items():
        print key, value

word_count(file_in)