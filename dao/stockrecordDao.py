from dao.ichess import Stockrecord

def getStockrecordList():
    result = []
    query = Stockrecord.select();
    for stockrecord in query:
        result.append(stockrecord)
    return result

def getStockrecordByCode(code):
    query = Stockrecord.select().where(Stockrecord.code==code)
    if(query):
        return query.get()
    else:
        return
    
def saveStockrecord(stockrecord):
    return Stockrecord.insert(stockrecord).execute()

def updateStockrecord(stockrecord):
    return Stockrecord.update(stockrecord).where(Stockrecord.code==stockrecord['code']).execute()

def deleteStockrecord(code):
    return Stockrecord.delete().where(Stockrecord.code==code).execute()