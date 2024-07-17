#1. Write a function called is_palindrome that takes a string as an argument 
#Returns True if the string is a palindrome and False otherwise. 
#Use a loop and a conditional statement in your function.

def is_palindrome(s):
    left, right = 0, len(s) - 1

    while left < right:
        if s[left] != s[right]:
            return False
        left += 1
        right -= 1
    return True

# Test cases
print(is_palindrome("racecar"))  # True
print(is_palindrome("python"))   # False

#2. Write a class called Rectangle that has two attributes: length and width. 
#The class should have a constructor method that takes two arguments and assigns them to the attributes. 
#The class should also have two methods: area and perimeter, that return the area and perimeter of the rectangle respectively.

class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width
    
    def area(self):
        return self.length * self.width
    
    def perimeter(self):
        return 2 * (self.length + self.width)

# Test case
r = Rectangle(6, 5)
print(r.area())        # 30
print(r.perimeter())   # 22

#3. Write a function called count_words that takes a list of strings as an argument
#Returns a dictionary that maps each word in the list to the number of times it appears.

def count_words(string_list):
    word_count = {}
    
    for word in string_list:
        if word in word_count:
            word_count[word] += 1
        else:
            word_count[word] = 1
            
    return word_count

# Test case
print(count_words(["hello", "world", "goodnight", "moon", "goodnight", "world"]))  
