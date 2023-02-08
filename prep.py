# 1 reverse a string


def reverse_string(myString):
    index = len(myString)
    reverse_ = ""
    while index:
        index -= 1
        reverse_ += myString[index]

    return reverse_


# test = reverse_string("josh")
# print(test)

# 2 Number of Vowels and Consonants in a String


def v_c_count(myString):
    vowels = ["a", "e", "i", "o", "u"]
    v_count = 0
    c_count = 0
    for x in myString:
        if x in vowels:
            v_count += 1
        else:
            c_count += 1
    return v_count, c_count


# test = v_c_count("joshoat")
# print(test)

# 3 Print the First Non-Repeated Character in a String


def non_repeated(myString):
    my_h = {}
    for x in myString:
        if x not in my_h:
            my_h[x] = 1
        else:
            my_h[x] -= 1
    print(my_h)
    for v in my_h:
        if my_h[v] == 1:
            return v
    return None


# test = non_repeated("josjhoatstoe")
# print(test)

#  find Out if the Provided String Is a Palindrome


def is_palindrome(my_string):
    new_string = "".join(reversed(my_string))
    print(new_string)
    if my_string == new_string:
        return True
    return False


# test = is_palindrome("tot")
# print(test)

# How Do You Determine Whether the Following Two Strings Are Anagrams of Each Other?


def are_anagrams(string_a, string_b):
    string_a = string_a.replace(" ", "").lower()
    string_b = string_b.replace(" ", "").lower()
    return sorted(string_a) == sorted(string_b)


# test = are_anagrams("tot", "ot")
# print(test)


# How Do You Find Duplicate Numbers in an Array With Multiple Duplicates?


def dup_num(arr):
    my_hash = {}
    dup_list = []

    for x in arr:
        if x not in my_hash:
            my_hash[x] = 0
        else:
            my_hash[x] += 1

    for y in my_hash:
        if my_hash[y] > 0:
            dup_list.append(y)

    return dup_list


# test = dup_num([1, 2, 1, 3, 4, 5, 3, 5, 1, 1, 1, 23, 34, 45, 45, 6, 7, 8, 8, 3, 1, 3, 56, 7, 3, 1, 3, 5, 2])
# print(test)


# How Do You Find the Largest and Smallest Number in an Array of 1–100


def find_m_min():
    arr = list(range(1, 101))
    max_num = max(arr)
    min_num = min(arr)

    return min_num, max_num


# print(find_m_min())


# How Do You Remove Duplicates From an Array in Place?

def rem_dup(arr):
    arr = set(arr)
    arr = list(arr)
    return arr


# print(rem_dup([1,2,1,2,3,4,1]))

# How Do You Find All Pairs in an Array of Integers That Add Up to a Specific Sum?

def find_pairs(arr, target):
    seen = {}
    pairs = []

    for x in arr:
        t = target - x

        if t in seen:
            pairs.append((x, t))
        else:
            seen[x] = True
    print(seen)
    return pairs


# print(find_pairs([1,2,3,4,3,7,2,1,-3,-3,5], 5))


# Create a class


class Dog:
    def __init__(self, name, breed):
        self.name = name
        self.breed = breed

    def bark(self):
        print("Woof")


class Shape:
    def __init__(self, color):
        self.color = color

    def get_color(self):
        return self.color


class Circle(Shape):
    def __init__(self, color, radius):
        super().__init__(color)
        self.radius = radius

    def get_area(self):
        return 3.142 * self.radius ** 2


# circle = Circle("red", 1)
# circle.radius = 2
# print(circle.get_color())
# print(circle.get_area())


# Binary Tree

class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None


class BinaryTree:
    def __init__(self):
        self.root = None

    def insert(self, key):
        self.root = self._insert(self.root, key)

    def _insert(self, node, key):
        if node is None:
            return Node(key)

        if key < node.key:
            node.left = self._insert(node.left, key)

        else:
            node.right = self._insert(node.right, key)

        return node

    def search(self, key):
        self.root = self._search(self.root, key)

    def _search(self, node, key):
        if node is None:
            return False

        if node.key == key:
            return True

        if key < node.key:
            return self._search(node.left, key)

        else:
            return self._search(node.right, key)


# overloading

class Vector:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def __add__(self, other):
        return Vector(self.x + other, self.y + other)

    def __sub__(self, other):
        return Vector(self.x - other, self.y - other)

    def __mul__(self, scalar):
        return Vector(self.x * scalar, self.y * scalar)

# Encapsulating


class Bank:
    def __init__(self, balance = 0):
        self.__balance = balance

    def deposit(self, dep):
        self.__balance += dep
        print("Successfully deposited")

    def withdraw(self, amount):
        if amount > self.__balance:
            print("Insufficient funds")
        else:
            self.__balance = self.__balance - amount
            print("Withdrawal successful")

    def check_balance(self):
        print(self.__balance)


bank = Bank()
bank.deposit(10000)
bank.check_balance()












