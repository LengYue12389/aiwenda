from flask import Blueprint
from flask import render_template
from flask import request, abort
from models import Question


qa = Blueprint('qa', __name__, template_folder='./templates', static_folder='../assets')

@qa.route('/')
def index():    #主页
    per_page = 20
    page = int(request.args.get('page', 1))
    #从数据库往外拿数据
    page_data = Question.query.filter_by(is_valid=True).paginate(per_page=per_page, page=page)
    return render_template('index.html', page_data=page_data)

@qa.route('/follow')
def follow():   #关注页面
    per_page = 20
    page = int(request.args.get('page', 1))
    #从数据库往外拿数据
    page_data = Question.query.filter_by(is_valid=True).paginate(per_page=per_page, page=page)
    return render_template('follow.html', page_data=page_data)

@qa.route('/write')
def write():    #写文章
    return render_template('write.html')


@qa.route('/detail/<int:q_id>')
def detail(q_id):   #从数据库里拿到问题信息
    # 1. 查询问题信息
    question = Question.query.get(q_id)
    if not question.is_valid:
        abort(404)
    # 2. 展示第一条回答信息
    answer = question.answer_list.filter_by(is_valid=True).first()

    return render_template('detail.html', question=question, answer=answer)

