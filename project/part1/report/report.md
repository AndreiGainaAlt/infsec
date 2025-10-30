---
## Front matter
title: "Отчёт по этапу 1 проекта"
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

Целью данной работы является установка и настройка Kali Linux.

# Задание

- Установите дистрибутив Kali Linux в виртуальную машину.

- В качестве среды виртуализации предлагается использовать VirtualBox.

- Сайт Kali Linux: https://www.kali.org/

# Теоретическое введение

Kali Linux — GNU/Linux-LiveCD, возникший как результат слияния WHAX и Auditor Security Collection. Проект создали Мати Ахарони (Mati Aharoni) и Макс Мозер (Max Moser). Предназначен прежде всего для проведения тестов на безопасность. Наследник развивавшегося до 2013 года на базе Knoppix дистрибутива BackTrack.

Популярность Kali Linux выросла после показа в нескольких эпизодах сериала Mr. Robot. Инструменты, показанные в фильме, включают Bluesniff, Bluetooth Scanner (btscanner), John the Ripper, Metasploit Framework, nmap, Shellshock и wget[7][8][9].

# Выполнение лабораторной работы

Скачали образ для VBox с сайта

![Рис.1](image\1.png)  

Импортируем .vbox файл в VBox.

![Рис.2](image\2.png)  

Запускаем Kali

![Рис.3](image\3.png)  

Виртуальная машина готова к работе.

![Рис.4](image\4.png)  

# Выводы

Благодаря данной работе я настроил виртуальную машину с Kali Linux.