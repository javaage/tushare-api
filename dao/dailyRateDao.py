from dao.ichess import DailyRate

def getDailyRateList():
    result = []
    query = DailyRate.select();
    for dailyRate in query:
        result.append(dailyRate)
    return result

def getDailyRateByCode(code):
    query = DailyRate.select().where(DailyRate.code==code)
    if(query):
        return query.get()
    else:
        return
    
def saveDailyRate(dailyRate):
    return DailyRate.insert(dailyRate).execute()

def updateDailyRate(dailyRate):
    return DailyRate.update(dailyRate).where(DailyRate.code==dailyRate['code']).execute()

def deleteDailyRate(code):
    return DailyRate.delete().where(DailyRate.code==code).execute()