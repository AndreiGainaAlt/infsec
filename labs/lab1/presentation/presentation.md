---
## Front matter
lang: ru-RU
title: "Презентация по лабораторной работе 1"
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

Целью данной работы является приобретение практических навыков
установки операционной системы на виртуальную машину, настройки минимально необходимых для дальнейшей работы сервисов.

# Задание

Установить на виртуальной машине дистрибутив Rocky Linux, запустить. С помощью dmesg получить информацию о системе.

# Выполнение лабораторной работы

Скачиваем Rocky Linux, конфигурируем в VirtualBox 

![Рис.1](image\1.png)

#

Запускаем установку

![Рис.2](image\2.png)

#

Командой dmesg получаем данные о системе

![Рис.3](image\3.png)

#

1. Версия Линукс 6.12.0
2. Частота 2419.210
3. Модель процессора 11th Gen Intel(R) Core i5-1135G7
4. Обьём доступной памяти 16gb
5. Тип обнаруженного гипервизора KVM
6. Тип корневой файловой системы XFS
7. Последовательность монтирования файловых систем (на рисунке ниже)

#

![Рис.4](image\4.png)

# Выводы

Установил и настроил Kali Linux.
