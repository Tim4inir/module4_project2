def palindromeword(word):
    l = []
    for i in word[::-1]:
       l.append(i)
    if l == list(word):
        print('True')
    else:
        print("False")
        
palindromeword('такси')

