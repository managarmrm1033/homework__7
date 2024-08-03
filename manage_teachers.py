import argparse
from models import Base, Student, Group, Teacher, Subject, Grade
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine

DATABASE_URL = "postgresql://postgres:<506e29ff>@localhost/mezyspostgres"
engine = create_engine(DATABASE_URL)
Session = sessionmaker(bind=engine)
session = Session()

def create_teacher(name):
    teacher = Teacher(fullname=name)
    session.add(teacher)
    session.commit()

def list_teachers():
    return session.query(Teacher).all()

def update_teacher(id, name):
    teacher = session.query(Teacher).filter_by(id=id).first()
    teacher.fullname = name
    session.commit()

def remove_teacher(id):
    teacher = session.query(Teacher).filter_by(id=id).first()
    session.delete(teacher)
    session.commit()

parser = argparse.ArgumentParser()
parser.add_argument('--action', '-a', required=True)
parser.add_argument('--model', '-m', required=True)
parser.add_argument('--name', '-n', required=False)
parser.add_argument('--id', type=int, required=False)

args = parser.parse_args()

if args.action == 'create' and args.model == 'Teacher':
    create_teacher(args.name)
elif args.action == 'list' and args.model == 'Teacher':
    for teacher in list_teachers():
        print(teacher.fullname)
elif args.action == 'update' and args.model == 'Teacher':
    update_teacher(args.id, args.name)
elif args.action == 'remove' and args.model == 'Teacher':
    remove_teacher(args.id)