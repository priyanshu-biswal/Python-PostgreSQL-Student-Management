import psycopg2
from psycopg2 import sql

DB_PARAMS = {
    "dbname": "students_db",
    "user": "postgres",
    "password": "YOUR_PASSWORD",
    "host": "localhost",
    "port": "5432"
}

def get_connection():
    try:
        return psycopg2.connect(**DB_PARAMS)
    except psycopg2.OperationalError as e:
        print(f"\n[ERROR] Could not connect to database 'students_db'. Ensure database exists.\nDetails: {e}")
        return None

def create_table():
    conn = get_connection()
    if not conn:
        return
    
    cursor = conn.cursor()
    create_table_query = """
    CREATE TABLE IF NOT EXISTS students (
        id SERIAL PRIMARY KEY,
        name VARCHAR(100) NOT NULL,
        age INT NOT NULL,
        course VARCHAR(100) NOT NULL
    );
    """
    cursor.execute(create_table_query)
    conn.commit()
    print("\n[SUCCESS] Table 'students' checked/created successfully.")
    
    cursor.close()
    conn.close()

def insert_student_record():
    print("\n--- Insert New Student Record ---")
    name = input("Enter Student Name: ").strip()
    
    try:
        age = int(input("Enter Student Age: "))
    except ValueError:
        print("[ERROR] Invalid age input. Please enter a valid integer.")
        return

    course = input("Enter Course Name: ").strip()

    conn = get_connection()
    if not conn:
        return

    cursor = conn.cursor()
    insert_query = "INSERT INTO students (name, age, course) VALUES (%s, %s, %s);"
    
    cursor.execute(insert_query, (name, age, course))
    conn.commit()
    
    print(f"\n[SUCCESS] Record for '{name}' inserted successfully!")
    cursor.close()
    conn.close()

def fetch_first_record():
    conn = get_connection()
    if not conn:
        return

    cursor = conn.cursor()
    cursor.execute("SELECT * FROM students ORDER BY id ASC;")
    record = cursor.fetchone()

    print("\n--- First Student Record (fetchone) ---")
    if record:
        print(f"ID: {record[0]} | Name: {record[1]} | Age: {record[2]} | Course: {record[3]}")
    else:
        print("No records found in the table.")

    cursor.close()
    conn.close()

def fetch_records_by_course():
    print("\n--- Search Students by Course ---")
    course_name = input("Enter Course Name to Search: ").strip()

    conn = get_connection()
    if not conn:
        return

    cursor = conn.cursor()
    select_query = "SELECT * FROM students WHERE course = %s;"
    cursor.execute(select_query, (course_name,))
    records = cursor.fetchall()

    print(f"\n--- Results for Course: '{course_name}' ---")
    if records:
        for row in records:
            print(f"ID: {row[0]} | Name: {row[1]} | Age: {row[2]} | Course: {row[3]}")
    else:
        print(f"No records found for course '{course_name}'.")

    cursor.close()
    conn.close()

def display_all_records():
    conn = get_connection()
    if not conn:
        return

    cursor = conn.cursor()
    cursor.execute("SELECT * FROM students ORDER BY id ASC;")
    records = cursor.fetchall()

    print("\n--- All Student Records ---")
    if records:
        for row in records:
            print(f"ID: {row[0]} | Name: {row[1]} | Age: {row[2]} | Course: {row[3]}")
    else:
        print("The table is currently empty.")

    cursor.close()
    conn.close()

def truncate_students_table():
    confirm = input("\n[WARNING] Are you sure you want to TRUNCATE the table? (yes/no): ").strip().lower()
    if confirm != 'yes':
        print("Truncate operation cancelled.")
        return

    conn = get_connection()
    if not conn:
        return

    cursor = conn.cursor()
    cursor.execute("TRUNCATE TABLE students RESTART IDENTITY;")
    conn.commit()
    print("\n[SUCCESS] Table 'students' truncated successfully. All data wiped.")

    cursor.close()
    conn.close()

def main_menu():
    create_table()

    while True:
        print("\n" + "="*40)
        print("      POSTGRESQL DATABASE OPERATIONS")
        print("="*40)
        print("1. Insert Student Record (Dynamic Input)")
        print("2. Display First Record (fetchone)")
        print("3. Display All Records")
        print("4. Search Students by Course (WHERE Clause)")
        print("5. Truncate Table")
        print("6. Exit")
        print("="*40)

        choice = input("Enter your choice (1-6): ").strip()

        match choice:
            case '1':
                insert_student_record()
            case '2':
                fetch_first_record()
            case '3':
                display_all_records()
            case '4':
                fetch_records_by_course()
            case '5':
                truncate_students_table()
            case '6':
                print("\nExiting program. Goodbye!")
                break
            case _:
                print("\n[ERROR] Invalid option! Please select a choice between 1 and 6.")

if __name__ == "__main__":
    main_menu()
