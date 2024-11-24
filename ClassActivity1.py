 #1. Loops: Even Numbers from a List

def filter_even_numbers(numbers):
    even_numbers = []
    for num in numbers:
        if num % 2 == 0:
            even_numbers.append(num)
    return even_numbers


 #2. Data Types: Student with the Highest Score

def highest_score(student_scores):
    highest_scorer = None
    highest_score = float('-inf')
    for name, score in student_scores.items():
        if score > highest_score:
            highest_score = score
            highest_scorer = name
    return highest_scorer


 # 3. Functions: Reverse String

def reverse_string(s):
    return s[::-1]

# Slicing creates a reversed copy 


 # 4. Loops & Data Types: Prime Numbers

def primes_Nos(n):
    primes = []
    num = 2
    while num <= n:
        is_prime = True
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                is_prime = False
                break
        if is_prime:
            primes.append(num)
        num += 1
    return primes

 # 5. Functions & Data Types: Merge Two Sorted Lists

def merge_lists(list1, list2):
    merged = []
    i, j = 0, 0
    while i < len(list1) and j < len(list2):
        if list1[i] < list2[j]:
            merged.append(list1[i])
            i += 1
        else:
            merged.append(list2[j])
            j += 1
    merged.extend(list1[i:])
    merged.extend(list2[j:])
    return merged

# Logic: Compare elements from both lists one by one, adding the smallest to the merged list.We are using approx merge sort algo.


# 6. Loops: Average Score

def averageScore(student_scores):
    total_score = 0
    for _, score in student_scores:
        total_score += score
    return total_score / len(student_scores) if student_scores else 0


 # 7. Loops & Strings: Count Vowels

def countVowel(s):
    vowels = 'aeiouAEIOU'
    count = 0
    for char in s:
        if char in vowels:
            count += 1
    return count

 # 8. Data Types & Functions: Squares Dictionary

def squaresDict(numbers):
    squares = {}
    for num in numbers:
        squares[num] = num ** 2
    return squares

# 9. Functions & Loops: Longest Word

def longestWord(words):
    longest = ""
    for word in words:
        if len(word) > len(longest):
            longest = word
    return longest


 # 10. Loops & Data Types: Word Frequency

def wordFrequency(s):
    word_counts = {}
    words = s.split()
    for word in words:
        word_counts[word] = word_counts.get(word, 0) + 1
    return word_counts



# TESTING:

print(filter_even_numbers([1, 2, 3, 4, 5, 6]))

scores = {"Alice": 85, "Bob": 90, "Charlie": 87}
highest_score(scores)

wordFrequency("My name is Muttayab")

longestWord("My name is Muttayyab")

squaresDict([1, 2, 3, 4])

countVowel("MOMIN")

students = [("Alice", 85), ("Bob", 90), ("Charlie", 87)]
averageScore(students)

primes_Nos(3)
