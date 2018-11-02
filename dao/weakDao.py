from dao.ichess import Weak

def getWeakList():
    result = []
    query = Weak.select();
    for weak in query:
        result.append(weak)
    return result

def getWeakByCode(code):
    query = Weak.select().where(Weak.code==code)
    if(query):
        return query.get()
    else:
        return
    
def saveWeak(weak):
    return Weak.insert(weak).execute()

def updateWeak(weak):
    return Weak.update(weak).where(Weak.code==weak['code']).execute()

def deleteWeak(code):
    return Weak.delete().where(Weak.code==code).execute()