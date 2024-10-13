# start

str_func1: str = " fun-day "
print(str_func1.strip())

str_func2: str = 'hello'
print(str_func2.isalpha())

str_func3: str = '777'
print(str_func3.isdigit())

str_func4: str = '    '
print(str_func4.isspace())

print(['N', 'I', 'N', 'J', 'A'])
print(''.join(['N', 'I', 'N', 'J', 'A']))
print(''.join(['N''*', 'I', '*', 'N', '*', 'J', '*', 'A']))

str_func5: str = 'hELLo'
print('e is in the list?', 'e' in str_func5.lower())

# Bonus:
number: list[int] = []
sentence: str = input('enter a sentence with letters and numbers:')
list_char: list[str] = [char for char in sentence if char not in [sentence.lower(), sentence != [number]]]
print(list_char)

# stop
