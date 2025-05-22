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
    SELECT cocktails.id, cocktails.name, cocktails.cost, AVG(drinks.abv) 
    FROM cocktails
    LEFT JOIN cocktails_composition composition ON cocktails.id = composition.cocktail_id
    LEFT JOIN drinks ON drinks.id = composition.drink_id
    """)
    for values in cursor.fetchall():
        print(f"""{values[0]}. {values[1]}:
 - Крепость: {values[3]}%
 - Цена: {values[2]}""")


connection = sqlite3.connect("i_love_drink.db")
cursor = connection.cursor()

cursor.execute("PRAGMA foreign_keys = ON")
cursor.execute("""
CREATE TABLE IF NOT EXISTS ingredients (
	id INTEGER PRIMARY KEY AUTOINCREMENT,
	name TEXT,
	count INTEGER
)
""")
cursor.execute("""
CREATE TABLE IF NOT EXISTS drinks (
	id INTEGER PRIMARY KEY AUTOINCREMENT,
	name TEXT,
	abv REAL,
	cost REAL,
	count INTEGER
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