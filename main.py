def is_palindrom(word: str) -> bool:
    word = word.replace(' ', '')
    word = word.lower()

    return word[::-1] == word
    
words = ['kajak', 'Poto p', 'stachu']
for word in words:
    print(is_palindrom(word))