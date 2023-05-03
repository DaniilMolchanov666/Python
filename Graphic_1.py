import matplotlib.pyplot as plt
import numpy
# График: y = x^2
x = numpy.arange(0.0, 30.0, 1.0)
y = x + x**2

# График: y = 3
x1 = numpy.arange(0.0, 30.0, 1.0)
y1 = [3 for i in x1]

# График: y = ln(x) + x
x2 = numpy.arange(0.0, 30.0, 1.0)
y2 = numpy.log(x2) + x2

# создаем окно для графика
p = plt.figure(figsize=(7,7))
p1 = p.add_subplot()

# задаем интервалы по осям X и Y
p1.set(xlim=(0,15), ylim=(0,15))

# добавляем три графика, задаем цвета, маркеры и легенды
p1.plot(x, y, '-b', marker='*', label='f(x) = x + x^2')
p1.plot(x1, y1, '-m', marker='*', label='f(x) = 3')
p1.plot(x2, y2, '-', color=(0,0,0), marker='*', label='f(x) = ln(x) + x')

# задаем расположение легенды
p1.legend(loc='lower right')

#задаем распределение сетки и ее толщину
p1.grid(which='major', color='black', linewidth=0.5)
p1.grid(which='minor', color='#aaa', linewidth=0.5)

# название графика и осей
plt.title('Графики функций')
plt.xlabel('X')
plt.ylabel('Y')

# постоянное отображение окна
plt.show()



