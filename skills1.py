# Things you should be able to do.

# Write a function that takes a list and returns a new list with only the odd numbers.
def all_odd(some_list):
    odd_list = []
    for i in some_list:
        if i % 2 != 0:
            odd_list.append(i)
    return odd_list   

# Write a function that takes a list and returns a new list with only the even numbers.
def all_even(some_list):
    even_list = []
    for i in some_list:
        if i % 2 == 0:
            even_list.append(i)
    return even_list 

# Write a function that takes a list of strings and a new list with all strings of length 4 or greater.
def long_words(word_list):
    long_words_list = []
    for i in word_list:
        if len(i) >= 4:
            long_words_list.append(i)
    return long_words_list

# Write a function that finds the smallest element in a list of integers and returns it.
def smallest(some_list):
    smallest = some_list[0]
    for i in range(len(some_list)-1):
        if some_list[i+1] < some_list[i]:
            smallest = some_list[i+1]
    return smallest

# Write a function that finds the largest element in a list of integers and returns it.
def largest(some_list):
    largest = some_list[0]
    for i in range(len(some_list)-1):
        if some_list[i+1] > some_list[i]:
            largest = some_list[i+1]
    return largest

# Write a function that takes a list of numbers and returns a new list of all those numbers divided by two.
def halvesies(some_list):
    halved_list = []
    for i in some_list:
        halved_list.append(float(i)/2)
    return halved_list

# Write a function that takes a list of words and returns a list of all the lengths of those words.
def word_lengths(word_list):
    length_list = []
    for i in word_list:
        length_list.append(len(i))
    return length_list

# Write a function (using iteration) that sums all the numbers in a list.
def sum_numbers(numbers):
    numbers_sum = 0
    for i in numbers:
        numbers_sum += i
    return numbers_sum

# Write a function that multiplies all the numbers in a list together.
def mult_numbers(numbers):
    product = 1
    for i in numbers:
        product *= i
    return product

# Write a function that joins all the strings in a list together (without using the join method) and returns a single string.
def join_strings(string_list):
    joined_string = ''
    for i in string_list:
        joined_string += i
    return joined_string

# Write a function that takes a list of integers and returns the average (without using the avg method)
def average(numbers):
    avg = sum(numbers) / len(numbers)
    return avg

def main():
    test_list = [2,0,6,3,7,8,34,2,9,77]
    smaller_list = [2, 5, 3, 10]
    string_list = ['bubblegum','farfel','gargantuan','feet','alto','should','hat','foolish','at','bit']
    print "All odd: ", all_odd(test_list)
    print "All even: ", all_even(test_list)
    print "Long word list: ", long_words(string_list)
    print "Smallest: ", smallest(test_list)
    print "Largest: ", largest(test_list)
    print "Halved list: ", halvesies(test_list)
    print "Lengths of words: ", word_lengths(string_list)
    print "Sum of numbers: ", sum_numbers(test_list)
    print "Product of numbers: ", mult_numbers(smaller_list)
    print "Joined list: ", join_strings(string_list)
    print "Average: ", average(smaller_list)

main()