from dao.ichess import Holder

def getHolderList():
    result = []
    query = Holder.select();
    for holder in query:
        result.append(holder)
    return result

def getHolderByCode(code):
    query = Holder.select().where(Holder.code==code)
    if(query):
        return query.get()
    else:
        return
    
def saveHolder(holder):
    return Holder.insert(holder).execute()

def updateHolder(holder):
    return Holder.update(holder).where(Holder.code==holder['code']).execute()

def deleteHolder(code):
    return Holder.delete().where(Holder.code==code).execute()