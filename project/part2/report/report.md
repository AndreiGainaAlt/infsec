---
## Front matter
title: "Отчёт по этапу 2 проекта"
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

Целью данной работы является установка DVWA

# Задание

Установить на виртуальную машину с Kali Linux DVWA

# Теоретическое введение

Damn Vulnerable Web Application - это веб приложение на PHP/MySQL, которое "чертовски уязвимо". Его главное цель - помочь профессионалам по безопасности протестировать их навыки и инструменты в легальном окружении, помочь веб разработчикам лучше понять процесс безопасности веб приложений и помочь и студентам и учителям в изучении безопасности веб приложений в контролируемом окружении аудитории.

Назначение DVWA - попрактиковаться в некоторых самых распространённых веб уязвимостях, с различными уровнями сложности, с простым прямолинейном интерфейсом. Обратите внимание, что имеются как задокументированные, так и незадокументированные уязвимости в этом программном обеспечении. Это сделано специально. Вам предлагается попробовать и обнаружить так много уязвимостей, как сможете.

# Выполнение лабораторной работы

Заходим на официальную страницу github DVWA.

![Рис.1](image\1.png)  

#

Переходим в раздел Installation, копируем команду и запускаем на виртуальной машине Kali Linux.

![Рис.2](image\2.png)  

#

Происходит установка. После этого DVWA работает на localhost.

![Рис.3](image\3.png)  

# Выводы

Благодаря данной работе я установил DVWA на виртуальную машину Kali Linux.