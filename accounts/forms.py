import hashlib

from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, ValidationError
from wtforms.validators import DataRequired, Length, EqualTo

from models import User, db, UserProfile
from utils.validators import phone_required


class RegisterForm(FlaskForm):
    """ 用户注册 """
    username = StringField(label='用户名', render_kw={
        'class': 'form-control input-lg',
        'placeholder': '请输入用户名'
    }, validators=[DataRequired('请输入用户名'), phone_required])
    nickname = StringField(label='用户昵称', render_kw={
        'class': 'form-control input-lg',
        'placeholder': '请输入用户昵称'
    }, validators=[DataRequired('请输入用户昵称'),
                   Length(min=2, max=20, message='昵称长度在2-20之间')])
    password = PasswordField(label='密码', render_kw={
        'class': 'form-control input-lg',
        'placeholder': '请输入密码'
    }, validators=[DataRequired('请输入密码')])
    confirm_password = PasswordField(label='确认密码', render_kw={
        'class': 'form-control input-lg',
        'placeholder': '请输入确认密码'
    }, validators=[DataRequired('请输入确认密码'),
                   EqualTo('password', message='两次密码输入不一致')])

    def validate_username(self, field):
        """ 检测用户名是否已经存在 """
        user = User.query.filter_by(username=field.data).first()
        if user:
            raise ValidationError('该用户名已经存在')
        return field

    def register(self):
        """ 自定义的用户注册函数 """
        # 1. 获取表单信息
        username = self.username.data
        password = self.password.data
        nickname = self.nickname.data
        # 2. 添加到db.session
        try:
            # 将密码加密存储
            password = hashlib.sha256(password.encode()).hexdigest()
            user_obj = User(username=username, password=password, nickname=nickname)
            db.session.add(user_obj)
            profile = UserProfile(username=username, user=user_obj)
            db.session.add(profile)
            db.session.commit()
            return user_obj
        except Exception as e:
            print(e)
        return None

