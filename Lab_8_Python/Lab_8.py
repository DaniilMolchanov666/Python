import psycopg2

# создаем подключение к базе данных PostgresQL, вводим данные хоста, названия пользователя и БД и пароль
conn = psycopg2.connect(dbname = 'cottonpads', user = 'daniilmolchanov',
                        password = 'microcuts1928', host = 'localhost')

# создаем БД, где id - это автогенерируемое, неповторяющееся число типа BIG INTEGER
# VARCHAR - поле типа String ограниченной длины, timestamp - формат времени, TEXT - поле типа String любой длины
cur = conn.cursor()
cur.execute("CREATE TABLE IF NOT EXISTS Programmers "
            "(Id BIGINT GENERATED BY DEFAULT AS IDENTITY PRIMARY KEY, "
            "Name VARCHAR(50), Date_of_birth timestamp, Gender VARCHAR(10), Info TEXT)")

# сохраняем изменения и закрываем подключение к БД
conn.commit()
cur.close()
conn.close()