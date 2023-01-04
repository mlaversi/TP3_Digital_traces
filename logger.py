#In this part, we will create a python decorator to monitor the time taken by the execution of a
#function. To test it, we’ll make two implementations of a function that count each word in the
#Shakespear artwork. Please add this python file in your repository so I can see the
#implementations.

import time
from collections import Counter
import numpy as np

def log_execution_time(func):
  def wrapper(a):
    array = []
    for i in range(100) :
        start_time = time.time()
        result = func(a)
        end_time = time.time()
        execution_time = end_time - start_time
        array.append(execution_time)


    average = np.sum(array) / len(array)
    standard = np.std(array) / len(array)
    print(f"The average over 100 iterations: {average}")
    print(f"The average over 100 iterations: {standard}")
    return result
  return wrapper


#1. Count the number of appearances of each word in this text:
@log_execution_time
def count_appearances(text) :
    count = {}
    for word in text.split() :
        if word in count :
            count[word] +=1
        else :
            count[word] = 1
    return count

@log_execution_time
def count_words(text):
    words = text.split()
    word_counts = Counter(words)

    return word_counts


with open('text.txt') as f:
    lines = f.read()
    count_app1= count_appearances(lines) #0.21
    count_app2 = count_words(lines) #0.18069243431091309
    print(count_app2)




