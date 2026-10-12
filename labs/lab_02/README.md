# Функциональные возможности Python

Лабораторная работа по курсу «Парадигмы и конструкции языков программирования».

| Модуль | Что отрабатывал |
| --- | --- |
| [field.py](lab_python_fp/field.py) | Генератор для извлечения полей словарей |
| [gen_random.py](lab_python_fp/gen_random.py) | Генерация последовательности случайных чисел |
| [unique.py](lab_python_fp/unique.py) | Собственный итератор и обработка повторов |
| [sort.py](lab_python_fp/sort.py) | Сортировка по ключу и использование `lambda` |
| [print_result.py](lab_python_fp/print_result.py) | Декоратор для вывода результата функции |
| [cm_timer.py](lab_python_fp/cm_timer.py) | Контекстные менеджеры для измерения времени |
| [process_data.py](lab_python_fp/process_data.py) | Обработка вакансий из JSON с помощью функций `f1`–`f4` |

Данные для обработки находятся в [data_light.json](data_light.json). В [text.txt](text.txt) сохранён вывод исходного запуска.

## Запуск

Нужен Python 3.10 или новее; используются модули стандартной библиотеки.

Из корня репозитория:

```bash
cd labs/lab_02
python3 -m lab_python_fp.sort
python3 -m lab_python_fp.print_result
python3 -m lab_python_fp.cm_timer
```

## Обработка JSON

В исходном `process_data.py` сохранён абсолютный путь к файлу на моём компьютере. Для запуска из папки `labs/lab_02` на другой машине замените значение `path` на:

```python
path = 'data_light.json'
```

После этого выполните:

```bash
python3 -m lab_python_fp.process_data
```

Функции последовательно формируют список названий вакансий, отбирают программистов и добавляют сведения об опыте Python и случайную зарплату. Модуль `cm_timer` при импорте также запускает демонстрацию таймера с паузой на две секунды.

## Отчёт

[Скачать отчёт в формате Word](Следнев_ДК_ИУ5-33Б_Лаб3-4_ПиКЯП.docx)

[Задание курса](https://github.com/ugapanyuk/BKIT_2022/wiki/lab_python_fp) · [← Все работы](../../README.md)
