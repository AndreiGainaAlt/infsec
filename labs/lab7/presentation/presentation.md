---
## Front matter
lang: ru-RU
title: "Презентация по лабораторной работе 7"
author: "Гэинэ Андрей"

## Formatting
toc: false
slide_level: 2
theme: metropolis
header-includes: 
 - \metroset{progressbar=frametitle,sectionpage=progressbar,numbering=fraction}
 - '\makeatletter'
 - '\beamer@ignorenonframefalse'
 - '\makeatother'
aspectratio: 43
section-titles: true
---


# Цель работы

Целью данной работы является изучение темы: Элементы
криптографии. Однократное гаммирование.

# Задание

Нужно подобрать ключ, чтобы получить сообщение «С Новым Годом,
друзья!». Требуется разработать приложение, позволяющее шифровать и
дешифровать данные в режиме однократного гаммирования. 

#

Приложение должно:
1. Определить вид шифротекста при известном ключе и известном открытом тексте.
#
2. Определить ключ, с помощью которого шифротекст может быть преобразован в некоторый фрагмент текста, представляющий собой один из
возможных вариантов прочтения открытого текста

# Выполнение лабораторной работы

Код программы:

#

```
from random import choice
import string


phrase = "С новым годом друзья!"
key_components = [str(i) for i in range(len(phrase))] + list(string.ascii_uppercase)

print(key_components)

key = ""

for i in range(len(phrase)):
    key = key + choice(key_components)
```
#
```
def cypher(key, text):
    _ = ""
    for i in range(len(text)):
        _ = _ + chr(ord(text[i]) ^ ord(key[i]))
    return _

print(f"Phrase: {phrase},\nKey: {key}")
cypher_ = cypher(key, phrase)
print(f"Cypher: {cypher_}")
decoded = cypher(key, cypher_)
print(f"DeCypher: {decoded}")
```

# Выводы

Благодаря данной работе я изучил темы: Элементы
криптографии. Однократное гаммирование.