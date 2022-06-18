from flask import Flask, render_template, jsonify, request

app = Flask(__name__)

from pymongo import MongoClient

client = MongoClient('localhost', 27017)
db = client.dbhomework


## HTML 화면 보여주기
@app.route('/')
def homework():
    return render_template('index.html')


# 주문하기(POST) API
@app.route('/order', methods=['POST'])
def save_order():
    orderName_receive = request.form['orderName_give']
    orderCount_receive = request.form['orderCount_give']
    orderAddress_receive = request.form['orderAddress_give']
    orderPhone_receive = request.form['orderPhone_give']
    print(orderName_receive, orderCount_receive, orderAddress_receive, orderPhone_receive)

    # DB 저장
    doc = {
        'orderName':orderName_receive,
        'orderCount':orderCount_receive,
        'orderAddress':orderAddress_receive,
        'orderPhone':orderPhone_receive
    }
    db.aloneShop.insert_one(doc)

    return jsonify({'msg': '주문이 완료되었습니다'})


# 주문 목록보기(Read) API
@app.route('/order', methods=['GET'])
def view_orders():
    orders = list(db.aloneShop.find({},{'_id':False}))
    print('서버단에서 list : ',orders)
    return jsonify({'orders': orders})


if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)