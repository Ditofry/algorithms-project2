#LastName:
#FirstName:
#Email:
#Comments:
from __future__ import print_function
import sys

# We will use a class called my trie node
class MyTrieNode:
    # Initialize some fields
    def __init__(self, isRootNode):
        #The initialization below is just a suggestion.
        #Change it as you will.
        # But do not change the signature of the constructor.
        # TODO: could have a RILL clean recursion if we add pointer to parent
        self.isRoot = isRootNode
        self.isWordEnd = False # is this node a word ending node
        self.isRoot = False # is this a root node
        self.count = 0 # frequency count
        self.next = {} # Dictionary mapping each character from a-z to the child node

    # OK, so we obviously need the nodes to link to one another in a directed format,
    # but we don't HAVE to have a node 'VALUE', (although that might be a better approach)
    # We can avoid having a value attribute trivially in addWord since we're just adding
    # characters until we reach the end of our string, but we'll have to do just a little
    # more work in lookupWord as well as in autoComplete, as we'll have to 'remember'
    # which characters we've collected so far.
    def addWord(self,w):
        wordLength = len(w)
        assert(wordLength > 0)

        n = self
        if wordLength is 1:
            n.isWordEnd = True
            n.count += 1

        if w[0] not in self.next:
            self.next[w[0]] = n

        i = 0
        while i < wordLength:
            # TODO: better to do 2-part loop?
            if w[i] in n.next:
                n = n.next[w[i]]
            else:
                child = MyTrieNode(False)
                n.next[w[i]] = child
                n = child
            i += 1
        n.isWordEnd = True
        n.count += 1

    # Return frequency of occurrence of the word w in the trie
    # returns a number for the frequency and 0 if the word w does not occur.
    def lookupWord(self,w):
        wordLength = len(w)
        n = self
        i = 0
        while i < wordLength:
            # If letter is in next dictionary then follow to that key's node
            if w[i] in n.next:
                n = n.next[w[i]]
            else:
                return 0
            i += 1
        # If we've gone through our loop then we're done
        return n.count

    def autoComplete(self,w):
        #Returns possible list of autocompletions of the word w
        #Returns a list of pairs (s,j) denoting that
        #         word s occurs with frequency j

        #YOUR CODE HERE
        # traverse tree until we get to our starting point
        wordLength = len(w)
        n = self
        i = 0
        while i < wordLength:
            if w[i] in n.next:
                n = n.next[w[i]]
            else:
                return 0
            i += 1
        # If we've gone through our loop then we have our starting point
        # now we traverse and look for all 'isWordEnd' and their count
        results = []

        # Time was running short so I went with a recursion that had a trillion
        # arguments since it was the easiest way to traverse something that's
        # arbitrary-ish in shape
        self.searchWords(w, n, "", results)
        return results

    def searchWords(self, prefix, n, chars, results):
        print(prefix + chars)
        if n.isWordEnd:
            word = prefix + chars
            results.append((word, n.count))
            print(results)

        # print(n.next)
        for char in n.next:
            print("in for")
            newChars = chars + char
            # print("Char is {0} and prefix is {1} and node is ".format(char, prefix), n.next[char])
            self.searchWords(prefix, n.next[char], newChars, results)


if (__name__ == '__main__'):
    t= MyTrieNode(True)
    lst1=['test','testament','testing','ping','pin','pink','pine','pint','testing','pinetree']

    for w in lst1:
        t.addWord(w)

    j = t.lookupWord('testy') # should return 0
    j2 = t.lookupWord('telltale') # should return 0
    j3 = t.lookupWord ('testing') # should return 2
    print("{0} should be 0".format(j))
    print("{0} should be 0".format(j2))
    print("{0} should be 2".format(j3))

    lst3 = t.autoComplete('pi')
    print('Completions for \"pi\" are : ')
    print(lst3)

    lst4 = t.autoComplete('tes')
    print('Completions for \"tes\" are : ')
    print(lst4)
