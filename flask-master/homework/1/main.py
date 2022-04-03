from flask import Flask, url_for, request, render_template, redirect 
from loginform import LoginForm


app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'

@app.route('/')
@app.route('/index')
def index():
    return render_template('base.html', title='Домашняя страница' )

@app.route('/training/<string:prof>')
def training(prof):
    
    prof_data = {
        'header': "Инженерные тренажеры",
        'img' : url_for('static', filename='img/it.png')
    }
    if prof.find('инженер')==-1 and prof.find('строитель')==-1:
            prof_data = {
                'header': "Научные симуляторы",
                'img' : url_for('static', filename='img/ns.png')
            }
        
    return render_template('training.html', title='Тренировки по специальности', prof_data=prof_data )

@app.route('/list_prof/<string:list_kind>')
def list_prof(list_kind):
    prof_list=['Слесарь', 'Инжинер', 'Врач']
    return render_template('list_prof.html', title='Список профессий', list=list_kind, professions=prof_list )

@app.route('/auto_answer')
@app.route('/answer')
def answer():
    answer_data = {
        'title':'Анкета',
        'surname' : 'Алимова',
        'name' : 'Варвара',
        'education' : 'начальное',
        'profession' : 'жук',
        'sex' : 'женский',
        'motivation' : 'Уйду туда, где нет домашки',
        'ready' : True
    }
    print(answer_data.keys())
    return render_template('auto_answer.html', answer_data=answer_data )
    
@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        return redirect('/')
    return render_template('login.html', title='Авторизация', form=form)   
    
if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
    
    