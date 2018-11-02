from dao.ichess import Wavedaily

def getWavedailyList():
    result = []
    query = Wavedaily.select();
    for wavedaily in query:
        result.append(wavedaily)
    return result

def getWavedailyByCode(code):
    query = Wavedaily.select().where(Wavedaily.code==code)
    if(query):
        return query.get()
    else:
        return
    
def saveWavedaily(wavedaily):
    return Wavedaily.insert(wavedaily).execute()

def updateWavedaily(wavedaily):
    return Wavedaily.update(wavedaily).where(Wavedaily.code==wavedaily['code']).execute()

def deleteWavedaily(code):
    return Wavedaily.delete().where(Wavedaily.code==code).execute()