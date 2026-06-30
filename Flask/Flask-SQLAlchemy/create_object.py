from app import db, app, Reader, Book, Review

with app.app_context():
    b1 = Book(id=123, title='Demian', author_name='Hermann', author_surname='Hesse')
    b2 = Book(id=533, title='The Stranger', author_name='Albert', author_surname='Camus')
    r1 = Reader(id=342, name='Ann', surname='Adams', email='ann.adams@example.com')
    r2 = Reader(id=312, name='Sam', surname='Adams', email='sam.adams@example.com')

    rev1 = Review(id=435, text='This book is amazing...', stars=5, reviewer_id=r1.id, book_id=b1.id)
    rev2 = Review(id=450, text='This book is difficult!', stars=2, reviewer_id=r2.id, book_id=b2.id)

    # Save everything into the database
    db.session.add_all([b1, b2, r1, r2, rev1, rev2])
    db.session.commit()

    print("Objects committed successfully!")
    
print(Book.query.all())
print(Reader.query.all())
print(Review.query.all())

