import psycopg2

## Bu değeri localinde çalışırken kendi passwordün yap. Ama kodu pushlarken 'postgres' olarak bırak.
password = ''

def connect_db():
    conn = psycopg2.connect(
    host="localhost",
    port=5432,
    database="postgres",
    user="postgres",
    password=password)
    return conn

#customers tablosundan tüm müşterilerin adlarını ve ülkelerini getir.

def question_1_query(): 
    connection = connect_db()
    cursor = connection.cursor()
    cursor.execute('SELECT name, country FROM customers;')
    data = cursor.fetchall()
    cursor.close()
    connection.close()
    return data

#orders tablosunda en yüksek tutarlı 5 siparişi listele (tüm sütunlarla birlikte).

def question_2_query():
    connection = connect_db()
    cursor = connection.cursor()
    cursor.execute('SELECT * FROM orders ORDER BY total_amount DESC LIMIT 5;')
    data = cursor.fetchall()
    cursor.close()
    connection.close()
    return data

#products tablosundan fiyatı en düşük 3 ürünü, sadece adları ve fiyatları ile getir.

def question_3_query():
    connection = connect_db()
    cursor = connection.cursor()
    cursor.execute('SELECT name, price FROM products ORDEY BY price ASC LIMIT 3;')
    data = cursor.fetchall()
    cursor.close()
    connection.close()
    return data

#customers tablosundaki en eski kayıtlı 10 müşteriyi signup_date'e göre sırala.

def question_4_query():
    connection = connect_db()
    cursor = connection.cursor()
    cursor.execute('SELECT * FROM customers ORDER BY signup_date ASC LIMIT 10;')
    data = cursor.fetchall()
    cursor.close()
    connection.close()
    return data

#products tablosunda en fazla stoğa sahip ürünü sadece adı ve stock_quantity ile getir.

def question_5_query():
    connection = connect_db()
    cursor = connection.cursor()
    cursor.execute('SELECT product_name, stock_quantity FROM product ORDER BY stock_quantity DESC LIMIT 1;')
    data = cursor.fetchall()
    cursor.close()
    connection.close()
    return data

#orders tablosunda son siparişi (tarihi en güncel olanı) listele.

def question_6_query():
    connection = connect_db()
    cursor = connection.cursor()
    cursor.execute('')
    data = cursor.fetchall()
    cursor.close()
    connection.close()
    return data

#products tablosunda sadece product_name sütununu alfabetik sırada göster.

def question_7_query():
    connection = connect_db()
    cursor = connection.cursor()
    cursor.execute('SELECT * FROM orders ORDER BY order_date DESC LIMIT 1;')
    data = cursor.fetchall()
    cursor.close()
    connection.close()
    return data

#customers tablosundan email sütunu olan ilk 5 müşteriyi customer_id'ye göre sırala.

def question_8_query():
    connection = connect_db()
    cursor = connection.cursor()
    cursor.execute('SELECT * FROM customers WHERE email IS NOT NULL ORDER BY customer_id ASC LIMIT 5;')
    data = cursor.fetchall()
    cursor.close()
    connection.close()
    return data

#orders tablosunda tutarı en düşük 3 siparişi ve bunların order_id'lerini getir.

def question_9_query():
    connection = connect_db()
    cursor = connection.cursor()
    cursor.execute('SELECT order_id, total_amount FROM orders ORDER BY total_amount ASC LIMIT 3;')
    data = cursor.fetchall()
    cursor.close()
    connection.close()
    return data

#customers tablosundan sadece Türkiye'deki (country = 'Turkey') müşterileri alfabetik sırala.

def question_10_query():
    connection = connect_db()
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM customers WHERE country = 'Turkey' ORDER BY customer_name ASC;")
    data = cursor.fetchall()
    cursor.close()
    connection.close()
    return data

   