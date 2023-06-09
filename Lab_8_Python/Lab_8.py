import psycopg2

# создаем подключение к базе данных PostgresQL, вводим данные хоста, названия пользователя и БД и пароль
conn = psycopg2.connect(dbname = 'cottonpads', user = 'daniilmolchanov',
                        password = 'microcuts1928', host = 'localhost')

# создаем БД, где id - это автогенерируемое, неповторяющееся число типа BIG INTEGER
# VARCHAR - поле типа String ограниченной длины, timestamp - формат времени, TEXT - поле типа String любой длины
cur = conn.cursor()

# создаем БД languages, в которой будем хранить языки программирования и IT технологии
cur.execute("CREATE TABLE languages (id BIGINT PRIMARY KEY GENERATED ALWAYS AS IDENTITY, Name VARCHAR(50) NOT NULL)")

# создаем БД countries, в которой будем хранить информацию о странах программистов
cur.execute("CREATE TABLE countries (id BIGINT PRIMARY KEY GENERATED ALWAYS AS IDENTITY, "
            "designation VARCHAR(50) NOT NULL)")

# создаем основную БД  Programmers, где будут указаны вторичные ключи на другие БД для соблюдения нормальной
# формы таблицы ( связь one-to-many с таблицами languages и countries)
cur.execute("CREATE TABLE IF NOT EXISTS Programmers "
            "(id BIGINT GENERATED BY DEFAULT AS IDENTITY PRIMARY KEY, "
            "id_language BIGINT REFERENCES languages(id), id_country BIGINT REFERENCES countries(id), "
            "name VARCHAR(255) UNIQUE NOT NULL, gender VARCHAR(10) NOT NULL, date_of_birth TIMESTAMP NOT NULL)")

# создаем БД info about programmers, где будет храниться информация о программистах по вторичным ключам, указывающих
# на суррогатные ключи id программистов
cur.execute("CREATE TABLE Info_About_Programmers (id BIGINT GENERATED BY DEFAULT AS IDENTITY PRIMARY KEY, "
            "id_programmer BIGINT REFERENCES programmers(id), name VARCHAR(255) UNIQUE NOT NULL, info TEXT NOT NULL)")

# сохраняем изменения и закрываем подключение к БД
conn.commit()
cur.close()
conn.close()