from collections import defaultdict


class TrieNode:
    def __init__(self):
        self.next = defaultdict(TrieNode)
        self.cnt = 0
        self.isWord = False


class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        node = self.root

        for char in word:
            node = node.next[char]
            node.cnt += 1

        node.isWord = True

    def search(self, word):
        node = self.root
        ans = 0
        depth = 0

        for char in word:
            if char not in node.next.keys():
                break

            node = node.next[char]
            depth += 1

            if node.cnt == 1:
                return depth

            if node.isWord:
                ans = depth

        return ans


def solution(words):
    answer = 0

    trie = Trie()

    for word in words:
        trie.insert(word)

    for word in words:
        answer += trie.search(word)

    return answer
