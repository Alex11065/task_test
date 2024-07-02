"""
Считалочка
Дано N человек, считалка из K слогов. Считалка начинает считать с первого человека. Когда считалка досчитывает до k-го слога,
человек, на котором она остановилась, вылетает. Игра происходит до тех пор, пока не останется последний человек.
Для данных N и К дать номер последнего оставшегося человека.
"""
from time import sleep


def counting_rhyme(N, K):
    list_people = [i for i in range(1, N + 1)]  # список людей
    # print(list_people)
    people_index = 0  # Начинаем с первого человека

    while len(list_people) > 1:
        people_index = (people_index + K - 1) % len(list_people)  # Находим индекс человека, который вылетает
        print(f"Вылетает {list_people[people_index]}")
        list_people.pop(people_index)  # Удаляем из списка человека
        sleep(0.5)

    return f"Победитель {list_people[0]}"  # номер последнего оставшегося человека


if __name__ == "__main__":
    N = 3
    K = 4
    print(counting_rhyme(N, K))


