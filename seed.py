from faker import Faker
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Base, Student, Group, Teacher, Subject, Grade
import random
from datetime import datetime

DATABASE_URL = "postgresql://user:password@localhost/dbname"
engine = create_engine(DATABASE_URL)
Session = sessionmaker(bind=engine)
session = Session()

fake = Faker()

groups = [Group(name=fake.word()) for _ in range(3)]
session.add_all(groups)
session.commit()

teachers = [Teacher(fullname=fake.name()) for _ in range(5)]
session.add_all(teachers)
session.commit()

subjects = [Subject(name=fake.word(), teacher_id=random.choice(teachers).id) for _ in range(8)]
session.add_all(subjects)
session.commit()

students = [Student(fullname=fake.name(), group_id=random.choice(groups).id) for _ in range(50)]
session.add_all(students)
session.commit()

grades = [Grade(student_id=random.choice(students).id, 
                subject_id=random.choice(subjects).id,
                grade=random.uniform(60, 100),
                date_received=datetime.now()) for _ in range(1000)]
session.add_all(grades)
session.commit()
