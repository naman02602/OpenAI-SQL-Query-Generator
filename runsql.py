import snowflake.connector
import sys
import os

# Connection parameters
account = os.environ.get("SNOWSQL_ACCOUNT")
user = os.environ.get("SNOWSQL_USER")
password = os.environ.get("SNOWSQL_PWD")
warehouse = os.environ.get("SNOWSQL_WAREHOUSE")
database = os.environ.get("SNOWSQL_DATABASE")
schema = os.environ.get("SCHEMA_NAME")

# print(sys.argv)
# account = sys.argv[1]
# user = sys.argv[2]
# password = sys.argv[3]
# warehouse = sys.argv[4]
# database = sys.argv[5]
# schema = sys.argv[6]

# Establish a connection
conn = snowflake.connector.connect(
    user=user,
    password=password,
    account=account,
    warehouse=warehouse,
    database=database,
    schema=schema
)
# Create a cursor object
cursor = conn.cursor()

# Read SQL script from file
with open(sys.argv[1], 'r') as file:
    sql_script = file.read()

# Split the script into individual statements
statements = sql_script.split(';')

# Execute each statement
for statement in statements:
    try:
        cursor.execute(statement)
    except snowflake.connector.errors.ProgrammingError as e:
        print(f"Error executing statement: {statement}")
        print(f"Error details: {e}")

# Commit changes
conn.commit()

# Close cursor and connection
cursor.close()
conn.close()
