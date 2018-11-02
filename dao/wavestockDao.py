from dao.ichess import Wavestock

def getWavestockList():
    result = []
    query = Wavestock.select();
    for wavestock in query:
        result.append(wavestock)
    return result

def getWavestockByCode(code):
    query = Wavestock.select().where(Wavestock.code==code)
    if(query):
        return query.get()
    else:
        return
    
def saveWavestock(wavestock):
    return Wavestock.insert(wavestock).execute()

def updateWavestock(wavestock):
    return Wavestock.update(wavestock).where(Wavestock.code==wavestock['code']).execute()

def deleteWavestock(code):
    return Wavestock.delete().where(Wavestock.code==code).execute()