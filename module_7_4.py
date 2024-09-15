#------------------Использование %:--------------------
print('В команде Магистра Йоды джедаев: %s !' % '117')

print('Итого сегодня в командах участников: %(team1)s и %(team2)s !' % {'team1': 117, 'team2': 102})
#------------------Использование format():-------------
print('Команда Легион.Сепаратисты решила задач: {} !'.format(300))

print('Легион.Сепаратисты решили задачи за {time} с !'.format(time = 133337))
#------------------Использование f-строк:--------------
score_1 = 301
score_2 = 300
print(f'Команды решили {score_1} и {score_2} задач')

challenge_result = ""
if score_1 > score_2 or score_1 == score_2 and team1_time > team2_time:
     challenge_result = 'Победа команды Магистра Йоды'
elif score_1 < score_2 or score_1 == score_2 and team1_time < team2_time:
     challenge_result = 'Победа команды Легион.Сепаратисты'
else:
    challenge_result = 'Ничья'
print(f'Результат битвы: {challenge_result}')

tasks_total = score_1 + score_2
time_second_team1 = 127277
time_second_team2 = 133337
time_all = time_second_team1 + time_second_team2
time_avg = time_all // tasks_total
print(f'Сегодня было решено {tasks_total} задач, в среднем по {time_avg} секунд на задачу!')

