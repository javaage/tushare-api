from dao.ichess import Collect

def getCollectList():
    result = []
    query = Collect.select();
    for collect in query:
        result.append(collect)
    return result

def getCollectByCode(code):
    query = Collect.select().where(Collect.code==code)
    if(query):
        return query.get()
    else:
        return
    
def saveCollect(collect):
    return Collect.insert(collect).execute()

def updateCollect(collect):
    return Collect.update(collect).where(Collect.code==collect['code']).execute()

def deleteCollect(code):
    return Collect.delete().where(Collect.code==code).execute()