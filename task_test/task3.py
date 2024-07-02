"""
Задача консенсуса DNA ридов
При чтении DNA последовательностей могут возникать единичные ошибки, выражающиеся в неверной букве в строке.
Для решения данной проблемы требуемое место читается несколько раз, после чего строится консенсус-строка,
в которой на каждом месте будет стоять тот символ, что чаще всего встречался в этом месте суммарно во всех чтениях.
Т.е. для строк
ATTA
ACTA
AGCA
ACAA
консенсус-строка будет ACTA (в первой ячейке чаще всего встречалась A, во второй – C, в третьей – Т, в четвертой – снова А).
Для входного списка из N строк одинаковой длины построить консенсус-строку.
"""

from typing import List


def consensus_string(reads: List[str]):
    """

    :param reads:
    :return: str
    """
    length = len(reads[0])  # берем длину первой строки т.к в задание сказано, что они одинаковы
    consensus_list = []  # результирующий список

    for i in range(length):
        count = {}  # создаем словарь в который будем записывать подсчет
        for read in reads:
            char = read[i]
            if char in count:
                count[char] += 1
            else:
                count[char] = 1
        consensus_char = max(count,
                             key=count.get)  # дополнительный парамтр в max дает возможность найти в словаре макс значение

        consensus_list.append(consensus_char)

    return "".join(consensus_list)


if __name__ == "__main__":
    reads = [
        "ATTA",
        "ACTA",
        "AGCA",
        "ACAA"
    ]

    print(consensus_string(reads))  # Вывод ACTA
