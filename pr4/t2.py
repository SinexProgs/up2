import sqlite3

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
	cost REAL,
)
""")
cursor.execute("""
CREATE TABLE IF NOT EXISTS cocktails_composition (
	cocktail_id INTEGER,
	drink_id INTEGER,
	volume REAL,
	
	PRIMARY KEY (cocktail_id, drink_id),
	FOREIGN KEY (cocktail_id) REFERENCES cocktails(id) ON DELETE CASCADE,
	FOREIGN KEY (drink_id) REFERENCES drinks(id) ON DELETE CASCADE
)
""")