# В большой текстовой строке подсчитать количество встречаемых слов и вернуть 10 
# самых частых. Не учитывать знаки препинания и регистр символов.
# За основу возьмите любую статью из википедии или из документации к языку.

import re
from collections import Counter

def count_words(text):

    text = text.lower()
    
    text = re.sub(r'[^\w\s]', '', text)

    words = text.split()

    word_count = Counter(words)

    top_10_words = word_count.most_common(10)
    
    return top_10_words

# Пример использования функции на тексте статьи из Википедии
article_text = '''
Python is an interpreted, high-level, general-purpose programming language. Created by Guido van Rossum and first released in 1991, 
Python's design philosophy emphasizes code readability with its notable use of significant whitespace. Its language constructs and 
object-oriented approach aim to help programmers write clear, logical code for small and large-scale projects.

Python is dynamically typed and garbage-collected. It supports multiple programming paradigms, including procedural, object-oriented, 
and functional programming. Python is often described as a "batteries included" language due to its comprehensive standard library.

Python interpreters are available for many operating systems. CPython, the reference implementation of Python, is open source software 
and has a community-based development model, as do nearly all of Python's other implementations. Python and CPython are managed by 
the non-profit Python Software Foundation.

Python was conceived in the late 1980s as a successor to the ABC language. Python 2.0, released in 2000, introduced features like 
list comprehensions and a garbage collection system capable of collecting reference cycles. Python 3.0, released in 2008, was a 
major revision of the language that is not completely backward-compatible, and much Python 2 code does not run unmodified on Python 3.
'''

most_common_words = count_words(article_text)
print(most_common_words)
