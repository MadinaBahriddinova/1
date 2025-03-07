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

# Task 1.1: Create Roster Database and Table
execute_query('roster.db', """CREATE TABLE IF NOT EXISTS Roster (
    Name TEXT,
    Species TEXT,
    Age INTEGER
)""")

# Task 1.2: Insert Data into Roster
execute_query('roster.db', """INSERT INTO Roster (Name, Species, Age) VALUES
    ('Benjamin Sisko', 'Human', 40),
    ('Jadzia Dax', 'Trill', 300),
    ('Kira Nerys', 'Bajoran', 29)""")

# Task 1.3: Update Name from Jadzia Dax to Ezri Dax
execute_query('roster.db', "UPDATE Roster SET Name = 'Ezri Dax' WHERE Name = 'Jadzia Dax'")

# Task 1.4: Query Bajoran Characters
print("Roster (Bajoran only):", fetch_results('roster.db', "SELECT Name, Age FROM Roster WHERE Species = 'Bajoran'"))

# Task 1.5: Delete Characters Aged Over 100
execute_query('roster.db', "DELETE FROM Roster WHERE Age > 100")

# Task 1.6: Add Rank Column and Update Data
execute_query('roster.db', "ALTER TABLE Roster ADD COLUMN Rank TEXT")
execute_query('roster.db', """UPDATE Roster SET Rank = CASE
    WHEN Name = 'Benjamin Sisko' THEN 'Captain'
    WHEN Name = 'Ezri Dax' THEN 'Lieutenant'
    WHEN Name = 'Kira Nerys' THEN 'Major'
END""")

# Task 1.7: Query Characters Sorted by Age Descending
print("Roster (sorted by age desc):", fetch_results('roster.db', "SELECT * FROM Roster ORDER BY Age DESC"))