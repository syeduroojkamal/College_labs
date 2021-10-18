import textwrap
sample_text = '''
enter the string[[]]
enter the wordpython
[[python]]
enter string : github.com
{'g': 1, 'i': 1, 't': 1, 'h': 1, 'u': 1, 'b': 1, '.': 1, 'c': 1, 'o': 1, 'm': 1}
Enter first string : abcd
Enter second string : abcde
as C++ or Java.
'''
print(sample_text)
text_without_Indentation = textwrap.dedent(sample_text)
print()
print(text_without_Indentation )
print()
