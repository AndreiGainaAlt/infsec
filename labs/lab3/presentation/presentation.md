---
## Front matter
lang: ru-RU
title: "Презентация по лабораторной работе 3"
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

Получение практических навыков работы в консоли с атрибутами файлов для групп пользователей

# Задание

Научиться разграничивать доступ по группам в системах типа Linux, заполнить таблицы о доступе групп.

# Выполнение лабораторной работы

Добавляем пользователя, редактируем пароль

![Рис.1](image\1.png)

#

Добавляем ещё пользователя, добавляем его в группу guest

![Рис.2](image\2.png)

#

Заходим обоими пользователями в разных консолях, уточняем информацию о них

![Рис.3](image\3.png)

#

Смотрим содержимое /etc/group

![Рис.4](image\4.png)

#

От имени guest2 регистрируемся в группе guest

![Рис.5](image\5.png)

#

От имени guest меняем права директории /home/guest

![Рис.6](image\6.png)

#

От имени guest снимаем все права директории /home/guest/dir1, проверяем аттрибуты

![Рис.6](image\6_1.png)

#

Таблицы:

#

![Рис.7](image\7.png)

#

![Рис.8](image\8.png)

#

![Рис.9](image\9.png)

#

![Рис.10](image\10.png)

#

![Рис.11](image\11.png)

# Выводы

Полученил практические навыки работы в консоли с атрибутами файлов