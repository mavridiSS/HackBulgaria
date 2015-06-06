import sqlite3
import re
import hashlib
import smtplib
import uuid
import datetime
from Client import Client
from SMTP_settings import PASSWORD, USERNAME
from settings import MAX_FAILED_LOGIN, TIME_FORMAT, TIME_LIMIT, DATABASE


conn = sqlite3.connect(DATABASE)
cursor = conn.cursor()

# MAKE THE USERNAME UNIQUE !!!!!!!!!!!!!!!!!!
# make new tables for the hash code: id and hash code for id


def create_clients_table():
    create_query = '''create table if not exists
        clients(id INTEGER PRIMARY KEY AUTOINCREMENT,
                username TEXT UNIQUE,
                email TEXT,
                password TEXT,
                balance REAL DEFAULT 0,
                message TEXT,
                code_to_reset TEXT DEFAULT '',
                tan_code TEXT DEFAULT '',
                failed_login_count INTEGER DEFAULT 0,
                locked_until TEXT,
                is_locked INTEGER DEFAULT 0)'''

    cursor.execute(create_query)


def check_if_strong_password(username, password):
    rgx = re.compile(r'\d.*?[A-Z].*?[a-z]')
    if (rgx.match(''.join(sorted(password))) and len(password) > 8 and not re.search(username, password)):
        return True
    else:
        return False


def get_hash(password):
    hash_object = hashlib.sha1(password.encode('utf-8'))
    hex_dig = hash_object.hexdigest()
    return hex_dig


def change_message(new_message, logged_user):
    update_sql = "UPDATE clients SET message =? WHERE id =?"
    cursor.execute(update_sql, (new_message, logged_user.get_id()))
    conn.commit()
    logged_user.set_message(new_message)


def change_pass(new_pass, logged_user):
    if check_if_strong_password(logged_user.get_username(), new_pass):
        update_sql = "UPDATE clients SET password =? WHERE id =?"
        cursor.execute(update_sql, (get_hash(new_pass), logged_user.get_id()))
        conn.commit()
        return True
    else:
        return False


def register(username, password, email):
    if check_if_strong_password(username, password):
        try:
            insert_sql = """INSERT INTO clients(username, password, email)
                            VALUES (?, ?, ?)"""
            cursor.execute(insert_sql, (username, get_hash(password), email))
        except sqlite3.IntegrityError:
            return "{} already exists!"
        else:
            conn.commit()
            return True
    else:
        return False


def login_user(username, password):
        select_query = """SELECT id,username,email,balance,message
                          FROM clients
                          WHERE username=? AND password =? LIMIT 1"""
        cursor.execute(select_query, (username, get_hash(password)))
        user = cursor.fetchone()
        return user


def login(username, password):
    if has_user(username):
        if can_login(username):
            user = login_user(username, password)
            if(user):
                return Client(user[0], user[1], user[2], user[3], user[4])
            else:
                increment_failed_login_count(username)
                return "YOUR USERNAME OR PASSWORD IS WRONG!"
        else:
            return "USER IS LOCKED"
    else:
        return "USER NOT EXISTS"


def update_code_to_reset(code, id):
    update_query = """UPDATE clients SET code_to_reset=? WHERE id=?"""
    cursor.execute(update_query, (code, id))
    conn.commit()


def update_tan_code(code, id):
    update_query = """UPDATE clients SET tan_code=? WHERE id=?"""
    cursor.execute(update_query, (code, id))
    conn.commit()


def check_tan_code(code, username):
    select_query = """SELECT tan_code FROM clients WHERE username=?"""
    cursor.execute(select_query, (username, ))
    check_code = cursor.fetchone()[0]
    return check_code == code


def check_code_to_reset(check_code, username):
    select_query = """SELECT code_to_reset FROM clients WHERE username=?"""
    cursor.execute(select_query, (username, ))
    code = cursor.fetchone()[0]
    return check_code == code


# NEED TO TEST THE FUNCTIONS BELOW!!!!!!


def reset_password(password, username):
    update_query = """UPDATE clients SET password=? WHERE username=?"""
    cursor.execute(update_query, (get_hash(password), username))
    conn.commit()


def send_reset_password(username):
    select_query = """SELECT email,id FROM clients WHERE username=?"""
    cursor.execute(select_query, (username, ))
    row = cursor.fetchone()
    if row is not None:
        toaddrs = row[0]
        user_id = row[1]

    unique_hash = uuid.uuid4().hex

    msg = "This is your unique code - {}".format(unique_hash)

    server = smtplib.SMTP('smtp.gmail.com:587')
    server.starttls()
    server.login(USERNAME, PASSWORD)
    server.sendmail(USERNAME, toaddrs, msg)
    server.quit()

    update_code_to_reset(unique_hash, user_id)


def send_tan_code(username):
    select_query = """SELECT email,id FROM clients WHERE username=?"""
    cursor.execute(select_query, (username, ))
    row = cursor.fetchone()
    if row is not None:
        toaddrs = row[0]
        user_id = row[1]

    tan_code = uuid.uuid4().hex[0:32]

    msg = "This is your TAN code - {}".format(tan_code)

    server = smtplib.SMTP('smtp.gmail.com:587')
    server.starttls()
    server.login(USERNAME, PASSWORD)
    server.sendmail(USERNAME, toaddrs, msg)
    server.quit()

    update_tan_code(tan_code, user_id)


def has_user(username):
    select_query = """SELECT * FROM clients WHERE username=?"""
    cursor.execute(select_query, (username, ))
    row = cursor.fetchone()
    if row is not None:
        return True
    else:
        return False


def is_locked(username):
    query = """SELECT is_locked FROM clients WHERE username=?"""
    cursor.execute(query, (username, ))
    row = cursor.fetchone()
    return row[0] == 1


def increment_failed_login_count(username):
    query = """UPDATE clients
               SET failed_login_count=failed_login_count+1
               WHERE username=?"""
    cursor.execute(query, (username, ))
    conn.commit()


def has_reached_max_failed_login(username):
    query = """SELECT failed_login_count FROM clients WHERE username=?"""
    cursor.execute(query, (username, ))
    row = cursor.fetchone()
    return row[0] == MAX_FAILED_LOGIN


def lock_until():
    time = datetime.datetime.now()
    time_limit = datetime.datetime.strptime(TIME_LIMIT, TIME_FORMAT)
    locked_until = time + datetime.timedelta(hours=time_limit.hour,
                                             minutes=time_limit.minute,
                                             seconds=time_limit.second)
    return '{}:{}:{}'.format(locked_until.hour,
                             locked_until.minute,
                             locked_until.second)


def lock(username):
    query = """UPDATE clients SET is_locked=? WHERE username=?"""
    cursor.execute(query, (1, username))
    update_query = """UPDATE clients SET locked_until=? WHERE username=?"""
    cursor.execute(update_query, (lock_until(), username))
    conn.commit()


def unlock(username):
    query = """UPDATE clients SET is_locked=? WHERE username=?"""
    cursor.execute(query, (0, username))
    query = """UPDATE clients SET failed_login_count=? WHERE username=?"""
    cursor.execute(query, (0, username))
    update_query = """UPDATE clients SET locked_until=? WHERE username=?"""
    cursor.execute(update_query, (None, username))
    conn.commit()


def can_login_after_block(username):
    query = """SELECT locked_until FROM clients WHERE username=?"""
    cursor.execute(query, (username, ))
    row = cursor.fetchone()
    locked_until = datetime.datetime.strptime(row[0], TIME_FORMAT)
    now = datetime.datetime.now()
    return now >= locked_until


def can_login(username):
    if is_locked(username):
        if can_login_after_block(username):
            unlock(username)
            return True
        else:
            return False
    else:
        if has_reached_max_failed_login(username):
            lock(username)
            return False
        else:
            return True

# functions below are tested


def balance(username):
    select_query = """SELECT balance FROM clients WHERE username=?"""
    cursor.execute(select_query, (username, ))
    row = cursor.fetchone()
    return row[0]


def update_balance(balance, username):
    update_query = """UPDATE clients SET balance=? WHERE username=?"""
    cursor.execute(update_query, (balance, username))
    conn.commit()


def deposit(amount, username):
    blnc = balance(username)
    new_balance = amount + blnc
    update_balance(new_balance, username)


def withdraw(amount, username):
    blnc = balance(username)
    if amount > blnc:
        return False
    else:
        new_balance = blnc - amount
        update_balance(new_balance, username)

