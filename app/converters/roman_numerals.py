def encode(number):
    layers = [
        {'one':'I','five':'V','ten':'X'},
        {'one':'X','five':'L','ten':'C'},
        {'one':'C','five':'D','ten':'M'},
        {'one':'M','five':'V','ten':'X'}
      ]
    digits = [int(x) for x in str(number)]
    letters = []
    for index, num in enumerate(reversed(digits)):
        letters.append(get_numerals(num, layers[index]))
      
    letters.reverse()  
    return ''.join(letters)
  
def get_numerals(n, layer):
    if n < 4:
        return n * layer['one']
    elif n == 4:
        return f"{layer['one']}{layer['five']}"
    elif n < 9:
        return f"{layer['five']}{(n-5)*layer['one']}"
    elif n == 9:
        return f"{layer['one']}{layer['ten']}"
    else:
        return layer['ten']
