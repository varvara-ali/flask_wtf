from flask import Flask, render_template
from data import db_session
from data.users import User
from data.jobs import Jobs

app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'


def main():
    db_session.global_init("/home/varvara/PycharmProjects/pythonProject8/flask_orm/homework/db/mars_explorer.db")
    app.run()


@app.route("/")
def index():
    db_sess = db_session.create_session()
    jobs = db_sess.query(Jobs)
    return render_template("index.html", jobs=jobs)
      
    
def add_users():
    db_session.global_init("/home/varvara/PycharmProjects/pythonProject8/flask_orm/homework/db/mars_explorer.db")
    db_sess = db_session.create_session()
    
    user = User()
    
    user.surname ='Scott'
    user.name = 'Ridley'
    user.age = 21
    user.position = 'captain'
    user.speciality = 'research engineer'
    user.address = 'module_1'
    user.email = 'scott_chief@mars.org'
    db_sess.add(user)
    
    user1 = User()
    user1.surname = 'Parker'
    user1.name = 'Piter'
    user1.age = 18
    user1.position = 'spiderman'
    user1.speciality = 'friendly neighbor'
    user1.address = 'module_2'
    user1.email = 'spiderman@mars.org'
    db_sess.add(user1)
    
    user2 = User()
    user2.surname = 'Dragov'
    user2.name = 'Ivan'
    user2.age = 34
    user2.position = 'teache'
    user2.speciality = 'soldier'
    user2.address = 'module_3'
    user2.email = 'ivanthebest@mars.org'
    db_sess.add(user2)
    
    db_sess.commit()


def add_job():
    db_session.global_init("/home/varvara/PycharmProjects/pythonProject8/flask_orm/homework/db/mars_explorer.db")
    db_sess = db_session.create_session()
    job = Jobs()
    job.team_leader = 1
    job.job = 'deployment of residential modules 1 and 2'
    job.work_size = 15
    job.collaborators = '2, 3'
    job.is_finished = False
    db_sess = db_session.create_session()
    db_sess.add(job)
    db_sess.commit()


if __name__ == '__main__':
    # add_users()
    # add_job()
    main()