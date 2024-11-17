from models import get_db_connection, init_db

def seed_products():
    init_db()  # Спочатку ініціалізуємо базу даних
    conn = get_db_connection()
    products = [
        ('Diamond', 520, "image href", "description"),
    ]
    
    conn.executemany('INSERT INTO products (name, price, image, description) VALUES (?, ?, ?, ?)', products)
    conn.commit()
    conn.close()

if __name__ == '__main__':
    seed_products()
    print("Тестові продукти додано до бази даних.")