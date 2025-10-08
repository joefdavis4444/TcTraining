import psycopg2

def pull_table_in_postgresql(tname):
    conn = None
    cursor = None
    try:
        # 1. Connect to your PostgreSQL database
        conn = psycopg2.connect(
            dbname="testdb",
            user="admin",
            password="admin123",
            host="localhost",  # Or your PostgreSQL host
            port="5432"      # Or your PostgreSQL port
        )

        # 2. Create a cursor object
        cursor = conn.cursor()

        # 3. Define the CREATE TABLE statement
        pull_table_query = "select * from " + tname + ";"


        # 4. Execute the CREATE TABLE statement
        cursor.execute(pull_table_query)
        records = cursor.fetchall()

        for row in records:
            print(row)

        # 5. Commit the transaction
        conn.commit()
        #print("Table 'joestore' pulled successfully.")

    except psycopg2.Error as e:
        print(f"Error pulling values from table: {e}")
        if conn:
            conn.rollback()  # Rollback in case of error
    finally:
        # 6. Close the cursor and connection
        if cursor:
            cursor.close()
        if conn:
            conn.close()
    print(type(records))
    return records

if __name__ == "__main__":
    pull_table_in_postgresql()


def pull_record_in_postgresql(tname):
    conn = None
    cursor = None
    try:
        # 1. Connect to your PostgreSQL database
        conn = psycopg2.connect(
            dbname="testdb",
            user="admin",
            password="admin123",
            host="localhost",  # Or your PostgreSQL host
            port="5432"      # Or your PostgreSQL port
        )

        # 2. Create a cursor object
        cursor = conn.cursor()

        # 3. Define the CREATE TABLE statement
        pull_table_query = "select * from joestore where items = '" + tname + "';"


        # 4. Execute the CREATE TABLE statement
        cursor.execute(pull_table_query)
        records = cursor.fetchall()
        for row in records:
            print(row)

        # 5. Commit the transaction
        conn.commit()
        #print("Table 'joestore' pulled successfully.")

    except psycopg2.Error as e:
        print(f"Error pulling values from table: {e}")
        if conn:
            conn.rollback()  # Rollback in case of error
    finally:
        # 6. Close the cursor and connection
        if cursor:
            cursor.close()
        if conn:
            conn.close()


def add_record_in_postgresql(tname, q, c):
    conn = None
    cursor = None
    q = str(q)
    c = str(c)
    try:
        # 1. Connect to your PostgreSQL database
        conn = psycopg2.connect(
            dbname="testdb",
            user="admin",
            password="admin123",
            host="localhost",  # Or your PostgreSQL host
            port="5432"      # Or your PostgreSQL port
        )

        # 2. Create a cursor object
        cursor = conn.cursor()

        # 3. Define the adding value statement
        add_value_query = "insert into shoppingcart values ('" + tname + "', " + q + " , " + c + " );"


        # 4. Execute the add value statement
        cursor.execute(add_value_query)



        # 5. Commit the transaction
        conn.commit()
        #print("Table 'joestore' pulled successfully.")

    except psycopg2.Error as e:
        print(f"Error adding values to table: {e}")
        if conn:
            conn.rollback()  # Rollback in case of error
    finally:
        # 6. Close the cursor and connection
        if cursor:
            cursor.close()
        if conn:
            conn.close()



def truncate_table_in_postgresql():
    conn = None
    cursor = None

    try:
        # 1. Connect to your PostgreSQL database
        conn = psycopg2.connect(
            dbname="testdb",
            user="admin",
            password="admin123",
            host="localhost",  # Or your PostgreSQL host
            port="5432"      # Or your PostgreSQL port
        )

        # 2. Create a cursor object
        cursor = conn.cursor()

        # 3. Define the adding value statement
        truncate_table_query = "truncate table shoppingcart;"


        # 4. Execute the add value statement
        cursor.execute(truncate_table_query)



        # 5. Commit the transaction
        conn.commit()
        #print("Table 'joestore' pulled successfully.")

    except psycopg2.Error as e:
        print(f"Error truncating table: {e}")
        if conn:
            conn.rollback()  # Rollback in case of error
    finally:
        # 6. Close the cursor and connection
        if cursor:
            cursor.close()
        if conn:
            conn.close()

def edit_record_in_postgresql(tname, q):
    conn = None
    cursor = None
    q = str(q)

    try:
        # 1. Connect to your PostgreSQL database
        conn = psycopg2.connect(
            dbname="testdb",
            user="admin",
            password="admin123",
            host="localhost",  # Or your PostgreSQL host
            port="5432"      # Or your PostgreSQL port
        )

        # 2. Create a cursor object
        cursor = conn.cursor()

        # 3. Define the adding value statement
        edit_value_query = "update joestore set quantity = " + q + " where items = '" + tname + "';"


        # 4. Execute the add value statement
        cursor.execute(edit_value_query)



        # 5. Commit the transaction
        conn.commit()
        #print("Table 'joestore' pulled successfully.")

    except psycopg2.Error as e:
        print(f"Error adding values to table: {e}")
        if conn:
            conn.rollback()  # Rollback in case of error
    finally:
        # 6. Close the cursor and connection
        if cursor:
            cursor.close()
        if conn:
            conn.close()


