from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Date
from sqlalchemy.orm import sessionmaker
from datetime import datetime, timedelta

Base = declarative_base()


class Task(Base):

    __tablename__ = 'task'
    id = Column(Integer, primary_key=True)
    task = Column(String, default='default_value')
    deadline = Column(Date, default=datetime.today())

    def __str__(self):
        return f'{self.task}'

    def __repr__(self):
        return f'id = {self.id}, task = {self.task}, deadline = {self.deadline}'


engine = create_engine('sqlite:///todo.db?check_same_thread=False')

Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
session = Session()
today = datetime.today()


class Interface:
    menu = ["1) Today's tasks", "2) Week's tasks", "3) All tasks", "4) Missed tasks", "5) Add task", "6) Delete task", "0) Exit"]

    def start(self):

        while 1:
            self.call_menu()
            user_choice = int(input())
            if user_choice == 0:
                self.leave()
                break
            elif user_choice == 1:
                self.today_tasks()
            elif user_choice == 2:
                self.week_tasks()
            elif user_choice == 3:
                self.all_tasks()
            elif user_choice == 4:
                self.missed_tasks()
            elif user_choice == 5:
                self.add_task()
            elif user_choice == 6:
                self.delete_tasks()
            else:
                print(f"There is no option {user_choice}. Please use 1, 2, ..., number of options to choose the option.")

    def today_tasks(self):

        tasks = session.query(Task).filter(Task.deadline == today).all()
        print(f"Today {today.day} {today.strftime('%b')}:")
        if len(tasks) != 0:
            for i in range(len(tasks)):
                print(f'{i + 1}. {tasks[i]}.')
        else:
            self.print_short()
        print()

    def week_tasks(self):

        for i in range(7):
            day = today + timedelta(days=i)
            tasks = session.query(Task).filter(Task.deadline == day.date()).all()
            self.print_short(day)

            if len(tasks) == 0:
                self.print_short()
                print()
            else:
                for i in range(len(tasks)):
                    print(f'{i + 1}. {tasks[i]}')
                print()

    def all_tasks(self):

        tasks = session.query(Task).all()

        if len(tasks) == 0:
            self.print_short()
        else:
            for i, task in enumerate(sorted(tasks, key=lambda tasks: tasks.deadline), start=1):
                print(f"{i+1}. {task}. {task.deadline.day} {task.deadline.strftime('%b')}")
        print()

    def add_task(self):

        new_task = Task(task=input("Enter task:\n"), deadline=datetime.strptime(input("Enter deadline:\n"), '%Y-%m-%d'))  # if can't work check the symbol ":"

        session.add(new_task)
        session.commit()
        print(new_task.task)
        print("The ask has been added!\n")

    def leave(self):
        print("Bye!")

    def call_menu(self):
        for menu_ in Interface.menu:
            print(menu_)
        print()

    def print_short(self, day=None):
        if day is None:
            print("Nothing to do!")
        else:
            print(f"{day.strftime('%A')} {day.day} {day.strftime('%b')}:")

    def missed_tasks(self):

        tasks = session.query(Task).filter(Task.deadline < today.date()).all()

        if len(tasks) == 0:
            print("Nothing is missed!")
        else:
            for i in range(len(tasks)):
                print(f"{i + 1}. {tasks[i]}. {tasks[i].deadline.day} {tasks[i].deadline.strftime('%b'):}")
        print()

    def delete_tasks(self):

        print("Choose the number of the task you want to delete:")
        tasks = session.query(Task).all()
        tasks = sorted(tasks, key=lambda tasks: tasks.deadline)

        for i, task in enumerate(tasks, start=1):
            print(f"{i+ 1}. {task}. {task.deadline.day} {task.deadline.strftime('%b')}")

        session.delete(tasks[int(input()) - 1])
        session.commit()


todo = Interface()
todo.start()

# possible improvements:
# 1. create class DBEngine and methods, which will find (maybe print query results) and delete queries
# 2. remove redundant print()
