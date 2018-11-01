from marshmallow import Schema, fields

class AllstockSchema(Schema):
    code = fields.Str()
    name = fields.Str()
    py = fields.Str()


class AttendSchema(Schema):
    ascrate = fields.Float()
    code = fields.Str()
    descrate = fields.Float()
    equalrate = fields.Float()
    name = fields.Str()
    time = fields.Str()


class BkrecordSchema(Schema):
    code = fields.Str()
    date = fields.DateTime()
    increase = fields.Float()
    name = fields.Str()
    time = fields.Str()


class CandRateSchema(Schema):
    a = fields.Float()
    b = fields.Float()
    code = fields.Str()
    increase = fields.Float()
    name = fields.Str()
    r = fields.Float()
    time = fields.Str()


class CandidateSchema(Schema):
    id = fields.Str()
    preflist = fields.Str()
    time = fields.DateTime()


class CategorySchema(Schema):
    code = fields.Str()
    content = fields.Str()
    name = fields.Str()
    type = fields.Str()


class Collect(Schema):
    code = fields.Str()
    date = fields.DateTime()
    flag = fields.Integer()
    name = fields.Str()


class Crecord(Schema):
    code = fields.Str()
    date = fields.DateTime()
    increase = fields.Float()
    name = fields.Str()
    time = fields.Str()

class Daily(Schema):
    clmn = fields.Float()
    code = fields.Str()
    current = fields.Float()
    date = fields.DateTime()
    high = fields.Float()
    low = fields.Float()
    open = fields.Float()

class DailyRateSchema(Schema):
    a = fields.Float()
    b = fields.Float()
    code = fields.Str()
    date = fields.DateTime()
    r = fields.Float()

class DirectorSchema(Schema):
    arrow = fields.Str()
    code = fields.Str()
    level = fields.Integer()
    name = fields.Str()
    price = fields.Float()
    time = fields.Str()
    total = fields.Integer()
    type = fields.Str()

class HistorySchema(Schema):
    ftime = fields.Str()
    id = fields.Str()
    ltime = fields.Str()
    record = fields.Str()
    type = fields.Str()

class HolderSchema(Schema):
    ascrate = fields.Float()
    code = fields.Str()
    descrate = fields.Float()
    equalrate = fields.Float()
    name = fields.Str()
    time = fields.Str()

class IchessTestSchema(Schema):
    age = fields.Integer()
    name = fields.Str()

class IndexrecordSchema(Schema):
    avg = fields.Float()
    clmn = fields.Float()
    close = fields.Float()
    code = fields.Str()
    current = fields.Float()
    date = fields.DateTime()
    high = fields.Float()
    low = fields.Float()
    money = fields.Float()
    name = fields.Str()
    open = fields.Float()
    time = fields.Integer()

class InspectSchema(Schema):
    code = fields.Str()
    create_date = fields.Str()
    flag = fields.Integer()
    name = fields.Str()
    opt = fields.Str()
    type = fields.Str()
    value = fields.Float()

class MessageSchema(Schema):
    code = fields.Str()
    flag = fields.Integer()
    message = fields.Str()
    name = fields.Str()
    time = fields.Str()

class SignSchema(Schema):
    buy = fields.Integer()
    code = fields.Str()
    concept = fields.Str()
    current = fields.Float()
    high = fields.Float()
    low = fields.Float()
    prefbuy = fields.Float()
    prefsell = fields.Float()
    sell = fields.Integer()

class StockactionSchema(Schema):
    action = fields.Str()
    arrow = fields.Str()
    content = fields.Str()
    detail = fields.Str()
    dex = fields.Float()
    ftime = fields.Str()
    gw = fields.Str()
    ltime = fields.Str()
    pref = fields.Str()
    pref1 = fields.Str()
    queue = fields.Str()
    strong = fields.Float()
    time = fields.Str()
    type = fields.Str()

class StockrecordSchema(Schema):
    avg = fields.Float()
    clmn = fields.Float()
    close = fields.Float()
    code = fields.Str()
    current = fields.Float()
    date = fields.DateTime()
    high = fields.Float()
    low = fields.Float()
    money = fields.Float()
    name = fields.Str()
    open = fields.Float()
    time = fields.Integer()

class TestTableSchema(Schema):
    age = fields.Integer()
    name = fields.Str()
    time = fields.DateTime()

class WavedailySchema(Schema):
    ac = fields.Integer()
    arrow = fields.Str()
    code = fields.Str()
    dt = fields.DateTime()
    gw = fields.Str()

class WaveindexSchema(Schema):
    ac = fields.Integer()
    arrow = fields.Str()
    code = fields.Str()
    dt = fields.DateTime()
    duration = fields.Integer()
    gw = fields.Str()
    max = fields.Float()
    min = fields.Float()
    name = fields.Str()
    time = fields.Integer()

class WaverecordSchema(Schema):
    ac = fields.Integer()
    arrow = fields.Str()
    code = fields.Str()
    dt = fields.DateTime()
    gw = fields.Str()
    wv = fields.Str()

class WavestockSchema(Schema):
    ac = fields.Integer()
    arrow = fields.Str()
    code = fields.Str()
    dt = fields.DateTime()
    duration = fields.Integer()
    gw = fields.Str()
    max = fields.Float()
    min = fields.Float()
    name = fields.Str()
    time = fields.Integer()

class WeakSchema(Schema):
    ascrate = fields.Float()
    code = fields.Str()
    descrate = fields.Float()
    equalrate = fields.Float()
    name = fields.Str()
    time = fields.Str()
        


