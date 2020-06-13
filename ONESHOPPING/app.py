from flask import Flask, render_template, jsonify, request
app = Flask(__name__)

from pymongo import MongoClient           # pymongo를 임포트 하기(패키지 인스톨 먼저 해야겠죠?)
client = MongoClient('localhost', 27017)  # mongoDB는 27017 포트로 돌아갑니다.
db = client.dbsparta                      # 'dbsparta'라는 이름의 db를 만듭니다.

## HTML을 주는 부분
@app.route('/')
def home():
    return render_template('index.html')

## API 역할을 하는 부분
@app.route('/orders', methods=['POST'])
def write_review():
    name_receive = request.form['name_give']
    count_receive = request.form['count_give']
    address_receive = request.form['address_give']
    phone_receive = request.form['phone_give']

    doc = {
        'name' : name_receive,
        'count' : count_receive,
        'address' : address_receive,
        'phone' : phone_receive

    }

    db.oneshopping.insert_one(doc)

    return jsonify({'result':'success', 'msg': '저장완료'})


@app.route('/orders', methods=['GET'])
def read_reviews():
    orders = list(db.oneshopping.find({},{'_id':0}))
    return jsonify({'result':'success', 'all_order': orders})


if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)