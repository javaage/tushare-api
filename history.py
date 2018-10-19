'''
Created on Oct 15, 2018

@author: spring
'''

from flask import Flask
import tushare as ts
from flask import jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)
# CORS(app, supports_credentials=True)

@app.route('/')
def hello_world():
    ts.set_token('ded567c8b305a3ed36fb2b12b15ca0209a9d93f5880be42822234fa6')
    pro = ts.pro_api()
    df = pro.daily(ts_code='000001.SZ', start_date='20180701', end_date='20180718')
    return jsonify(data=df.values.tolist())  

@app.route('/daily/<code>')
def daily(code):
    ts.set_token('ded567c8b305a3ed36fb2b12b15ca0209a9d93f5880be42822234fa6')
    pro = ts.pro_api()
#     df = pro.daily(ts_code=code)
    df = ts.pro_bar(pro_api=pro, ts_code=code, adj='qfq')
    return jsonify(data=df.values.tolist()) 

@app.route('/allstock')
def allstock():
    ts.set_token('ded567c8b305a3ed36fb2b12b15ca0209a9d93f5880be42822234fa6')
    pro = ts.pro_api()
#     df = pro.daily(ts_code=code)
    df = pro.stock_basic(exchange_id='', list_status='L', fields='ts_code,name,enname,exchange_id,fullname')
    return jsonify(data=df.values.tolist()) 

if __name__ == '__main__':
    app.run(host='0.0.0.0',port=8888)
