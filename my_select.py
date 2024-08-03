from sqlalchemy import func, desc
from models import Student, Grade
from sqlalchemy.orm import sessionmaker

DATABASE_URL = "postgresql://user:password@localhost/dbname"
engine = create_engine(DATABASE_URL)
Session = sessionmaker(bind=engine)
session = Session()

def select_1():
    return session.query(Student.fullname, func.round(func.avg(Grade.grade), 2).label('avg_grade'))\
        .select_from(Grade).join(Student).group_by(Student.id).order_by(desc('avg_grade')).limit(5).all()

print(select_1())
