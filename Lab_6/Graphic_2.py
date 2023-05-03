import math
import matplotlib
import matplotlib.pyplot as plt
import numpy

# количество интервалов
intervals_count = 20

# создаем 440 рандомынх чисел с 1 с математическим ожиданием = 0
list_of_random_numbers = numpy.random.normal(0, 1, 440)

# создаем равномерное распределение
plt.hist(list_of_random_numbers, intervals_count, density=True, stacked=True, color='#800080')
plt.title('Гистограмма распределения')
plt.grid()
plt.show()