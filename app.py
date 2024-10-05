import os
import mysql.connector
from dotenv import load_dotenv
from openai import OpenAI

client = OpenAI()

# Set up the MySQL connection
db = mysql.connector.connect(
    host=os.getenv("DB_HOST"),
    user=os.getenv("DB_USER"),
    password=os.getenv("DB_PASSWORD"),
    database=os.getenv("DB_NAME")
)

# Cursor to interact with the database
cursor = db.cursor()

# Load environment variables from a .env file
load_dotenv()

def get_sql_query_from_gpt(question):
    """Send a question to GPT and get an SQL query."""
    # Getting the general schema of the database to send to GPT
    cursor.execute("SHOW TABLES;")
    tables = cursor.fetchall()

    schema_info = {}
    for (table_name,) in tables:
        cursor.execute(f"SHOW COLUMNS FROM {table_name}")
        columns = cursor.fetchall()
        schema_info[table_name] = [column[0] for column in columns]  # Get only the column names(can't make it TOO easy for GPT)

    # print("Database Schema:", schema_info)

    schema_description = "\n".join(
        [f"Table: {table}\nColumns: {', '.join(columns)}" for table, columns in schema_info.items()]
    )

    response = client.chat.completions.create(
        model="gpt-4",
        messages=[
            {"role": "system", "content": "You are an expert SQL query generator."},
            {"role": "user", "content": f"Here is the schema of the database:\n{schema_description}\n\nNow generate a MySQL query for this question: {question}. Only return the MySQL query in your response."}
        ]
    )

    sql_query = response.choices[0].message.content    
    return sql_query

def execute_sql_query(query):
    """Execute an SQL query and return the result."""
    # Query the database from the GPT response
    try:
        cursor.execute(query)
        results = cursor.fetchall()
        return results
    except mysql.connector.Error as err:
        return str(err)


def get_friendly_response_from_gpt(results):
    """Send the SQL results to GPT to get a friendly response."""
    response = client.chat.completions.create(
        model="gpt-4",
        messages=[
            {"role": "system", "content": "You are an assitant that summarizes SQL query results for the average person."},
            {"role": "user", "content": f"Summarize these SQL query results: {results}"}
        ]
    )
    friendly_response = response.choices[0].message.content
    return friendly_response

def ask_question(question):
    """Main function to ask a question and get a friendly response."""
    # SQL query from GPT
    sql_query = get_sql_query_from_gpt(question)
    print(f"Generated SQL Query: {sql_query}")
    
    # SQL query execution
    results = execute_sql_query(sql_query)
    print(f"Query Results: {results}")
    
    # Friendly Response
    friendly_response = get_friendly_response_from_gpt(results)
    print(f"Friendly Response: {friendly_response}")

if __name__ == "__main__":
    print("Question 1:")
    question = "Show me all the cards in the deck titled 'Python Basics'"
    ask_question(question)

    print("Question 2:")
    question = "Show me all the cards created by the user'123456789012'"
    ask_question(question)
    
    print("Question 3:")
    question = "Show me all the decks created by the user '123456789012'"
    ask_question(question)

    print("Question 4:")
    question = "Show me all the deleted decks"
    ask_question(question)

    print("Question 5:")
    question = "Show me all the cards where both the front and back are null"
    ask_question(question)

    print("Question 6:")
    question = "Show me all the cards where the back is null"
    ask_question(question)
