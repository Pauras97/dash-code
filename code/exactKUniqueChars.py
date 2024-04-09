## AT MOST K CHARACTERS, EASY KEEP COUNT OF DISTINC CHARS
def most_k_chars(s, k):
    if not s:
        return 0
    table = {}
    num, left = 0, 0
    for i in range(len(s)):
        table[s[i]] = table.get(s[i], 0) + 1
        while len(table) > k:
            table[s[left]] -= 1
            if table[s[left]] == 0:
                del table[s[left]]
            left += 1
        ## V-IMP - SINCE WE'RE looking at AT MOST K chars
        ## THIS STEP ADDS NUM OF DIFFERENT SUBSTRINGS WE CAN MAKE FROM 1 to K unique chars
        num += i - left + 1
    return num

#EXACT K IS AT MOST K - AT MOST K-1
def exact_k_chars(s, k):
    return most_k_chars(s, k) - most_k_chars(s, k-1)

# Main function to test the implementation
if __name__ == "__main__":
    s1 = "pqpqs"
    print(f"Answer should be 7: {exact_k_chars(s1, 2)}")
    s2 = "aabab"
    print(f"Answer should be 0: {exact_k_chars(s2, 3)}")
    s3 = "bbacacbccc"
    print(f"Answer should be 0: {exact_k_chars(s3, 2)}")
    print(f"Answer should be 0: {exact_k_chars(s3, 1)}")
