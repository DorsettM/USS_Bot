import random

def insults():
    
    #load in insults form a file
    insults = open('/home/INSULTS.txt', 'r').readlines()
    
    #Choose Random line from text file and return it
    index = random.randint(0 , len(insults))
    text = insults[index]

    return text

    
