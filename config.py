import os


class Config(object):
    """ 配置信息，文件上传的根路径以及数据库连接的uri """
    #数据库的配置uri
    SQLALCHEMY_DATABASE_URI = 'mysql://root:panshidi@localhost:3306/flask_qa'
    SECRET_KEY = 'abcdsacb12312'
    MEDIA_ROOT = os.path.join(os.path.dirname(__file__), 'medias')
    SQLALCHEMY_TRACK_MODIFICATIONS = True