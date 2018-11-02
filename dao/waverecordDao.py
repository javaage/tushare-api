from dao.ichess import Waverecord

def getWaverecordList():
    result = []
    query = Waverecord.select();
    for waverecord in query:
        result.append(waverecord)
    return result

def getWaverecordByCode(code):
    query = Waverecord.select().where(Waverecord.code==code)
    if(query):
        return query.get()
    else:
        return
    
def saveWaverecord(waverecord):
    return Waverecord.insert(waverecord).execute()

def updateWaverecord(waverecord):
    return Waverecord.update(waverecord).where(Waverecord.code==waverecord['code']).execute()

def deleteWaverecord(code):
    return Waverecord.delete().where(Waverecord.code==code).execute()