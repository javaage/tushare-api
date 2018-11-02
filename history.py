'''
Created on Oct 15, 2018

@author: spring
'''

from flask import Flask, request, Response
import tushare as ts
from flask import jsonify
from flask_cors import CORS
from common import *
from ichessSchema import *
import json
from dao.candidateDao import *
import dao.holderDao as holderDao

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

@app.route('/daily/<code>/<dt>')
def dailyDate(code,dt):
    dt=dt.replace('-','');
    dt=dt.replace('/','');
    ts.set_token('ded567c8b305a3ed36fb2b12b15ca0209a9d93f5880be42822234fa6')
    pro = ts.pro_api()
    df = ts.pro_bar(ts_code=code,pro_api=pro,start_date=dt, adj='qfq')
    return jsonify(data=df.values.tolist()) 

@app.route('/allstock')
def allstock():
    ts.set_token('ded567c8b305a3ed36fb2b12b15ca0209a9d93f5880be42822234fa6')
    pro = ts.pro_api()
#     df = pro.daily(ts_code=code)
    df = pro.stock_basic(exchange_id='', list_status='L', fields='ts_code,name,enname,exchange_id,fullname')
    return jsonify(data=df.values.tolist()) 

@app.route('/indexDelta/<indexCode>')
def indexDelta(indexCode):
    return jsonify(calIndexDelta(indexCode))

@app.route('/stockDelta/<stockCode>')
def stockDelta(stockCode):
    return jsonify(calStockDelta(stockCode))

@app.route('/indexWeight/<indexCode>')
def indexWeight(indexCode):
    ts.set_token('ded567c8b305a3ed36fb2b12b15ca0209a9d93f5880be42822234fa6')
    pro = ts.pro_api()
    df = pro.index_weight(index_code=indexCode, fields='con_code') 
    return jsonify(df.values.tolist())

@app.route('/wavestock/<stockCode>')
def wavestock(stockCode):
    query = Wavestock.select().where(Wavestock.code == stockCode);
    if(query):
        stock = query.get()
        return WavestockSchema().dumps(stock)
    return ""
 
@app.route('/waveindex/<indexCode>')
def waveindex(indexCode):
    query = Waveindex.select().where(Waveindex.code == indexCode);
    if(query):
        stock = query.get()
        return WaveindexSchema().dumps(stock)
    return ""

@app.route('/candidate/last')
def candidateLast():
    candidate = getLastCandidate()
    return CandidateSchema().dumps(candidate)

@app.route('/holder')
def getHolderList():
    list = holderDao.getHolderList()
    return HolderSchema(many=True).dumps(list)

@app.route('/holder/<code>')
def getHolderByCode(code):
    holder = holderDao.getHolderByCode(code)
    return HolderSchema().dumps(holder)

@app.route('/holder', methods=["POST"])
def saveHolder():
    holder = json.loads(request.data)
    if holderDao.saveHolder(holder) > 0:
        return sucess_response()
    else:
        return fail_response()
    
@app.route('/holder', methods=["PUT"])
def updateHolder():
    holder = json.loads(request.data)
    if holderDao.updateHolder(holder) > 0:
        return sucess_response()
    else:
        return fail_response()

@app.route('/holder/<code>', methods=["DELETE"])
def deleteHolder(code):
    if holderDao.deleteHolder(code) > 0:
        return sucess_response()
    else:
        return fail_response()
    
if __name__ == '__main__':
    app.run(host='0.0.0.0',port=8001)


