def findWords(words):
    row1="qwertyuiop";
    row2="asdfghjkl";
    row3="zxcvbnm";

    result=[];
    for word in words:
        w_set=set(word.lower());
        if w_set.issubset(row1) or w_set.issubset(row2) or w_set.issubset(row3):
            result.append(word);
    return result;

print(findWords(["Hello","Alaska","Dad","Peace"]))