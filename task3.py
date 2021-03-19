from typing import Dict


def appearance(intervals: Dict[str, int]) -> int:
    lessons = intervals['lesson']
    pupil = intervals['pupil']
    tutor = intervals['tutor']
    
    first = tutor # массив первого начавшего
    second = pupil # массив второго начавшего
    result = 0
    first_p = 1 # для массива first (который начался первым)
    first_start_p = 0
    second_p = 0
    start = min(pupil[0], tutor[0])
    result = 0
    min_len = min(len(pupil), len(tutor))
    while first_p <= min_len - 1:
        if first[first_p] > second[second_p] and first[first_p] < second[second_p + 1]: # не полностью пересекаются 
            krappa = first[first_p] - second[second_p]
            result += first[first_p] - second[second_p]
            first_p += 1
            second_p += 1
            continue
        elif first[first_p] > second[second_p] and first[first_p] > second[second_p + 1]: # пересекаются полностью
            result += second[second_p + 1] - second[second_p]
            second_p += 2
            continue
        elif first[first_p] < second[second_p]:
            test = second[second_p] - first[first_p]
            result += test
            first_p += 1
            second_p += 1
            continue
        

intervals = { 
'lesson': [1594692000, 1594695600],
'pupil': [1594692033, 1594696347],
'tutor': [1594692017, 1594692066, 1594692068, 1594696341]
    }

test_data = {

}
print(appearance(intervals))


# Мы сохраняем время присутствия каждого пользователя на уроке в виде интервалов. В функцию передается словарь, содержащий три списка с таймстемпами (время в секундах): 
# — lesson – начало и конец урока 
# — pupil – интервалы присутствия ученика 
# — tutor – интервалы присутствия учителя 
# Интервалы устроены следующим образом – это всегда список из четного количества элементов. Под четными индексами (начиная с 0) время входа на урок, 
# под нечетными - время выхода с урока.
# Нужно написать функцию, которая получает на вход словарь с интервалами и возвращает время общего присутствия ученика и учителя на уроке (в секундах). 
# Будет плюсом: Написать WEB API с единственным endpoint’ом для вызова этой функции.

# время общего присутствия ученика и учителя на уроке в секундах
