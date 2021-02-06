import sqlite3 as sql
import requests
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("-t", "--total", dest = "total", type=int, default=50)
args = parser.parse_args()
total_users = args.total

conn = sql.connect('github.db')
print("Database successfully created")

conn.execute('DROP TABLE IF EXISTS users;')
conn.execute('CREATE TABLE users (username TEXT, id INTEGER, image_url TEXT, type TEXT, profile_url TEXT)')
print("Table created successfully")

users = {}
try:
    url = 'https://api.github.com/users'
    params={'per_page': 100, 'page': 1}
    r = requests.get(url, params=params)
    r.raise_for_status()
    users = r.json()
    while 'next' in r.links.keys() and len(users) < total_users:
        r=requests.get(r.links['next']['url'])
        r.raise_for_status()
        users.extend(r.json())
except requests.exceptions.HTTPError as err:
    conn.close()
    raise SystemExit(err)

user_tuples = []
for user in users[:total_users]:
    user_tuple = (user['login'], user['id'], user['avatar_url'], user['type'], user['html_url'] )
    user_tuples.append(user_tuple)

cur = conn.cursor()
cur.executemany("INSERT INTO users VALUES (?, ?, ?, ?, ?)", user_tuples)
conn.commit()

conn.close()

