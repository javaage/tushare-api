'''
Created on Oct 15, 2018

@author: spring
'''
from flask import Flask
from ichessSchema import *
from dao.holderDao import *

app = Flask(__name__)

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

@app.route('/holder/<code>', methods=["DELETE"])
def deleteHolder(code):
    if holderDao.deleteHolder(code) > 0:
        return sucess_response()
    else:
        return fail_response()



