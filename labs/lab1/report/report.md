---
## Front matter
title: "Отчёт по лабораторной работе 1"
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

Целью данной работы является приобретение практических навыков
установки операционной системы на виртуальную машину, настройки минимально необходимых для дальнейшей работы сервисов.

# Задание

Установить на виртуальной машине дистрибутив Rocky Linux, запустить. С помощью dmesg получить информацию о системе.

# Выполнение лабораторной работы

Скачиваем Rocky Linux, конфигурируем в VirtualBox 

![Рис.1](image\1.png)

Запускаем установку

![Рис.2](image\2.png)

Командой dmesg получаем данные о системе

![Рис.3](image\3.png)

1. Версия Линукс 6.12.0
2. Частота 2419.210
3. Модель процессора 11th Gen Intel(R) Core i5-1135G7
4. Обьём доступной памяти 16gb
5. Тип обнаруженного гипервизора KVM
6. Тип корневой файловой системы XFS
7. Последовательность монтирования файловых систем (на рисунке ниже)

![Рис.4](image\4.png)

# Выводы

Установил и настроил Kali Linux.