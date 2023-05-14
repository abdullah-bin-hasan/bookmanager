
from flask import Flask, render_template, request, url_for, flash, redirect
import sqlite3

app = Flask(__name__)


if __name__ == '__main__':
   app.run()


@app.route('/create/', methods=('GET', 'POST'))
def create():
    if request.method == 'POST':
        title = request.form['title']
        publisher = request.form['publisher']
        date_of_publication = request.form['date_of_publication']
        book_type = request.form['book_type']
        pages = request.form['pages']
        if not title:
            flash('Title is required!')
        elif not publisher:
            flash('publihser name is required!')
        elif not date_of_publication:
            flash('Date is required!')
        elif not book_type:
            flash('book type is required!')
        elif not pages:
            flash('Number of pages is required!')
        else:
            conn = get_db_connection()
            conn.execute('INSERT INTO books (title, publisher, date_of_publication, book_type, pages) VALUES (?, ?, ?, ?, ?)',
                         (title, publisher, date_of_publication, book_type, pages))
            conn.commit()
            conn.close()
            return redirect(url_for('index'))

    return render_template('create.html')



def get_db_connection():
    conn = sqlite3.connect('database.db')
    conn.row_factory = sqlite3.Row
    return conn


@app.route('/')
def index():
    conn = get_db_connection()
    books = conn.execute('SELECT * FROM books').fetchall()
    conn.close()
    return render_template('index.html', books=books)

@app.route('/api')
def get_book(book_id):
    conn = get_db_connection()
    book = conn.execute('SELECT * FROM books WHERE id = ?',
                        (book_id)).fetchone()
    conn.close()
    if book is None:
        abort(404)
    return book

@app.route('/api/', methods=('GET', 'POST'))
def api(book_id):
    book_id = request.args.get['book_id']
    if request.method == 'GET':
        conn = get_db_connection()
        book = conn.execute('SELECT * FROM books WHERE id = ?',
                        (book_id)).fetchone()
        conn.close()
        if book is None:
            abort(404)
        return redirect(url_for('index'))
    return render_template('index.html', books = book)
