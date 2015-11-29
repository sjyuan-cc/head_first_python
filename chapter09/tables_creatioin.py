import sqlite3


def create_connection(sqlite_db_file=None):
    try:
        return sqlite3.connect(sqlite_db_file)
    except ConnectionError:
        print('sqlite3 db file is invalid :' + str(sqlite_db_file))


def commit_and_close(connection=None):
    if connection is not None:
        connection.commit()
        connection.close()


def create_tables():
    connection = create_connection('test.sqlite3')
    cursor = connection.cursor()
    cursor.execute('DROP TABLE IF EXISTS athlete')
    cursor.execute('''
                CREATE TABLE athlete(
                  id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
                  name TEXT NOT NULL,
                  dob DATE NOT NULL
                )'''
                   )
    cursor.execute('DROP TABLE IF EXISTS timing_data')
    cursor.execute('''
                CREATE TABLE timing_data(
                  id INTEGER PRIMARY KEY AUTOINCREMENT,
                  athlete_id INTEGER NOT NULL,
                  value TEXT NOT NULL,
                  FOREIGN KEY (athlete_id) REFERENCES athlete(id)
                )'''
                   )
    commit_and_close(connection)
