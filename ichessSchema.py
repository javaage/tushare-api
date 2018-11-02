from marshmallow import Schema, fields

class AllstockSchema(Schema):
    id = fields.Integer()
    code = fields.Str()
    name = fields.Str()
    py = fields.Str()


class AttendSchema(Schema):
    id = fields.Integer()
    ascrate = fields.Float()
    code = fields.Str()
    descrate = fields.Float()
    equalrate = fields.Float()
    name = fields.Str()
    time = fields.Str()


class BkrecordSchema(Schema):
    id = fields.Integer()
    code = fields.Str()
    date = fields.DateTime()
    increase = fields.Float()
    name = fields.Str()
    time = fields.Str()


class CandRateSchema(Schema):
    id = fields.Integer()
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
    id = fields.Integer()
    code = fields.Str()
    content = fields.Str()
    name = fields.Str()
    type = fields.Str()


class Collect(Schema):
    id = fields.Integer()
    code = fields.Str()
    date = fields.DateTime()
    flag = fields.Integer()
    name = fields.Str()


class Crecord(Schema):
    id = fields.Integer()
    code = fields.Str()
    date = fields.DateTime()
    increase = fields.Float()
    name = fields.Str()
    time = fields.Str()

class Daily(Schema):
    id = fields.Integer()
    clmn = fields.Float()
    code = fields.Str()
    current = fields.Float()
    date = fields.DateTime()
    high = fields.Float()
    low = fields.Float()
    open = fields.Float()

class DailyRateSchema(Schema):
    id = fields.Integer()
    a = fields.Float()
    b = fields.Float()
    code = fields.Str()
    date = fields.DateTime()
    r = fields.Float()

class DirectorSchema(Schema):
    id = fields.Integer()
    arrow = fields.Str()
    code = fields.Str()
    level = fields.Integer()
    name = fields.Str()
    price = fields.Float()
    time = fields.Str()
    total = fields.Integer()
    type = fields.Str()

class HistorySchema(Schema):
    id = fields.Integer()
    ftime = fields.Str()
    id = fields.Str()
    ltime = fields.Str()
    record = fields.Str()
    type = fields.Str()

class HolderSchema(Schema):
    id = fields.Integer()
    ascrate = fields.Float()
    code = fields.Str()
    descrate = fields.Float()
    equalrate = fields.Float()
    name = fields.Str()
    time = fields.Str()

class IchessTestSchema(Schema):
    id = fields.Integer()
    age = fields.Integer()
    name = fields.Str()

class IndexrecordSchema(Schema):
    id = fields.Integer()
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
    id = fields.Integer()
    code = fields.Str()
    create_date = fields.Str()
    flag = fields.Integer()
    name = fields.Str()
    opt = fields.Str()
    type = fields.Str()
    value = fields.Float()

class MessageSchema(Schema):
    id = fields.Integer()
    code = fields.Str()
    flag = fields.Integer()
    message = fields.Str()
    name = fields.Str()
    time = fields.Str()

class SignSchema(Schema):
    id = fields.Integer()
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
    id = fields.Integer()
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
    id = fields.Integer()
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
    id = fields.Integer()
    age = fields.Integer()
    name = fields.Str()
    time = fields.DateTime()

class WavedailySchema(Schema):
    id = fields.Integer()
    ac = fields.Integer()
    arrow = fields.Str()
    code = fields.Str()
    dt = fields.DateTime()
    gw = fields.Str()

class WaveindexSchema(Schema):
    id = fields.Integer()
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
    id = fields.Integer()
    ac = fields.Integer()
    arrow = fields.Str()
    code = fields.Str()
    dt = fields.DateTime()
    gw = fields.Str()
    wv = fields.Str()

class WavestockSchema(Schema):
    id = fields.Integer()
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
    id = fields.Integer()
    ascrate = fields.Float()
    code = fields.Str()
    descrate = fields.Float()
    equalrate = fields.Float()
    name = fields.Str()
    time = fields.Str()
        


