from re import U
from data.users import User
from data.jobs import Jobs
from data.db_session import global_init, create_session

if __name__ == '__main__':
    #db_name = input()
    db_name = 'db\mars_explorer.db'
    global_init(db_name)
    db_sess = create_session()
    for user in db_sess.query(User).filter(User.address == 'module_1',
                                           User.position.notlike('%engineer%'),
                                           User.speciality.not_like('%engineer%')).all():
        print(user.id)