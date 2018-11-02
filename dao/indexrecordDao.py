from dao.ichess import Indexrecord

def getIndexrecordList():
    result = []
    query = Indexrecord.select();
    for indexrecord in query:
        result.append(indexrecord)
    return result

def getIndexrecordByCode(code):
    query = Indexrecord.select().where(Indexrecord.code==code)
    if(query):
        return query.get()
    else:
        return
    
def saveIndexrecord(indexrecord):
    return Indexrecord.insert(indexrecord).execute()

def updateIndexrecord(indexrecord):
    return Indexrecord.update(indexrecord).where(Indexrecord.code==indexrecord['code']).execute()

def deleteIndexrecord(code):
    return Indexrecord.delete().where(Indexrecord.code==code).execute()