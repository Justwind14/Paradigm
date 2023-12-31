import pandas as pd
import numpy as np

# Задача
# Написать скрипт в любой парадигме, который выводит на экран таблицу умножения всех чисел от 1 до n.
# Обоснуйте выбор парадигм.

# запрашиваем число n для входных данных
n = int(input('введите число, которое будет являться пределом выводимой таблицы умножения всех чисел: '))

# вывод таблицы умножения в консоль
for i in range(1, n+1):
    for j in range(1, n+1):
        print(f"{i} * {j} = {i*j}")

# была выбрана структурная парадигма, так как данный код не имеет необходимости множественного повторонго использования.
# для процедурного больше бы подошел код, где мы бы брали два числа и через выдов функции получали результат их умножения.
# также здесь нечего разбивать на части.

# процедурный подход никак бы нам не помог перевести вывод таблицы умножение в другом внешнем виде как в примере ниже
print('')
print('')
data = np.arange(1, n + 1)
df = pd.DataFrame(data, columns=['x*1'])
df.index = np.arange(1, n + 1)
for i in range(1, n + 1):
    df[f'x*{i}'] = df['x*1'] * i
print(df.rename_axis('x').sort_index(axis=1))

# под такой код нужно было бы уже создавать совсем иной метод