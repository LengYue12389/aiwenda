""" 
    所依赖的库和框架：
    flask, SQLAlachmey, wtforms
    数据库：MySQl
    Python版本：3.9.2
    使用蓝图，按模块进行拆分
 """

from utils.filters import number_split
from flask import Flask
from models import db
from accounts.views import accounts
from qa.views import qa


app = Flask(__name__, template_folder='./templates')
app.config.from_object('config.Config')     #从配置文件加载配置
#绑定到数据库
db.init_app(app)

#注册蓝图
app.register_blueprint(accounts, url_prefix='/accounts')
app.register_blueprint(qa, url_prefix='/')

# 注册过虑器
app.jinja_env.filters['number_split'] = number_split

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8001, debug=True)
    # db.create_all(app=app)