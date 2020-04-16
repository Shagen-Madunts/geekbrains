"""
Закодируйте любую строку по алгоритму Хаффмана.
"""

import heapq
from collections import Counter, namedtuple


class Node(namedtuple("Node", ["left", "right"])):
    def move(self, cipher, pref):
        self.left.move(cipher, pref + "0")
        self.right.move(cipher, pref + "1")


class Foliage(namedtuple("Foliage", ["char"])):
    def move(self, cipher, pref):
        cipher[self.char] = pref or "0"


def encode(s):
    priority_queue = []
    for ch, freq in Counter(s).items():
        priority_queue.append((freq, len(priority_queue), Foliage(ch)))  # частота символа, счетчик, сам символ
    count = len(priority_queue)
    while len(priority_queue) > 1:  # в цикле будем добавлять узлы дерева, суммируя вес узла (частоты)
        fr1, cnt1, left = heapq.heappop(priority_queue)
        fr2, cnt2, right = heapq.heappop(priority_queue)
        heapq.heappush(priority_queue, (fr1 + fr2, count, Node(left, right)))
        count += 1
    ciphers = {}
    if priority_queue:
        [(freq, cnt, root)] = priority_queue
        root.move(ciphers, "")
    return ciphers


obj = input(f'Введите строку: ')
codes = encode(obj)
print(f'Код строки: {" ".join(codes[ch] for ch in obj)}\nСоответствие: {codes}')
