from flask import Flask, render_template
from werkzeug.utils import redirect

from data.db_session import *
from data.users import *
from loginform import LoginForm

app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'


@app.route('/inde')
def inde():
    global_init(f"db/blogs.db")
    db_sess = create_session()
    colonists = db_sess.query(User).all()
    return render_template('index.html', title='Журнал работ',
                           colonists=colonists)

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        return redirect('/success')
    return render_template('login.html', title='Авторизация', form=form)

@app.route('/success')
def index():
    return "Вы зарегестрированы. Ожидайте, за вами придут"

if __name__ == '__main__':
    app.run()
