from app import create_app, db
from app.models import User

app = create_app()

@app.cli.command("init-db")
def init_db():
    with app.app_context():
        db.create_all()
        admin = User(email='admin@example.com', password='admin123')
        db.session.add(admin)
        db.session.commit()

if __name__ == '__main__':
    app.run(debug=True)