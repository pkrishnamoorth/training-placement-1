
#1.

def find_gcd(a, b):
    while b:
        a, b = b, a % b
    return a

a, b = map(int, input("Enter two integers separated by space: ").split())

print("GCD is:", find_gcd(a, b))

#2.

def fibonacci_sequence(n):
    if n <= 0:
        return []
    elif n == 1:
        return [0]
    elif n == 2:
        return [0, 1]
    
    sequence = [0, 1]
    for i in range(2, n):
        sequence.append(sequence[-1] + sequence[-2])
    return sequence

n = int(input("Enter the number of terms: "))

print("Fibonacci sequence:", fibonacci_sequence(n))

#3.

list1 = list(map(int, input("Enter elements of the first list separated by space: ").split()))
list2 = list(map(int, input("Enter elements of the second list separated by space: ").split()))

intersection = list(set(list1) & set(list2))

print("Intersection:", intersection)

#4.

nums = list(map(int, input("Enter integers separated by space: ").split()))

frequency = {}
for num in nums:
    if num in frequency:
        frequency[num] += 1
    else:
        frequency[num] = 1

print("Frequency of elements:", frequency)

#5.

def unique_substrings(s, k):
    if k > len(s):
        return []
    
    substrings = set()
    for i in range(len(s) - k + 1):
        substrings.add(s[i:i+k])
    return list(substrings)

s = input("Enter a string: ")
k = int(input("Enter the length of substrings (k): "))

result = unique_substrings(s, k)
print("Unique substrings of length", k, ":", result)

#6.

def find_longest_word(sentence):
    words = sentence.split()  
    longest_word = max(words, key=len)  
    return longest_word, len(longest_word)

sentence = input("Enter a sentence: ")

word, length = find_longest_word(sentence)
print("Longest word:", word)
print("Length:", length)

