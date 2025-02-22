from main import app, db

def create_db():

  import model
  with app.app_context():
    db.create_all()

if __name__ == "__main__":
  create_db()