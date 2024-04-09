# TIME AND SPACE O(N*L) n = num words, l = avg len of word
class Trie:
    def __init__(self):
        self.children = defaultdict(Trie)
        self.word = None
        self.end = False
    
    def insert(self, word):
        curr = self
        for char in word:
            curr = curr.children[char]
        curr.word = word
        curr.end = True
    
    def searchPrefix(self, prefix):
        curr = self
        for ch in prefix:
            curr = curr.children[ch]
        return curr
    
    def getKSearchWords(self, curr, k):
        result = []
        if curr.end:
            result.append(curr.word)
        if len(result) >= k:
            return result[:k]
        
        for child in sorted(curr.children):
            result.extend(self.getKSearchWords(curr.children[child], k - len(result)))
            if len(result) >= k:
                break
        return result
        
class Solution:
    def __init__(self):
        self.root = Trie()
        
        #optional
        self.cache = {}
        
    def suggestedProducts(self, products: List[str], searchWord: str, k: int) -> List[List[str]]:        
        for product in products:
            self.root.insert(product)
        
        # Check cache first // optional 
        if searchWord in self.cache:
            return self.cache[searchWord]
        
        prefixNode = self.root.searchPrefix(searchWord)
        if not prefixNode:
            return []
        
        return self.root.getKSearchWords(prefixNode, k)        
        

products = ["mobile","mouse","moneypot","monitor","mousepad", "map"]
searchWord = "mo"

products = [
    "apple", "applet", "applesauce", "application", "appreciate", 
    "banana", "bandana", "banish", "banner", "bandwidth",
    "candle", "candy", "canopy", "candid", "canvas",
    "delta", "delve", "deliver", "demand", "demure",
    "echo", "eclipse", "ecology", "economy", "eclectic",
    # Adding more for a common prefix "appl"
    "applaud", "applepie", "appliance", "applicant", "applied", 
    "apply", "appraise", "approach", "approval", "approximate",
    # Unique and rare prefixes
    "xylophone", "xenon", "zebra", "zenith", 
    # Long list of similar prefixes
    "microscope", "microservice", "microwave", "microcosm", "microchip", "microfilm",
    "microphone", "microbial", "microeconomics", "microorganism"
]
searchTerms = ["app", "micro", "x", "qu", "application", ""]

solution = Solution()

for k in range(1, 5):
    for prefix in searchTerms:
        print(f'\n pref = {prefix}; k = {k}')
        print(solution.suggestedProducts(products, prefix, k))

# def printTrie(self, level=0, key=''):
#     # Print the current key (character) and any words at this node
#     indent = '  ' * level
#     print(f"{indent}Key: '{key}', Words: {self.word}")

#     # Recursively print children
#     for k, child in self.children.items():
#         child.printTrie(level + 1, k)