from app import app, db
from model import Users, UserStats, Category
from strings import CATEGORIES, USERS

def add_users():
  with app.app_context():
    for new_user in USERS:
      if db.session.execute(db.select(Users).filter_by(username=new_user)).scalar_one_or_none() is not None: continue
      user = Users()
      user.username = new_user

      db.session.add(user)
      db.session.commit()


if __name__ == "__main__":
  add_users()