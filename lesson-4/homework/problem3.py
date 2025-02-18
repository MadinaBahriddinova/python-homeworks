def add_underscore(txt):
    result = []
    count = 0

    for i in range(len(txt)):
        result.append(txt[i])
        
        if txt[i] in 'aeiou' or (i > 0 and txt[i-1] == '_'):
            continue
        
        count += 1
        if count == 3 and i != len(txt) - 1:
            result.append('_')
            count = 0
            
    return ''.join(result)

print(add_underscore("hello"))  
print(add_underscore("assalom"))  
print(add_underscore("abcabcdabcdeabcdefabcdefg"))  
