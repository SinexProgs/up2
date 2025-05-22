import sqlite3

def add_new_ingredient(name, count):
    cursor.execute("INSERT INTO ingredients (name, count) VALUES (?, ?)", (name, count))
    connection.commit()


def add_new_drink(name, abv, cost, ingredients, count):
    cursor.execute("INSERT INTO drinks (name, abv, cost, count) VALUES (?, ?, ?, ?)",
                   (name, abv, cost, count))
    drink_id = cursor.lastrowid

    cursor.executemany("""
    INSERT INTO drinks_ingredients (drink_id, ingredient_id)
    VALUES (?, ?)
    """, ((drink_id, x) for x in ingredients))

    connection.commit()


def add_new_cocktail(name, cost, composition):
    cursor.execute("INSERT INTO cocktails (name, cost) VALUES (?, ?)", (name, cost))
    cocktail_id = cursor.lastrowid

    cursor.executemany("""
    INSERT INTO cocktails_composition (cocktail_id, drink_id)
    VALUES (?, ?)
    """, ((cocktail_id, x) for x in composition))

    connection.commit()


def print_all_ingredients():
    cursor.execute("SELECT * FROM ingredients")
    for values in cursor.fetchall():
        print(f"{values[0]}. {values[1]} (осталось {values[2]})")


def print_all_drinks():
    cursor.execute("SELECT * FROM drinks")
    for values in cursor.fetchall():
        print(f"""{values[0]}. {values[1]} (осталось {values[4]}):
 - Крепость: {values[2]}%
 - Цена: {values[3]}""")


def print_all_cocktails():
    cursor.execute("""
    SELECT c.id, c.name, c.cost, AVG(d.abv) 
    FROM cocktails c
    LEFT JOIN cocktails_composition composition ON c.id = composition.cocktail_id
    LEFT JOIN drinks d ON d.id = composition.drink_id
    GROUP BY c.id
    """)
    for values in cursor.fetchall():
        print(f"""{values[0]}. {values[1]}:
 - Крепость: {values[3]}%
 - Цена: {values[2]}""")


def restock_ingredient(id, count):
    cursor.execute("UPDATE ingredient SET count = count + ? WHERE id = ?", (count, id))
    connection.commit()


def make_drink(id, count):
    cursor.execute("BEGIN")
    try:
        cursor.execute("""
        UPDATE ingredients
        SET count = count - ?
        WHERE id IN (SELECT ingredient_id
                     FROM drinks_ingredients
                     WHERE drink_id = ?)
        """, (count, id))

        cursor.execute("UPDATE drinks SET count = count + ? WHERE id = ?", (count, id))

        cursor.execute("COMMIT")
    except connection.Error:
        print("Не хватает ингредиентов!")
        cursor.execute("ROLLBACK")

    connection.commit()


def sell_drink(id, count, money):
    change = money
    cursor.execute("SELECT cost * ? FROM drinks WHERE id = ?", (count, id))
    change -= cursor.fetchone()
    if change < 0:
        print(f"Для покупки нехватает {-change} рублей!")
        return money
    else:
        cursor.execute("BEGIN")
        try:
            cursor.execute("UPDATE drinks SET count = count - ? WHERE id = ?", (count, id))
            cursor.execute("COMMIT")
        except connection.Error:
            print("Не хватает напитков!")
            cursor.execute("ROLLBACK")
            change = money

        connection.commit()
        return change


def sell_cocktail(id, count, money):
    change = money
    cursor.execute("SELECT cost * ? FROM cocktails WHERE id = ?", (count, id))
    change -= cursor.fetchone()
    if change < 0:
        print(f"Для покупки нехватает {-change} рублей!")
        return money
    else:
        cursor.execute("BEGIN")
        try:
            cursor.execute("""
            UPDATE drinks
            SET count = count - ?
            WHERE id IN (SELECT drink_id
                         FROM cocktails_composition
                         WHERE cocktail_id = ?)
            """, (count, id))

            cursor.execute("UPDATE cocktails SET count = count + ? WHERE id = ?", (count, id))

            cursor.execute("COMMIT")
        except connection.Error:
            print("Не хватает напитков!")
            cursor.execute("ROLLBACK")
            change = money

        connection.commit()
        return change


connection = sqlite3.connect("i_love_drink.db")
connection.isolation_level = None
cursor = connection.cursor()

cursor.execute("PRAGMA foreign_keys = ON")
cursor.execute("""
CREATE TABLE IF NOT EXISTS ingredients (
	id INTEGER PRIMARY KEY AUTOINCREMENT,
	name TEXT,
	count INTEGER CHECK (count >= 0)
)
""")
cursor.execute("""
CREATE TABLE IF NOT EXISTS drinks (
	id INTEGER PRIMARY KEY AUTOINCREMENT,
	name TEXT,
	abv REAL,
	cost REAL,
	count INTEGER CHECK (count >= 0)
)
""")
cursor.execute("""
CREATE TABLE IF NOT EXISTS drinks_ingredients (
	drink_id INTEGER,
	ingredient_id INTEGER,
	
	PRIMARY KEY (drink_id, ingredient_id),
	FOREIGN KEY (drink_id) REFERENCES drinks(id) ON DELETE CASCADE,
	FOREIGN KEY (ingredient_id) REFERENCES ingredients(id) ON DELETE CASCADE
)
""")
cursor.execute("""
CREATE TABLE IF NOT EXISTS cocktails (
	id INTEGER PRIMARY KEY AUTOINCREMENT,
	name TEXT,
	cost REAL
)
""")
cursor.execute("""
CREATE TABLE IF NOT EXISTS cocktails_composition (
	cocktail_id INTEGER,
	drink_id INTEGER,
	
	PRIMARY KEY (cocktail_id, drink_id),
	FOREIGN KEY (cocktail_id) REFERENCES cocktails(id) ON DELETE CASCADE,
	FOREIGN KEY (drink_id) REFERENCES drinks(id) ON DELETE CASCADE
)
""")