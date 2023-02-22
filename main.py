def is_palindrom(word: str) -> bool:
    #najpierw usuwam spacje ze stringa
    word = word.replace(' ', '')
    #i zmieniam wszystkie znaki na małe
    word = word.lower()
    #teraz porównuję czy słowo wygląda tak samo od lewej do prawej i na odwrót
    return word[::-1] == word
    
words = ['kajak', 'Poto p', 'stachu']
for word in words:
    print(is_palindrom(word))