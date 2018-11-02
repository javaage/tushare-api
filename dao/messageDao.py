from dao.ichess import Message

def getMessageList():
    result = []
    query = Message.select();
    for message in query:
        result.append(message)
    return result

def getMessageByCode(code):
    query = Message.select().where(Message.code==code)
    if(query):
        return query.get()
    else:
        return
    
def saveMessage(message):
    return Message.insert(message).execute()

def updateMessage(message):
    return Message.update(message).where(Message.code==message['code']).execute()

def deleteMessage(code):
    return Message.delete().where(Message.code==code).execute()