def is_palindrom(word: str) -> bool:
    #najpierw usuwam spacje ze stringa
    word = word.replace(' ', '')
    #i zmieniam wszystkie znaki na małe
    word = word.lower()
    #usuwam jeszcze znaki specjane ze stringa
    word = ''.join(filter(str.isalnum, word))
    #teraz porównuję czy słowo wygląda tak samo od lewej do prawej i na odwrót
    return word[::-1] == word
    
words = ['kajak', 'Poto p', 'stachu', 'kobyła, ma. mały! bok?']
for word in words:
    print(is_palindrom(word))