import snowflake.connector
# import os
import sys
# from dotenv import load_dotenv

# load_dotenv()

# # Connection parameters
# account = os.getenv('account')
# user = os.getenv('user')
# password = os.getenv('password')
# warehouse = os.getenv('warehouse')
# database = os.getenv('database')
# schema = os.getenv('schema')

# Connection parameters
account = sys.argv[1]
user = sys.argv[2]
password = sys.argv[3]
warehouse = sys.argv[4]
database = sys.argv[5]
schema = sys.argv[6]

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
with open(sys.argv[7], 'r') as file:
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
