import re
from Final_CS2420 import LinkedListSet
import Node

def read_words(file_path):
    with open(file_path, 'r') as file:
        txt = file.read()
        #lowercase split
        words = txt.lower().split()
        #filter words
        words = [word for word in words if word.isalpha()]
    return words

#create a, b, c sets
def make_sets(words):
    set_a = LinkedListSet()
    set_b = LinkedListSet()
    set_c = LinkedListSet()

    for word in words:
        if len(word) <= 5:
            set_a.add(word)
        if len(word) >= 5:
            set_b.add(word)
        if len(word) == 5:
            set_c.add(word)

    return set_a, set_b, set_c

#print word sizes
def print_sizes(set_a, set_b, set_c):
    print(f"Size of Set A: {len(set_a)}")
    print(f"Size of Set B: {len(set_b)}")
    print(f"Size of Set C: {len(set_c)}")

#perform 12 operations
def print_sets(set_a, set_b, set_c):

    #union (A union B, B union C, B union C)
    print(f"Size of A union B: {len(set_a.union(set_b))}")
    print(f"Size of A union C: {len(set_a.union(set_c))}")
    print(f"Size of B union C: {len(set_b.union(set_c))}")

    #intersection (a b, a c, b c)
    print(f"Size of A intersect B: {len(set_a.intersect(set_b))}")
    print(f"Size of A intersect C: {len(set_a.intersect(set_c))}")
    print(f"Size of B intersect C: {len(set_b.intersect(set_c))}")

    #difference (a-b, b-a, a-c, c-a, b-c, c-b)
    print(f"Size of A - B: {len(set_a.difference(set_b))}")
    print(f"Size of B - A: {len(set_b.difference(set_a))}")
    print(f"Size of A - C: {len(set_a.difference(set_c))}")
    print(f"Size of C - A: {len(set_c.difference(set_a))}")
    print(f"Size of B - C: {len(set_b.difference(set_c))}")
    print(f"Size of C - B: {len(set_c.difference(set_b))}")

def main():
    file_path = "Partial_Book.txt"
    words = read_words(file_path)
    set_a, set_b, set_c = make_sets(words)
    print_sizes(set_a, set_b, set_c)
    print_sets(set_a, set_b, set_c)

if __name__ == "__main__":
    main()
