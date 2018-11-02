from dao.ichess import Waveindex

def getWaveindexList():
    result = []
    query = Waveindex.select();
    for waveindex in query:
        result.append(waveindex)
    return result

def getWaveindexByCode(code):
    query = Waveindex.select().where(Waveindex.code==code)
    if(query):
        return query.get()
    else:
        return
    
def saveWaveindex(waveindex):
    return Waveindex.insert(waveindex).execute()

def updateWaveindex(waveindex):
    return Waveindex.update(waveindex).where(Waveindex.code==waveindex['code']).execute()

def deleteWaveindex(code):
    return Waveindex.delete().where(Waveindex.code==code).execute()