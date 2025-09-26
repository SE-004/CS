def shortest_completing_word(plate, words):
    def count(i):
        ans =[0] * 26;
        for letter in i:
            ans[ord(letter) - ord("a")] += 1
        return ans;

    def dominates(c1, c2):
        return all(x1 >= x2 for x1, x2 in zip(c1, c2))
    
    ans = None
    target = count(c.lower() for c in plate if c.isalpha())
    for word in words:
        if (ans is None or len(word) < len(ans)) and dominates(count(word.lower()), target):
            ans = word
    
    return ans;

print(shortest_completing_word("1s3 PSt", ["step","steps","stripe","stepple"]))


    