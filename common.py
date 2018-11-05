# coding:utf8

import tushare as ts
import pandas as pd
import json

def sucess_response(result=None):
    result={'code':1,'data':result,'message':'success'}
    return json.dumps(result)

def fail_response(result=None):
    result={'code':-1,'data':result,'message':'failed'}
    return json.dumps(result)

def calIndexDelta(indexCode, indexCodeBase='399001.SZ'):
    ts.set_token('ded567c8b305a3ed36fb2b12b15ca0209a9d93f5880be42822234fa6')

    pro = ts.pro_api()
    df_base = pro.index_daily(ts_code=indexCodeBase)
    df_compare = pro.index_daily(ts_code=indexCode)

    df_base_slice = df_base[['trade_date', 'close']]
    df_compare_slice = df_compare[['trade_date', 'close']]

    weight_base = df_base_slice[['close']].apply(lambda x: x.max() + x.min())
    weight_compare = df_compare_slice[['close']].apply(lambda x: x.max() + x.min())
    factor = weight_base.values[0] / weight_compare.values[0]

    df_compare_slice = df_compare_slice.assign(closeMulti=lambda x: x.close * factor)
    dfNew = pd.merge(df_base_slice, df_compare_slice, how='inner', on='trade_date')
    dfNew.eval('delta=closeMulti-close_x', inplace=True)
    return dfNew[['trade_date', 'close_x', 'delta', 'close_y', 'closeMulti']].round(2).values.tolist()

def calStockDelta(code, indexCodeBase='399001.SZ'):
    ts.set_token('ded567c8b305a3ed36fb2b12b15ca0209a9d93f5880be42822234fa6')

    pro = ts.pro_api()
    df_base = pro.index_daily(ts_code=indexCodeBase)
    df_compare = ts.pro_bar(ts_code=code,pro_api=pro, adj='qfq')

    df_base_slice = df_base[['trade_date', 'close']]
    df_compare_slice = df_compare[['trade_date', 'close']]

    weight_base = df_base_slice[['close']].apply(lambda x: x.max() + x.min())
    weight_compare = df_compare_slice[['close']].apply(lambda x: x.max() + x.min())
    factor = weight_base.values[0] / weight_compare.values[0]

    df_compare_slice = df_compare_slice.assign(closeMulti=lambda x:  x.close * factor)
    dfNew = pd.merge(df_base_slice, df_compare_slice, how='inner', on='trade_date')
    dfNew.eval('delta=closeMulti-close_x', inplace=True)
    return dfNew[['trade_date', 'close_x', 'delta', 'close_y', 'closeMulti']].round(2).values.tolist()

def compareIndexDelta(indexs, dtStart='19800101', indexCodeBase='399001.SZ'):
    ts.set_token('ded567c8b305a3ed36fb2b12b15ca0209a9d93f5880be42822234fa6')
    indexNames = []
    indexList = indexs.split(',');
    pro = ts.pro_api()
    
    df_base = pro.index_daily(ts_code=indexCodeBase, start_date=dtStart)
    df_base_slice = df_base[['trade_date', 'close']]
    weight_base = df_base_slice[['close']].apply(lambda x: x.max() + x.min())
    
    for indexCode in indexList:
        df_compare = pro.index_daily(ts_code=indexCode, start_date=dtStart)
        df_compare_slice = df_compare[['trade_date', 'close']]
        weight_compare = df_compare_slice[['close']].apply(lambda x: x.max() + x.min())
        factor = weight_base.values[0] / weight_compare.values[0]
        df_compare_slice = df_compare_slice.assign(closeMulti=lambda x: x.close * factor)
        df_base_slice = pd.merge(df_base_slice, df_compare_slice, how='inner', on='trade_date')
        name = indexCode[7:] + indexCode[0:6]
        expr = '%s=closeMulti-close_x'%(name)
        indexNames.append(name)
        df_base_slice.eval(expr, inplace=True)
        exclude = ['close', 'close_y', 'closeMulti']
        df_base_slice = df_base_slice[df_base_slice.columns.difference(exclude)]
    columns = ['trade_date','close_x'] + indexNames
    df_base_slice = df_base_slice[columns]
    return df_base_slice.round(2).values.tolist()

def compareStockDelta(indexs, dtStart='19800101', indexCodeBase='399001.SZ'):
    ts.set_token('ded567c8b305a3ed36fb2b12b15ca0209a9d93f5880be42822234fa6')
    indexNames = []
    indexList = indexs.split(',');
    pro = ts.pro_api()
    
    df_base = pro.index_daily(ts_code=indexCodeBase, start_date=dtStart)
    df_base_slice = df_base[['trade_date', 'close']]
    weight_base = df_base_slice[['close']].apply(lambda x: x.max() + x.min())
    
    for indexCode in indexList:
        df_compare = ts.pro_bar(ts_code=indexCode,pro_api=pro, start_date=dtStart, adj='qfq')
        df_compare_slice = df_compare[['trade_date', 'close']]
        weight_compare = df_compare_slice[['close']].apply(lambda x: x.max() + x.min())
        factor = weight_base.values[0] / weight_compare.values[0]
        df_compare_slice = df_compare_slice.assign(closeMulti=lambda x: x.close * factor)
        df_base_slice = pd.merge(df_base_slice, df_compare_slice, how='inner', on='trade_date')
        name = indexCode[7:] + indexCode[0:6]
        expr = '%s=closeMulti-close_x'%(name)
        indexNames.append(name)
        df_base_slice.eval(expr, inplace=True)
        exclude = ['close', 'close_y', 'closeMulti']
        df_base_slice = df_base_slice[df_base_slice.columns.difference(exclude)]
    columns = ['trade_date','close_x'] + indexNames
    df_base_slice = df_base_slice[columns]
    return df_base_slice.round(2).values.tolist()
