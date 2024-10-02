import pyodbc

# Connection string for Windows Authentication
connection_string = (
    "Driver={ODBC Driver 17 for SQL Server};"
    "Server=localhost;"
    "Database=LH;"
    "Trusted_Connection=yes;"
)

try:
    # Create connection
    conn = pyodbc.connect(connection_string)
    print("Connection successful!")

    # Test the connection by executing a simple query
    cursor = conn.cursor()
    cursor.execute("SELECT @@version;")
    row = cursor.fetchone()

    # Print SQL Server version
    if row:
        print("SQL Server version:", row[0])

    # Close the connection
    cursor.close()
    conn.close()

except pyodbc.Error as e:
    print("Error while connecting to SQL Server", e)
