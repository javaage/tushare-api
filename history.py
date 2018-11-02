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

import dao.holderDao as holderDao
import dao.allstockDao as allstockDao
import dao.attendDao as attendDao
import dao.bkrecordDao as bkrecordDao
import dao.candRateDao as candRateDao
import dao.candidateDao as candidateDao
import dao.categoryDao as categoryDao
import dao.collectDao as collectDao
import dao.crecordDao as crecordDao
import dao.dailyDao as dailyDao
import dao.dailyRateDao as dailyRateDao
import dao.directorDao as directorDao
import dao.historyDao as historyDao
import dao.indexrecordDao as indexrecordDao
import dao.inspectDao as inspectDao
import dao.messageDao as messageDao
import dao.signDao as signDao
import dao.stockactionDao as stockactionDao
import dao.stockrecordDao as stockrecordDao
import dao.wavedailyDao as wavedailyDao
import dao.waveindexDao as waveindexDao
import dao.waverecordDao as waverecordDao
import dao.wavestockDao as wavestockDao
import dao.weakDao as weakDao

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

# @app.route('/allstock')
# def getAllstockList():
#     list = allstockDao.getAllstockList()
#     return AllstockSchema(many=True).dumps(list)

@app.route('/allstock/<code>')
def getAllstockByCode(code):
    allstock = allstockDao.getAllstockByCode(code)
    return AllstockSchema().dumps(allstock)

@app.route('/allstock', methods=["POST"])
def saveAllstock():
    allstock = json.loads(request.data)
    if allstockDao.saveAllstock(allstock) > 0:
        return sucess_response()
    else:
        return fail_response()
    
@app.route('/allstock', methods=["PUT"])
def updateAllstock():
    allstock = json.loads(request.data)
    if allstockDao.updateAllstock(allstock) > 0:
        return sucess_response()
    else:
        return fail_response()

@app.route('/allstock/<code>', methods=["DELETE"])
def deleteAllstock(code):
    if allstockDao.deleteAllstock(code) > 0:
        return sucess_response()
    else:
        return fail_response()

@app.route('/attend')
def getAttendList():
    list = attendDao.getAttendList()
    return AttendSchema(many=True).dumps(list)

@app.route('/attend/<code>')
def getAttendByCode(code):
    attend = attendDao.getAttendByCode(code)
    return AttendSchema().dumps(attend)

@app.route('/attend', methods=["POST"])
def saveAttend():
    attend = json.loads(request.data)
    if attendDao.saveAttend(attend) > 0:
        return sucess_response()
    else:
        return fail_response()
    
@app.route('/attend', methods=["PUT"])
def updateAttend():
    attend = json.loads(request.data)
    if attendDao.updateAttend(attend) > 0:
        return sucess_response()
    else:
        return fail_response()

@app.route('/attend/<code>', methods=["DELETE"])
def deleteAttend(code):
    if attendDao.deleteAttend(code) > 0:
        return sucess_response()
    else:
        return fail_response()

@app.route('/bkrecord')
def getBkrecordList():
    list = bkrecordDao.getBkrecordList()
    return BkrecordSchema(many=True).dumps(list)

@app.route('/bkrecord/<code>')
def getBkrecordByCode(code):
    bkrecord = bkrecordDao.getBkrecordByCode(code)
    return BkrecordSchema().dumps(bkrecord)

@app.route('/bkrecord', methods=["POST"])
def saveBkrecord():
    bkrecord = json.loads(request.data)
    if bkrecordDao.saveBkrecord(bkrecord) > 0:
        return sucess_response()
    else:
        return fail_response()
    
@app.route('/bkrecord', methods=["PUT"])
def updateBkrecord():
    bkrecord = json.loads(request.data)
    if bkrecordDao.updateBkrecord(bkrecord) > 0:
        return sucess_response()
    else:
        return fail_response()

@app.route('/bkrecord/<code>', methods=["DELETE"])
def deleteBkrecord(code):
    if bkrecordDao.deleteBkrecord(code) > 0:
        return sucess_response()
    else:
        return fail_response()

@app.route('/candRate')
def getCandRateList():
    list = candRateDao.getCandRateList()
    return CandRateSchema(many=True).dumps(list)

@app.route('/candRate/<code>')
def getCandRateByCode(code):
    candRate = candRateDao.getCandRateByCode(code)
    return CandRateSchema().dumps(candRate)

@app.route('/candRate', methods=["POST"])
def saveCandRate():
    candRate = json.loads(request.data)
    if candRateDao.saveCandRate(candRate) > 0:
        return sucess_response()
    else:
        return fail_response()
    
@app.route('/candRate', methods=["PUT"])
def updateCandRate():
    candRate = json.loads(request.data)
    if candRateDao.updateCandRate(candRate) > 0:
        return sucess_response()
    else:
        return fail_response()

@app.route('/candRate/<code>', methods=["DELETE"])
def deleteCandRate(code):
    if candRateDao.deleteCandRate(code) > 0:
        return sucess_response()
    else:
        return fail_response()
@app.route('/candidate')
def getCandidateList():
    list = candidateDao.getCandidateList()
    return CandidateSchema(many=True).dumps(list)

@app.route('/candidate/<code>')
def getCandidateByCode(code):
    candidate = candidateDao.getCandidateByCode(code)
    return CandidateSchema().dumps(candidate)

@app.route('/candidate', methods=["POST"])
def saveCandidate():
    candidate = json.loads(request.data)
    if candidateDao.saveCandidate(candidate) > 0:
        return sucess_response()
    else:
        return fail_response()
    
@app.route('/candidate', methods=["PUT"])
def updateCandidate():
    candidate = json.loads(request.data)
    if candidateDao.updateCandidate(candidate) > 0:
        return sucess_response()
    else:
        return fail_response()

@app.route('/candidate/<code>', methods=["DELETE"])
def deleteCandidate(code):
    if candidateDao.deleteCandidate(code) > 0:
        return sucess_response()
    else:
        return fail_response()

@app.route('/category')
def getCategoryList():
    list = categoryDao.getCategoryList()
    return CategorySchema(many=True).dumps(list)

@app.route('/category/<code>')
def getCategoryByCode(code):
    category = categoryDao.getCategoryByCode(code)
    return CategorySchema().dumps(category)

@app.route('/category', methods=["POST"])
def saveCategory():
    category = json.loads(request.data)
    if categoryDao.saveCategory(category) > 0:
        return sucess_response()
    else:
        return fail_response()
    
@app.route('/category', methods=["PUT"])
def updateCategory():
    category = json.loads(request.data)
    if categoryDao.updateCategory(category) > 0:
        return sucess_response()
    else:
        return fail_response()

@app.route('/category/<code>', methods=["DELETE"])
def deleteCategory(code):
    if categoryDao.deleteCategory(code) > 0:
        return sucess_response()
    else:
        return fail_response()

@app.route('/collect')
def getCollectList():
    list = collectDao.getCollectList()
    return CollectSchema(many=True).dumps(list)

@app.route('/collect/<code>')
def getCollectByCode(code):
    collect = collectDao.getCollectByCode(code)
    return CollectSchema().dumps(collect)

@app.route('/collect', methods=["POST"])
def saveCollect():
    collect = json.loads(request.data)
    if collectDao.saveCollect(collect) > 0:
        return sucess_response()
    else:
        return fail_response()
    
@app.route('/collect', methods=["PUT"])
def updateCollect():
    collect = json.loads(request.data)
    if collectDao.updateCollect(collect) > 0:
        return sucess_response()
    else:
        return fail_response()

@app.route('/collect/<code>', methods=["DELETE"])
def deleteCollect(code):
    if collectDao.deleteCollect(code) > 0:
        return sucess_response()
    else:
        return fail_response()

@app.route('/crecord')
def getCrecordList():
    list = crecordDao.getCrecordList()
    return CrecordSchema(many=True).dumps(list)

@app.route('/crecord/<code>')
def getCrecordByCode(code):
    crecord = crecordDao.getCrecordByCode(code)
    return CrecordSchema().dumps(crecord)

@app.route('/crecord', methods=["POST"])
def saveCrecord():
    crecord = json.loads(request.data)
    if crecordDao.saveCrecord(crecord) > 0:
        return sucess_response()
    else:
        return fail_response()
    
@app.route('/crecord', methods=["PUT"])
def updateCrecord():
    crecord = json.loads(request.data)
    if crecordDao.updateCrecord(crecord) > 0:
        return sucess_response()
    else:
        return fail_response()

@app.route('/crecord/<code>', methods=["DELETE"])
def deleteCrecord(code):
    if crecordDao.deleteCrecord(code) > 0:
        return sucess_response()
    else:
        return fail_response()

@app.route('/daily')
def getDailyList():
    list = dailyDao.getDailyList()
    return DailySchema(many=True).dumps(list)

@app.route('/daily/<code>')
def getDailyByCode(code):
    daily = dailyDao.getDailyByCode(code)
    return DailySchema().dumps(daily)

@app.route('/daily', methods=["POST"])
def saveDaily():
    daily = json.loads(request.data)
    if dailyDao.saveDaily(daily) > 0:
        return sucess_response()
    else:
        return fail_response()
    
@app.route('/daily', methods=["PUT"])
def updateDaily():
    daily = json.loads(request.data)
    if dailyDao.updateDaily(daily) > 0:
        return sucess_response()
    else:
        return fail_response()

@app.route('/daily/<code>', methods=["DELETE"])
def deleteDaily(code):
    if dailyDao.deleteDaily(code) > 0:
        return sucess_response()
    else:
        return fail_response()

@app.route('/dailyRate')
def getDailyRateList():
    list = dailyRateDao.getDailyRateList()
    return DailyRateSchema(many=True).dumps(list)

@app.route('/dailyRate/<code>')
def getDailyRateByCode(code):
    dailyRate = dailyRateDao.getDailyRateByCode(code)
    return DailyRateSchema().dumps(dailyRate)

@app.route('/dailyRate', methods=["POST"])
def saveDailyRate():
    dailyRate = json.loads(request.data)
    if dailyRateDao.saveDailyRate(dailyRate) > 0:
        return sucess_response()
    else:
        return fail_response()
    
@app.route('/dailyRate', methods=["PUT"])
def updateDailyRate():
    dailyRate = json.loads(request.data)
    if dailyRateDao.updateDailyRate(dailyRate) > 0:
        return sucess_response()
    else:
        return fail_response()

@app.route('/dailyRate/<code>', methods=["DELETE"])
def deleteDailyRate(code):
    if dailyRateDao.deleteDailyRate(code) > 0:
        return sucess_response()
    else:
        return fail_response()

@app.route('/director')
def getDirectorList():
    list = directorDao.getDirectorList()
    return DirectorSchema(many=True).dumps(list)

@app.route('/director/<code>')
def getDirectorByCode(code):
    director = directorDao.getDirectorByCode(code)
    return DirectorSchema().dumps(director)

@app.route('/director', methods=["POST"])
def saveDirector():
    director = json.loads(request.data)
    if directorDao.saveDirector(director) > 0:
        return sucess_response()
    else:
        return fail_response()
    
@app.route('/director', methods=["PUT"])
def updateDirector():
    director = json.loads(request.data)
    if directorDao.updateDirector(director) > 0:
        return sucess_response()
    else:
        return fail_response()

@app.route('/director/<code>', methods=["DELETE"])
def deleteDirector(code):
    if directorDao.deleteDirector(code) > 0:
        return sucess_response()
    else:
        return fail_response()

@app.route('/history')
def getHistoryList():
    list = historyDao.getHistoryList()
    return HistorySchema(many=True).dumps(list)

@app.route('/history/<code>')
def getHistoryByCode(code):
    history = historyDao.getHistoryByCode(code)
    return HistorySchema().dumps(history)

@app.route('/history', methods=["POST"])
def saveHistory():
    history = json.loads(request.data)
    if historyDao.saveHistory(history) > 0:
        return sucess_response()
    else:
        return fail_response()
    
@app.route('/history', methods=["PUT"])
def updateHistory():
    history = json.loads(request.data)
    if historyDao.updateHistory(history) > 0:
        return sucess_response()
    else:
        return fail_response()

@app.route('/history/<code>', methods=["DELETE"])
def deleteHistory(code):
    if historyDao.deleteHistory(code) > 0:
        return sucess_response()
    else:
        return fail_response()

@app.route('/indexrecord')
def getIndexrecordList():
    list = indexrecordDao.getIndexrecordList()
    return IndexrecordSchema(many=True).dumps(list)

@app.route('/indexrecord/<code>')
def getIndexrecordByCode(code):
    indexrecord = indexrecordDao.getIndexrecordByCode(code)
    return IndexrecordSchema().dumps(indexrecord)

@app.route('/indexrecord', methods=["POST"])
def saveIndexrecord():
    indexrecord = json.loads(request.data)
    if indexrecordDao.saveIndexrecord(indexrecord) > 0:
        return sucess_response()
    else:
        return fail_response()
    
@app.route('/indexrecord', methods=["PUT"])
def updateIndexrecord():
    indexrecord = json.loads(request.data)
    if indexrecordDao.updateIndexrecord(indexrecord) > 0:
        return sucess_response()
    else:
        return fail_response()

@app.route('/indexrecord/<code>', methods=["DELETE"])
def deleteIndexrecord(code):
    if indexrecordDao.deleteIndexrecord(code) > 0:
        return sucess_response()
    else:
        return fail_response()

@app.route('/inspect')
def getInspectList():
    list = inspectDao.getInspectList()
    return InspectSchema(many=True).dumps(list)

@app.route('/inspect/<code>')
def getInspectByCode(code):
    inspect = inspectDao.getInspectByCode(code)
    return InspectSchema().dumps(inspect)

@app.route('/inspect', methods=["POST"])
def saveInspect():
    inspect = json.loads(request.data)
    if inspectDao.saveInspect(inspect) > 0:
        return sucess_response()
    else:
        return fail_response()
    
@app.route('/inspect', methods=["PUT"])
def updateInspect():
    inspect = json.loads(request.data)
    if inspectDao.updateInspect(inspect) > 0:
        return sucess_response()
    else:
        return fail_response()

@app.route('/inspect/<code>', methods=["DELETE"])
def deleteInspect(code):
    if inspectDao.deleteInspect(code) > 0:
        return sucess_response()
    else:
        return fail_response()

@app.route('/message')
def getMessageList():
    list = messageDao.getMessageList()
    return MessageSchema(many=True).dumps(list)

@app.route('/message/<code>')
def getMessageByCode(code):
    message = messageDao.getMessageByCode(code)
    return MessageSchema().dumps(message)

@app.route('/message', methods=["POST"])
def saveMessage():
    message = json.loads(request.data)
    if messageDao.saveMessage(message) > 0:
        return sucess_response()
    else:
        return fail_response()
    
@app.route('/message', methods=["PUT"])
def updateMessage():
    message = json.loads(request.data)
    if messageDao.updateMessage(message) > 0:
        return sucess_response()
    else:
        return fail_response()

@app.route('/message/<code>', methods=["DELETE"])
def deleteMessage(code):
    if messageDao.deleteMessage(code) > 0:
        return sucess_response()
    else:
        return fail_response()

@app.route('/sign')
def getSignList():
    list = signDao.getSignList()
    return SignSchema(many=True).dumps(list)

@app.route('/sign/<code>')
def getSignByCode(code):
    sign = signDao.getSignByCode(code)
    return SignSchema().dumps(sign)

@app.route('/sign', methods=["POST"])
def saveSign():
    sign = json.loads(request.data)
    if signDao.saveSign(sign) > 0:
        return sucess_response()
    else:
        return fail_response()
    
@app.route('/sign', methods=["PUT"])
def updateSign():
    sign = json.loads(request.data)
    if signDao.updateSign(sign) > 0:
        return sucess_response()
    else:
        return fail_response()

@app.route('/sign/<code>', methods=["DELETE"])
def deleteSign(code):
    if signDao.deleteSign(code) > 0:
        return sucess_response()
    else:
        return fail_response()

@app.route('/stockaction')
def getStockactionList():
    list = stockactionDao.getStockactionList()
    return StockactionSchema(many=True).dumps(list)

@app.route('/stockaction/<code>')
def getStockactionByCode(code):
    stockaction = stockactionDao.getStockactionByCode(code)
    return StockactionSchema().dumps(stockaction)

@app.route('/stockaction', methods=["POST"])
def saveStockaction():
    stockaction = json.loads(request.data)
    if stockactionDao.saveStockaction(stockaction) > 0:
        return sucess_response()
    else:
        return fail_response()
    
@app.route('/stockaction', methods=["PUT"])
def updateStockaction():
    stockaction = json.loads(request.data)
    if stockactionDao.updateStockaction(stockaction) > 0:
        return sucess_response()
    else:
        return fail_response()

@app.route('/stockaction/<code>', methods=["DELETE"])
def deleteStockaction(code):
    if stockactionDao.deleteStockaction(code) > 0:
        return sucess_response()
    else:
        return fail_response()

@app.route('/stockrecord')
def getStockrecordList():
    list = stockrecordDao.getStockrecordList()
    return StockrecordSchema(many=True).dumps(list)

@app.route('/stockrecord/<code>')
def getStockrecordByCode(code):
    stockrecord = stockrecordDao.getStockrecordByCode(code)
    return StockrecordSchema().dumps(stockrecord)

@app.route('/stockrecord', methods=["POST"])
def saveStockrecord():
    stockrecord = json.loads(request.data)
    if stockrecordDao.saveStockrecord(stockrecord) > 0:
        return sucess_response()
    else:
        return fail_response()
    
@app.route('/stockrecord', methods=["PUT"])
def updateStockrecord():
    stockrecord = json.loads(request.data)
    if stockrecordDao.updateStockrecord(stockrecord) > 0:
        return sucess_response()
    else:
        return fail_response()

@app.route('/stockrecord/<code>', methods=["DELETE"])
def deleteStockrecord(code):
    if stockrecordDao.deleteStockrecord(code) > 0:
        return sucess_response()
    else:
        return fail_response()
 
@app.route('/wavedaily')
def getWavedailyList():
    list = wavedailyDao.getWavedailyList()
    return WavedailySchema(many=True).dumps(list)

@app.route('/wavedaily/<code>')
def getWavedailyByCode(code):
    wavedaily = wavedailyDao.getWavedailyByCode(code)
    return WavedailySchema().dumps(wavedaily)

@app.route('/wavedaily', methods=["POST"])
def saveWavedaily():
    wavedaily = json.loads(request.data)
    if wavedailyDao.saveWavedaily(wavedaily) > 0:
        return sucess_response()
    else:
        return fail_response()
    
@app.route('/wavedaily', methods=["PUT"])
def updateWavedaily():
    wavedaily = json.loads(request.data)
    if wavedailyDao.updateWavedaily(wavedaily) > 0:
        return sucess_response()
    else:
        return fail_response()

@app.route('/wavedaily/<code>', methods=["DELETE"])
def deleteWavedaily(code):
    if wavedailyDao.deleteWavedaily(code) > 0:
        return sucess_response()
    else:
        return fail_response()

@app.route('/waveindex')
def getWaveindexList():
    list = waveindexDao.getWaveindexList()
    return WaveindexSchema(many=True).dumps(list)

@app.route('/waveindex/<code>')
def getWaveindexByCode(code):
    waveindex = waveindexDao.getWaveindexByCode(code)
    return WaveindexSchema().dumps(waveindex)

@app.route('/waveindex', methods=["POST"])
def saveWaveindex():
    waveindex = json.loads(request.data)
    if waveindexDao.saveWaveindex(waveindex) > 0:
        return sucess_response()
    else:
        return fail_response()
    
@app.route('/waveindex', methods=["PUT"])
def updateWaveindex():
    waveindex = json.loads(request.data)
    if waveindexDao.updateWaveindex(waveindex) > 0:
        return sucess_response()
    else:
        return fail_response()

@app.route('/waveindex/<code>', methods=["DELETE"])
def deleteWaveindex(code):
    if waveindexDao.deleteWaveindex(code) > 0:
        return sucess_response()
    else:
        return fail_response()

@app.route('/waverecord')
def getWaverecordList():
    list = waverecordDao.getWaverecordList()
    return WaverecordSchema(many=True).dumps(list)

@app.route('/waverecord/<code>')
def getWaverecordByCode(code):
    waverecord = waverecordDao.getWaverecordByCode(code)
    return WaverecordSchema().dumps(waverecord)

@app.route('/waverecord', methods=["POST"])
def saveWaverecord():
    waverecord = json.loads(request.data)
    if waverecordDao.saveWaverecord(waverecord) > 0:
        return sucess_response()
    else:
        return fail_response()
    
@app.route('/waverecord', methods=["PUT"])
def updateWaverecord():
    waverecord = json.loads(request.data)
    if waverecordDao.updateWaverecord(waverecord) > 0:
        return sucess_response()
    else:
        return fail_response()

@app.route('/waverecord/<code>', methods=["DELETE"])
def deleteWaverecord(code):
    if waverecordDao.deleteWaverecord(code) > 0:
        return sucess_response()
    else:
        return fail_response()

@app.route('/waveStock')
def getWaveStockList():
    list = waveStockDao.getWaveStockList()
    return WaveStockSchema(many=True).dumps(list)

@app.route('/waveStock/<code>')
def getWaveStockByCode(code):
    waveStock = waveStockDao.getWaveStockByCode(code)
    return WaveStockSchema().dumps(waveStock)

@app.route('/waveStock', methods=["POST"])
def saveWaveStock():
    waveStock = json.loads(request.data)
    if waveStockDao.saveWaveStock(waveStock) > 0:
        return sucess_response()
    else:
        return fail_response()
    
@app.route('/waveStock', methods=["PUT"])
def updateWaveStock():
    waveStock = json.loads(request.data)
    if waveStockDao.updateWaveStock(waveStock) > 0:
        return sucess_response()
    else:
        return fail_response()

@app.route('/waveStock/<code>', methods=["DELETE"])
def deleteWaveStock(code):
    if waveStockDao.deleteWaveStock(code) > 0:
        return sucess_response()
    else:
        return fail_response()

@app.route('/weak')
def getWeakList():
    list = weakDao.getWeakList()
    return WeakSchema(many=True).dumps(list)

@app.route('/weak/<code>')
def getWeakByCode(code):
    weak = weakDao.getWeakByCode(code)
    return WeakSchema().dumps(weak)

@app.route('/weak', methods=["POST"])
def saveWeak():
    weak = json.loads(request.data)
    if weakDao.saveWeak(weak) > 0:
        return sucess_response()
    else:
        return fail_response()
    
@app.route('/weak', methods=["PUT"])
def updateWeak():
    weak = json.loads(request.data)
    if weakDao.updateWeak(weak) > 0:
        return sucess_response()
    else:
        return fail_response()

@app.route('/weak/<code>', methods=["DELETE"])
def deleteWeak(code):
    if weakDao.deleteWeak(code) > 0:
        return sucess_response()
    else:
        return fail_response()
                                                                       
if __name__ == '__main__':
    app.run(host='0.0.0.0',port=8001)


