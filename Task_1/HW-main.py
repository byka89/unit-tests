def sort_russia(lis):
    for b in range(len(lis)):
      i = 0
      for visit in lis:
        if "Россия" not in list(visit.values())[0][1]:
          del geo_logs[i]
        i+=1
    return lis

def unic_num(ids):
    new_list = []
    for user in ids:
        new_list.extend(ids[user])
    return list(set(new_list))

def max_value(stats):
    sorted_stats = list(sorted(stats.items(), key=lambda item:item[1],reverse = True))
    high_num = sorted_stats[0][1]
    companies = []
    for el in sorted_stats:
        if el[1] == high_num:
            companies.append(el[0])
    return f"Канал/ы с максимальным объёмом продаж: {', '.join(companies)}"


geo_logs = [
    {'visit1': ['Москва', 'Россия']},
    {'visit2': ['Дели', 'Индия']},
    {'visit3': ['Владимир', 'Россия']},
    {'visit4': ['Лиссабон', 'Португалия']},
    {'visit5': ['Париж', 'Франция']},
    {'visit6': ['Лиссабон', 'Португалия']},
    {'visit7': ['Тула', 'Россия']},
    {'visit8': ['Тула', 'Россия']},
    {'visit9': ['Курск', 'Россия']},
    {'visit10': ['Архангельск', 'Россия']}
]

ids = {'user1': [213, 213, 213, 15, 213],
       'user2': [54, 54, 119, 119, 119],
       'user3': [213, 98, 98, 35]}

stats = {'facebook': 55, 'yandex': 120, 'vk': 115, 'google': 99, 'email': 42, 'ok': 98, 'ivi': 120}
