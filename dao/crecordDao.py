from dao.ichess import Crecord

def getCrecordList():
    result = []
    query = Crecord.select();
    for crecord in query:
        result.append(crecord)
    return result

def getCrecordByCode(code):
    query = Crecord.select().where(Crecord.code==code)
    if(query):
        return query.get()
    else:
        return
    
def saveCrecord(crecord):
    return Crecord.insert(crecord).execute()

def updateCrecord(crecord):
    return Crecord.update(crecord).where(Crecord.code==crecord['code']).execute()

def deleteCrecord(code):
    return Crecord.delete().where(Crecord.code==code).execute()