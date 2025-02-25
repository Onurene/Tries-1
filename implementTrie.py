# Time Complexity : Insert:O(L),Search:O(L),startswith:O(L)
# Space Complexity : Insert:O(L),Search:O(1),startswith:O(1)
# Did this code successfully run on Leetcode : Yes
# Any problem you faced while coding this : No

class TrieNode:
    def __init__(self):
        self.children = [None for i in range(26)]
        self.isEnd = False
class Trie:
    
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = TrieNode()
        return       

    def insert(self, word: str) -> None:
        """
        Inserts a word into the trie.
        """
        curr = self.root
        for i in range(len(word)):
            c = word[i]
            if curr.children[ord(c) - ord('a')] is None:
                curr.children[ord(c)-ord('a')] = TrieNode() 
            curr = curr.children[ord(c)-ord('a')]

        curr.isEnd = True

        

    def search(self, word: str) -> bool:
        """
        Returns if the word is in the trie.
        """
        curr = self.root
        for i in range(len(word)):

            c = word[i]
            if curr.children[ord(c)-ord('a')] is None:
                return False
            curr = curr.children[ord(c) -ord('a')]

        return curr.isEnd                             

       

    def startsWith(self, prefix: str) -> bool:
        """
        Returns if there is any word in the trie that starts with the given prefix.
        """
        curr = self.root
        for i in range(len(prefix)):

            c = prefix[i]
            if curr.children[ord(c)- ord('a')] is None:
                return False

            curr = curr.children[ord(c) - ord('a')]

        return True     


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)