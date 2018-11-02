from dao.ichess import Category

def getCategoryList():
    result = []
    query = Category.select();
    for category in query:
        result.append(category)
    return result

def getCategoryByCode(code):
    query = Category.select().where(Category.code==code)
    if(query):
        return query.get()
    else:
        return
    
def saveCategory(category):
    return Category.insert(category).execute()

def updateCategory(category):
    return Category.update(category).where(Category.code==category['code']).execute()

def deleteCategory(code):
    return Category.delete().where(Category.code==code).execute()