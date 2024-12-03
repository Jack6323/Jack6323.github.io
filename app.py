from flask import Flask, render_template, request, redirect, url_for
import sqlite3
from datetime import datetime, timedelta

app = Flask(__name__)

# Connecting to the SQLite database
def get_db_connection():
    conn = sqlite3.connect('notes.db')
    conn.row_factory = sqlite3.Row
    return conn

# Initialise the database and create tables if they don't already exist
def init_db():
    conn = get_db_connection()

    # Create a tasks table with a category column
    conn.execute('''CREATE TABLE IF NOT EXISTS tasks (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        title TEXT NOT NULL,
                        due_date TEXT,
                        category TEXT CHECK(category IN ('Personal', 'Work')) DEFAULT 'Personal'
                    )''')

    # Create a notes table
    conn.execute('''CREATE TABLE IF NOT EXISTS notes (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        note_title TEXT NOT NULL,
                        content TEXT NOT NULL
                    )''')

    conn.commit()
    conn.close()

# Call init_db to ensure the database is created when startup
init_db()

# Home page showing tasks due today and over this week
@app.route('/')
@app.route('/home')
def home():
    today = datetime.now().date()
    next_week = today + timedelta(days=6)

    conn = get_db_connection()
    tasks_today = conn.execute('SELECT * FROM tasks WHERE due_date = ?', (today,)).fetchall()
    tasks_week = conn.execute('SELECT * FROM tasks WHERE due_date BETWEEN ? AND ?', (today, next_week)).fetchall()

    # Organise tasks by day for the upcoming week
    week_tasks = {today + timedelta(days=i): [] for i in range(7)}
    for task in tasks_week:
        task_date = datetime.strptime(task['due_date'], '%Y-%m-%d').date()
        week_tasks[task_date].append(task)

    conn.close()

    return render_template('home.html', tasks_today=tasks_today, week_tasks=week_tasks)

# Calendar page displaying all of the tasks
@app.route('/calendar')
def calendar():
    conn = get_db_connection()
    tasks = conn.execute('SELECT * FROM tasks').fetchall()
    conn.close()

    return render_template('calendar.html', tasks=tasks)

# Tasks page for managing the tasks
@app.route('/tasks', methods=['GET', 'POST'])
def tasks():
    conn = get_db_connection()

    if request.method == 'POST':
        title = request.form['title']
        due_date = request.form['due_date']
        category = request.form['category']
        # Insert the new task with category
        conn.execute('INSERT INTO tasks (title, due_date, category) VALUES (?, ?, ?)', (title, due_date, category))
        conn.commit()

    # Fetch tasks categorised as either Personal or Work
    personal_tasks = conn.execute('SELECT * FROM tasks WHERE category = ?', ('Personal',)).fetchall()
    work_tasks = conn.execute('SELECT * FROM tasks WHERE category = ?', ('Work',)).fetchall()

    conn.close()

    return render_template('tasks.html', personal_tasks=personal_tasks, work_tasks=work_tasks)

# Delete a task by its ID
@app.route('/delete_task/<int:task_id>', methods=['POST'])
def delete_task(task_id):
    conn = get_db_connection()
    conn.execute('DELETE FROM tasks WHERE id = ?', (task_id,))
    conn.commit()
    conn.close()
    return redirect(url_for('tasks'))

# Notes page for managing the notes
@app.route('/notes', methods=['GET', 'POST'])
def notes():
    conn = get_db_connection()

    if request.method == 'POST':
        try:
            note_title = request.form['note_title']
            content = request.form['content']

            if note_title.strip() == "" or content.strip() == "":
                return "Both fields must be filled.", 400

            conn.execute('INSERT INTO notes (note_title, content) VALUES (?, ?)', (note_title, content))
            conn.commit()
            return redirect(url_for('notes'))

        except sqlite3.Error as e:
            print(f"Database error occurred: {e}")
            return "There was an error saving your note.", 500

        except Exception as e:
            print(f"Unexpected error occurred: {e}")
            return "There was an error saving your note.", 500

    notes = conn.execute('SELECT * FROM notes').fetchall()
    conn.close()

    return render_template('notes.html', notes=notes)

# Delete a note by its ID
@app.route('/delete_note/<int:note_id>', methods=['POST'])
def delete_note(note_id):
    conn = get_db_connection()
    conn.execute('DELETE FROM notes WHERE id = ?', (note_id,))
    conn.commit()
    conn.close()
    return redirect(url_for('notes'))

# Run the Flask app
if __name__ == '__main__':
    app.run(debug=True)
