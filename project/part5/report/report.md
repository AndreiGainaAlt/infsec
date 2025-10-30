---
## Front matter
title: "Отчёт по этапу 5 проекта"
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

Целью данной работы является работа с Burp Suite.

# Теоретическое введение

Burp Suite is a proprietary software tool for security assessment and penetration testing of web applications. It was initially developed in 2003-2006 by Dafydd Stuttard to automate his own security testing needs, after realizing the capabilities of automatable web tools like Selenium.

# Выполнение лабораторной работы

Заходим, настраиваем прокси

![](image\1.png)  

#

Настраиваем прокси в браузере

![](image\2.png)  

#

Пытаемся ввести нерпавильный логин и пароль

![](image\4.png)  

#

Intercept is on, поэтому Burp засекает попытку.

![](image\3.png)  

# Выводы

Благодаря данной работе я научился работать с Burp Suite