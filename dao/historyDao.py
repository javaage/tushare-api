from dao.ichess import History

def getHistoryList():
    result = []
    query = History.select();
    for history in query:
        result.append(history)
    return result

def getHistoryByCode(code):
    query = History.select().where(History.code==code)
    if(query):
        return query.get()
    else:
        return
    
def saveHistory(history):
    return History.insert(history).execute()

def updateHistory(history):
    return History.update(history).where(History.code==history['code']).execute()

def deleteHistory(code):
    return History.delete().where(History.code==code).execute()