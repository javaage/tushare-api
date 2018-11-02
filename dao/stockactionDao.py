from dao.ichess import Stockaction

def getStockactionList():
    result = []
    query = Stockaction.select();
    for stockaction in query:
        result.append(stockaction)
    return result

def getStockactionByCode(code):
    query = Stockaction.select().where(Stockaction.code==code)
    if(query):
        return query.get()
    else:
        return
    
def saveStockaction(stockaction):
    return Stockaction.insert(stockaction).execute()

def updateStockaction(stockaction):
    return Stockaction.update(stockaction).where(Stockaction.code==stockaction['code']).execute()

def deleteStockaction(code):
    return Stockaction.delete().where(Stockaction.code==code).execute()