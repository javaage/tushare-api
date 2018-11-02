from dao.ichess import Bkrecord

def getBkrecordList():
    result = []
    query = Bkrecord.select();
    for bkrecord in query:
        result.append(bkrecord)
    return result

def getBkrecordByCode(code):
    query = Bkrecord.select().where(Bkrecord.code==code)
    if(query):
        return query.get()
    else:
        return
    
def saveBkrecord(bkrecord):
    return Bkrecord.insert(bkrecord).execute()

def updateBkrecord(bkrecord):
    return Bkrecord.update(bkrecord).where(Bkrecord.code==bkrecord['code']).execute()

def deleteBkrecord(code):
    return Bkrecord.delete().where(Bkrecord.code==code).execute()