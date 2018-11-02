from dao.ichess import CandRate

def getCandRateList():
    result = []
    query = CandRate.select();
    for candRate in query:
        result.append(candRate)
    return result

def getCandRateByCode(code):
    query = CandRate.select().where(CandRate.code==code)
    if(query):
        return query.get()
    else:
        return
    
def saveCandRate(candRate):
    return CandRate.insert(candRate).execute()

def updateCandRate(candRate):
    return CandRate.update(candRate).where(CandRate.code==candRate['code']).execute()

def deleteCandRate(code):
    return CandRate.delete().where(CandRate.code==code).execute()