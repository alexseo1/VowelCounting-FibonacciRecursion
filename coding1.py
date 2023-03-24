Counts the number of vowels in a given string.

Parameters:
s (string): lowercase string without spaces, numbers, or special characters.

Returns:
int: number of vowels in s
'''
def vowel_counter(s):
    vowel_count = 0
    vowels = ['a', 'e', 'i', 'o', 'u']
    
    for char in s:
        if char in vowels:
            vowel_count += 1
            
    return vowel_count

'''
Counts the number of vowels in a given string, implementing the sometimes 'y' rule.

Parameters:
s (string): lowercase string without spaces, numbers, or special characters.

Returns:
bool: whether 'y' is in the string or not
int: number of vowels without the 'y' rule
int: number of vowels with the 'y' rule
'''
def sometimes_y(s):
    
    vowels = 0
    vowels_including_y = 0
    y_present = False
    
    words = s.split()
    
    for word in words:
        vowels += vowel_counter(word)
        vowels_including_y += vowel_counter(word)
        
        if word[-1] == 'y':
            vowels_including_y += 1
            y_present = True
            
        for char in word:
            if char == 'y':
                y_present = True
            
            
    return y_present, vowels, vowels_including_y

'''
Counts the number of vowels in each word within a sentence.

Parameters:
sentence (string): a string of words separated by spaces, with punctuation but without numbers. Capital letters are allowed.

Returns:
list: a list containing the number of vowels in each word in the sentence
'''
def sentence_counter(sentence):
    words = sentence.split()
    vowels = []
    
    for word in words:
        word = word.lower().strip(".,!?")
        vowels.append(sometimes_y(word)[2])
   
    return vowels

'''
Returns a code decoder dictionary

Parameters: 
secret_alphabet (string): a 26 letter string of unique characters without spaces.

Returns:
dict: a dictionary mapping from each secret language letter to its english alphabet equivalent.
'''
def create_code(secret_alphabet):
    original = 'abcdefghijklmnopqrstuvwxyz'
    decoder = {}
    
    for i in range(26):
        decoder[secret_alphabet[i]] = original[i]
        
    return decoder

'''
Returns the decoded version of a string using a decoder dictionary

Parameters:
decoder (dict): a dictionary mapping from each secret language letter to its english alphabet equivalent.
encoded_word (str): a string made up only of characters in the secret language.

Returns:
str: the decoded word.
'''
def decode(decoder, encoded_word):
    decoded_word = ''
    
    for char in encoded_word:
        decoded_word += decoder[char]
        
    return decoded_word

'''
Returns an integer that is the nth Fibonacci number.

Parameters:
n (int): The nth Fibonacci number you want.

Returns:
int: the nth fibonacci number.
'''
def recursive_fib(n):
    if n <= 1:
        return n
    
    else:
        return recursive_fib(n-2) + recursive_fib(n-1)
'''
Returns an integer that is the nth Fibonacci number.

Parameters:
n (int): The nth Fibonacci number you want.

Returns:
int: the nth fibonacci number.
'''
def iterative_fib(n):
    if n <= 1:
        return n
    
    else:
        fib_1 = 1
        fib_2 = 0
        
        for i in range(2, n+1):
            fib_n = fib_1 + fib_2
            fib_2 = fib_1
            fib_1 = fib_n

        return fib_n
######################################################################
### DO NOT TURN IN AN ASSIGNMENT WITH ANYTHING BELOW HERE MODIFIED ###
######################################################################
if __name__ == '__main__':
    print("#######################################")
    print("Welcome to Coding 1: Python Introduction!")
    print("#######################################")
    print()

    print("---------------------------------------")
    print("PART A: Vowel Counting")
    print("---------------------------------------")
    
    print("---------------------------------------")
    print("\'vowel_counter\' Tests")
    print("---------------------------------------")
    
    vowel_counter_tests = ['apple', 'cake', 'zzzz', 'aeiou', 'pneumonoultramicroscopicsilicovolcanoconiosis']
    vowel_counter_answers = [2, 2, 0, 5, 20]
    
    for count, test in enumerate(vowel_counter_tests):
        if (vowel_counter(vowel_counter_tests[count]) == vowel_counter_answers[count]):
          passed = 'PASSED!'
        else:
          passed = "FAILED!"
        
        print("Test #{}: {}".format(count + 1, passed))
        print(f'Correct Answer: {vowel_counter_answers[count]}')
        print(f'Your Answer: {vowel_counter(vowel_counter_tests[count])}')
        
        
    print("---------------------------------------")
    print("\'sometimes_y\' Tests")
    print("---------------------------------------")
    
    sometimes_y_tests = ['apple', 'syzygy', 'zzzz', 'aeiouy', 'pneumonoultramicroscopicsilicovolcanoconiosis', 'yellow', 'yesterday', 'y']
    sometimes_y_answers = [(False, 2, 2), (True, 0, 1), (False, 0, 0), (True, 5, 6), (False, 20, 20), (True, 2, 2), (True, 3, 4), (True, 0, 1)]

    for count, test in enumerate(sometimes_y_tests):
        if (sometimes_y(sometimes_y_tests[count]) == sometimes_y_answers[count]):
          passed = 'PASSED!'
        else:
          passed = "FAILED!"
        
        print("Test #{}: {}".format(count + 1, passed))
        print(f'Correct Answer: {sometimes_y_answers[count]}')
        print(f'Your Answer: {sometimes_y(sometimes_y_tests[count])}')
        
    print("---------------------------------------")
    print("\'sentence_counter\' Tests")
    print("---------------------------------------")
    
    sentence_counter_tests = ['The boy, Sam, walked to the store.',
                              'Hello, how are you?',
                              'On a sunny day, the funny, punny bunny ran up the hill.',
                              'I went to office hours, and the TAs were so friendly!!!']

    sentence_counter_answers = [[1, 2, 1, 2, 1, 1, 2],
                                [2, 1, 2, 2],
                                [1, 1, 2, 2, 1, 2, 2, 2, 1, 1, 1, 1],
                                [1, 1, 1, 3, 2, 1, 1, 1, 2, 1, 3]]
    
      
    for count, test in enumerate(sentence_counter_tests):
        if (sentence_counter(sentence_counter_tests[count]) == sentence_counter_answers[count]):
          passed = 'PASSED!'
        else:
          passed = 'FAILED!'
        
        print("Test #{}: {}".format(count + 1, passed))   
        print(f'Correct Answer: {sentence_counter_answers[count]}')
        print(f'Your Answer: {sentence_counter(sentence_counter_tests[count])}')
        
    print("---------------------------------------")
    print("\'create_code\' Tests")
    print("---------------------------------------")
        
    alphabet_1 = 'Hh!@mbM*()QWERTYUIOPASDFGZ'
    decoder_1={'H': 'a', 
              'h':'b',
              '!':'c',
              '@': 'd', 
              'm': 'e', 
              'b': 'f',
              'M': 'g', 
              '*': 'h', 
              '(': 'i',
              ')':'j',
              'Q': 'k', 
              'W': 'l', 
              'E':'m',
              'R': 'n', 
              'T': 'o', 
              'Y':'p', 
              'U': 'q', 
              'I':'r',
              'O': 's', 
              'P':'t',
              'A':'u',
              'S':'v', 
              'D': 'w', 
              'F': 'x', 
              'G': 'y',
              'Z': 'z'}
    
    alphabet_2 = 'Hh!@mbM*()qwertyUIOPAS5FGZ'
    decoder_2={'H': 'a', 
              'h':'b',
              '!':'c',
              '@': 'd', 
              'm': 'e', 
              'b': 'f',
              'M': 'g', 
              '*': 'h', 
              '(': 'i',
              ')':'j',
              'q': 'k', 
              'w': 'l', 
              'e':'m',
              'r': 'n', 
              't': 'o', 
              'y':'p', 
              'U': 'q', 
              'I':'r',
              'O': 's', 
              'P':'t',
              'A':'u',
              'S':'v', 
              '5': 'w', 
              'F': 'x', 
              'G': 'y',
              'Z': 'z'}
    
    create_code_tests = [alphabet_1, alphabet_2]
    create_code_answers = [decoder_1, decoder_2]
    
    for count, test in enumerate(create_code_tests):
        if (create_code(create_code_tests[count]) == create_code_answers[count]):
          passed = "PASSED!"
        else:
          passed = "FAILED!"
          
        print("Test #{}: {}".format(count + 1, passed)) 
        print(f'Correct Answer: {create_code_answers[count]}')
        print(f'Your Answer: {create_code(create_code_tests[count])}')
        
    print("---------------------------------------")
    print("\'decode\' Tests")
    print("---------------------------------------")
    
    decode_tests = [[decoder_1, '@TM'], [decoder_2, '!HP']]
    decode_answers = ['dog', 'cat']
    
    for count, test in enumerate(decode_tests):
        if (decode(decode_tests[count][0], decode_tests[count][1]) == decode_answers[count]):
          passed = 'PASSED!'
        else:
          passed = 'FAILED!'
          
        print("Test #{}: {}".format(count + 1, passed))
        print(f'Correct Answer: {decode_answers[count]}')
        print(f'Your Answer: {decode(decode_tests[count][0], decode_tests[count][1])}')
        print()
      
    print("---------------------------------------")
    print("PART B: Fibonacci")
    print("---------------------------------------")
    tests = [[1, 1], [4, 4], [10, 10]]
    answers = [[1, 1], [3, 3], [55, 55]]
    for count, test in enumerate(tests):
        if(answers[count][0] == recursive_fib(test[0]) and
            answers[count][1] == iterative_fib(test[1])):
            passed = "PASSED!"
        else:
            passed = "FAILED!"

        print("Test #{}: {}".format(count + 1, passed))
        print("Recursive Fibonacci (Correct): ", answers[count][0])
        print("Recursive Fibonacci (Your Answer): ", recursive_fib(test[0]))
        print("Iterative Fibonacci (Correct): ", answers[count][1])
        print("Iterative Fibonacci (Your Answer): ", iterative_fib(test[1]))
        
