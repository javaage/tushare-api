from dao.ichess import Allstock

def getAllstockList():
    result = []
    query = Allstock.select();
    for allstock in query:
        result.append(allstock)
    return result

def getAllstockByCode(code):
    query = Allstock.select().where(Allstock.code==code)
    if(query):
        return query.get()
    else:
        return
    
def saveAllstock(allstock):
    return Allstock.insert(allstock).execute()

def updateAllstock(allstock):
    return Allstock.update(allstock).where(Allstock.code==allstock['code']).execute()

def deleteAllstock(code):
    return Allstock.delete().where(Allstock.code==code).execute()