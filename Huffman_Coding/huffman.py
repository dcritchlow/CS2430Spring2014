#!/usr/bin/python
from __future__ import division
from itertools import groupby
from heapq import heapify, heappop, heappush

# Frequencies from pg 771 #27
frequencies = [('A', 0.0817), ('B', 0.0145), ('C', 0.0248),
               ('D', 0.0431), ('E', 0.1232), ('F', 0.0209),
               ('G', 0.0182), ('H', 0.0668), ('I', 0.0689),
               ('J', 0.0010), ('K', 0.0080), ('L', 0.0397),
               ('M', 0.0277), ('N', 0.0662), ('O', 0.0781),
               ('P', 0.0156), ('Q', 0.0009), ('R', 0.0572),
               ('S', 0.0628), ('T', 0.0905), ('U', 0.0304),
               ('V', 0.0102), ('W', 0.0264), ('X', 0.0015),
               ('Y', 0.0211), ('Z', 0.0005)]

class Node(object): #[1]
    """
    Tree nodes are simple objects, but they need to keep track of four
    things: Which item they store (if any), the combined weight of them
    and their children, and their left and right child nodes.
    """
    left = None
    right = None
    item = None
    weight = 0

    def __init__(self, i, w):
        self.item = i
        self.weight = w

    def setChildren(self, ln, rn):
        self.left = ln
        self.right = rn

    def __repr__(self):
        """Print out the status of the nodes to debug the tree"""
        return "%s - %s -- %s _ %s"\
            % (self.item, self.weight, self.left, self.right)

    def __cmp__(self, a):
        """Use the heapq module to order the nodes"""
        return cmp(self.weight, a.weight)

def huffman(input): #[1]
    """Use the groupby function of the itertools module to calculate the
    original weights, then use a heapq priority queue to rank the nodes"""
    itemqueue =  [Node(a,len(list(b))) for a,b in groupby(sorted(input))]
    heapify(itemqueue)
    """At the end of this step, itemqueue has only one element,
    the root node of the tree."""
    while len(itemqueue) > 1:
        l = heappop(itemqueue)
        r = heappop(itemqueue)
        n = Node(None, r.weight+l.weight)
        n.setChildren(l,r)
        heappush(itemqueue, n)

    codes = {}

    def code_it(s, node):
        """
        Walk through the tree to work out the encoding for each item.
        Traverse the whole tree in one go and store the results in a
        dictionary
        """
        if node.item:
            if not s:
                codes[node.item] = "0"
            else:
                codes[node.item] = s
        else:
            code_it(s+"0", node.left)
            code_it(s+"1", node.right)

    # Recursive function to accumulate the encoding as we walk down
    # the tree and branch at each non-leaf node
    code_it("",itemqueue[0])

    return codes, "".join([codes[a] for a in input])

def my_huffman(mylist, input):
    """
    Take the frequencies of letters in typical English text and build a
    Huffman code
    """
    itemqueue = [Node(a,b) for a,b in sorted(frequencies,
        key=lambda frequencies: frequencies[1])]

    while len(itemqueue) > 1:
        l = heappop(itemqueue)
        r = heappop(itemqueue)
        n = Node(None, r.weight+l.weight)
        n.setChildren(l,r)
        heappush(itemqueue, n)

    codes = {}

    def code_it(s, node):
        """
        Walk through the tree to work out the encoding for each item.
        Traverse the whole tree in one go and store the results in a
        dictionary
        """
        if node.item:
            if not s:
                codes[node.item] = "0"
            else:
                codes[node.item] = s
        else:
            code_it(s+"0", node.left)
            code_it(s+"1", node.right)

    # Recursive function to accumulate the encoding as we walk down
    # the tree and branch at each non-leaf node
    code_it("",itemqueue[0])

    return codes
def huffman_text(codes, data):
    huff_text = []
    counter = 0
    counter_alpha = 0
    for i in data.upper():
        if i.isalpha():
            huff_text.append(huff_2.get(i))
            counter_alpha += len(huff_2.get(i))
        else:
            counter += 1
            huff_text.append(i)
    return "".join(huff_text), counter, counter_alpha

if __name__ == "__main__":
    print 'Build a Huffman code based upon the frequency of characters',
    print 'in the Metamorphosis.txt file','\n'
    with open('Metamorphosis.bin', 'rb') as f:
        data = f.read()
    huff = huffman(data)
    with open('huffman.bin', 'wb')as f2:
        f2.write(huff[1])
    with open('huffman.bin', 'rb')as f3:
        myfile = f3.read()
    original_byte_length = len(data) * 8
    myfile_byte_length = len(myfile)
    percent = myfile_byte_length / original_byte_length

    print 'myfile\n>> %d bytes' %(myfile_byte_length),\
        '\nOriginal file\n>> %d bytes' %(original_byte_length),\
        '\nCompression of %.2f%%' %(100 - round(percent * 100, 2))

    print

    huff_2 = my_huffman(frequencies, data.upper())
    english_huff = huffman_text(huff_2, data)
    with open('huffman2.bin', 'wb')as f2:
        f2.write(english_huff[0])
    second_file_byte_length = (english_huff[1] * 8) + english_huff[2]
    percent = second_file_byte_length / original_byte_length
    print 'second file\n>> %d bytes' %(second_file_byte_length),\
        '\nOriginal file\n>> %d bytes' %(original_byte_length),\
        '\nCompression of %.2f%%' %(100 - round(percent * 100, 2))

