# meta = open('amt.png', 'rb')
# print meta.mode
# print meta.name
# print meta.encoding
# data = meta.read()
# print data
# print type(data)
# print meta.tell()
# print len(data)
# bina = open('Metamorphosis.bin', 'wb')
# print bina.encoding
# data1 = bina.read()
# print type(data1)
# bina.write(''.join(format(ord(x), 'b') for x in data1))

# import binascii
# with open('Metamorphosis.txt', 'rb') as f:
#     data = f.read()
# # print data
# data_bin = bin(int(binascii.hexlify(data),16))
# # print data_bin
# # n = int(data_bin, 2)
# # data_txt = binascii.unhexlify('%x' %n)
# # print data_txt

# with open('Metamorphosis_original_copy.txt', 'rb') as f2:
#     data = f2.read()
# print data

# with open('Metamorphosis.bin', 'wb') as f3:
#     f3.write(data)

with open('Metamorphosis.bin', 'rb') as f:
    data = f.read()


from heapq import heappush, heappop, heapify
from collections import defaultdict

def encode(symb2freq):
    """Huffman encode the given dict mapping symbols to weights"""
    heap = [[wt, [sym, ""]] for sym, wt in symb2freq.items()]
    heapify(heap)
    while len(heap) > 1:
        lo = heappop(heap)
        hi = heappop(heap)
        for pair in lo[1:]:
            pair[1] = '0' + pair[1]
        for pair in hi[1:]:
            pair[1] = '1' + pair[1]
        heappush(heap, [lo[0] + hi[0]] + lo[1:] + hi[1:])
    # print sorted(heappop(heap)[1:], key=lambda p: (len(p[-1]), p))
    return sorted(heappop(heap)[1:], key=lambda p: (len(p[-1]), p))

# txt = "this is an example for huffman encoding"
symb2freq = defaultdict(int)
for ch in data:
    symb2freq[ch] += 1
# print "Symbol\tWeight\tHuffman Code"
huff = encode(symb2freq)
# for p in huff:
#     print "%s\t%s\t%s" % (p[0], symb2freq[p[0]], p[1])

# with open("huffman_values.txt", 'wb') as f4:
#     f4.write(str(huff))
