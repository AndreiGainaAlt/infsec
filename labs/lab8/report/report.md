---
## Front matter
title: "Отчёт по лабораторной работе 8"
author: "Гэинэ Андрей"

## Generic otions
lang: ru-RU
toc-title: "Содержание"

## Bibliography
bibliography: bib/cite.bib
csl: pandoc/csl/gost-r-7-0-5-2008-numeric.csl

## Pdf output format
toc: true # Table of contents
toc-depth: 2
fontsize: 12pt
linestretch: 1.5
papersize: a4
documentclass: scrreprt
## I18n polyglossia
polyglossia-lang:
  name: russian
  options:
	- spelling=modern
	- babelshorthands=true
polyglossia-otherlangs:
  name: english
## I18n babel
babel-lang: russian
babel-otherlangs: english
## Fonts
mainfont: PT Serif
romanfont: PT Serif
sansfont: PT Sans
monofont: PT Mono
mainfontoptions: Ligatures=TeX
romanfontoptions: Ligatures=TeX
sansfontoptions: Ligatures=TeX,Scale=MatchLowercase
monofontoptions: Scale=MatchLowercase,Scale=0.9
## Biblatex
biblatex: true
biblio-style: "gost-numeric"
biblatexoptions:
  - parentracker=true
  - backend=biber
  - hyperref=auto
  - language=auto
  - autolang=other*
  - citestyle=gost-numeric
## Pandoc-crossref LaTeX customization
figureTitle: "Рис."
tableTitle: "Таблица"
listingTitle: "Листинг"
lofTitle: "Список иллюстраций"
lotTitle: "Список таблиц"
lolTitle: "Листинги"
## Misc options
indent: true
header-includes:
  - \usepackage{indentfirst}
  - \usepackage{float} # keep figures where there are in the text
  - \floatplacement{figure}{H} # keep figures where there are in the text
---

# Цель работы

Освоить на практике применение режима однократного гаммирования
на примере кодирования различных исходных текстов одним ключом

# Задание

Два текста кодируются одним ключом (однократное гаммирование).
Требуется не зная ключа и не стремясь его определить, прочитать оба текста. Необходимо разработать приложение, позволяющее шифровать и дешифровать тексты P1 и P2 в режиме однократного гаммирования. Приложение должно определить вид шифротекстов C1 и C2 обоих текстов P1 и
P2 при известном ключе ; Необходимо определить и выразить аналитически способ, при котором злоумышленник может прочитать оба текста, не
зная ключа и не стремясь его определить.

# Выполнение лабораторной работы

Код программы:

#

```
rom random import choice
import string

text1 = "Кирие елейсон"
text2 = "Глобет сист ду Мария"

key_components = [str(i) for i in range(10)] + list(string.ascii_uppercase)

key = ''.join(choice(key_components) for _ in range(len(text1)))

print(f"Key: {key}")

def xor_cypher(key, text):
    result = ""
    for i in range(len(text)):
        result = result + chr(ord(text[i]) ^ ord(key[i % len(key)]))
    return result
```
#
```
c1 = xor_cypher(key, text1)
c2 = xor_cypher(key, text2)

print(f"Text1: {text1}")
print(f"Text2: {text2}")
print(f"Cyphertext1: {c1}")
print(f"Cyphertext2: {c2}")

def get_second_text(c1,c2,text1):
    result = ""
    for i in range(len(text1)):
        result = result + chr(ord(c1[i]) ^ ord(c2[i]) ^ ord(text1[i]))
    return result

restored_text2 = get_second_text(c1,c2,text1)

print(f"Original: {text2}; Recovered: {restored_text2}")
```

# Выводы

Благодаря данной работе я изучил темы:  Элементы
криптографии. Шифрование (кодирование)
различных исходных текстов одним ключом