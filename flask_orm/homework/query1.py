from re import U
from data.users import User
from data.jobs import Jobs
from data.db_session import global_init, create_session

if __name__ == '__main__':
    #db_name = input()
    db_name = '/home/varvara/PycharmProjects/pythonProject8/flask_orm/homework/db/mars_explorer.db'
    global_init(db_name)
    db_sess = create_session()
    for user in db_sess.query(User).filter(User.address == 'module_1',
                                           User.speciality.notlike('%engineer%'),
                                           User.position.notlike('%engineer%')).all():
        print(user.id)

