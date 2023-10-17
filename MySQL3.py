# #!/usr/bin/python
#
import sqlite3
import hashlib


def add_user(username, password_hash, name, authority):
    temp_conn = sqlite3.connect("user_database.db")
    temp_cursor = temp_conn.cursor()
    password_hash = hashlib.sha256(password_hash.encode()).hexdigest()
    # 插入用户数据
    temp_cursor.execute("INSERT INTO School_User (User_Name, PassWord_Hash, Name, Authority) VALUES (?, ?, ?, ?)",
                   (username, password_hash, name, authority))

    temp_conn.commit()
    temp_conn.close()


