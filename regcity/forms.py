from wtforms import Form, StringField

class PostForm(Form):
    name = StringField('Имя: ')