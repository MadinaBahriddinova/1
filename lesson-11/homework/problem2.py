import sqlite3

def execute_query(database, query, params=()):
    """Executes a single query on the given database."""
    conn = sqlite3.connect(database)
    cursor = conn.cursor()
    cursor.execute(query, params)
    conn.commit()
    conn.close()

def fetch_results(database, query, params=()):
    """Fetches and returns results from a database based on the given query."""
    conn = sqlite3.connect(database)
    cursor = conn.cursor()
    cursor.execute(query, params)
    results = cursor.fetchall()
    conn.close()
    return results

# Task 2.1: Create Library Database and Table
execute_query('library.db', """CREATE TABLE IF NOT EXISTS Books (
    Title TEXT,
    Author TEXT,
    Year_Published INTEGER,
    Genre TEXT
)""")

# Task 2.2: Insert Data into Books Table
execute_query('library.db', """INSERT INTO Books (Title, Author, Year_Published, Genre) VALUES
    ('To Kill a Mockingbird', 'Harper Lee', 1960, 'Fiction'),
    ('1984', 'George Orwell', 1949, 'Dystopian'),
    ('The Great Gatsby', 'F. Scott Fitzgerald', 1925, 'Classic')""")

# Task 2.3: Update Year Published for 1984
execute_query('library.db', "UPDATE Books SET Year_Published = 1950 WHERE Title = '1984'")

# Task 2.4: Query Dystopian Books
print("Dystopian Books:", fetch_results('library.db', "SELECT Title, Author FROM Books WHERE Genre = 'Dystopian'"))

# Task 2.5: Delete Books Published Before 1950
execute_query('library.db', "DELETE FROM Books WHERE Year_Published < 1950")

# Task 2.6: Add Rating Column and Update Data
execute_query('library.db', "ALTER TABLE Books ADD COLUMN Rating REAL")
execute_query('library.db', """UPDATE Books SET Rating = CASE
    WHEN Title = 'To Kill a Mockingbird' THEN 4.8
    WHEN Title = '1984' THEN 4.7
    WHEN Title = 'The Great Gatsby' THEN 4.5
END""")

# Task 2.7: Query Books Sorted by Year Published Ascending
print("Books (sorted by year asc):", fetch_results('library.db', "SELECT * FROM Books ORDER BY Year_Published ASC"))
