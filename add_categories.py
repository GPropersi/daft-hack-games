from app import app, db
from model import Users, UserStats, Category
from strings import CATEGORIES, USERS

def add_categories():

  with app.app_context():
    for category_name in CATEGORIES:
      if db.session.execute(db.select(Category).filter_by(name=category_name)).scalar_one_or_none() is not None: continue
      category = Category()
      category.name = category_name 

      db.session.add(category)
      db.session.commit()


if __name__ == "__main__":
  add_categories()