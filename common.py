# coding:utf8

import tushare as ts
import pandas as pd

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

    return dfNew[['trade_date', 'close_x', 'delta', 'close_y']].round(2).values.tolist()

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
    return dfNew[['trade_date', 'close_x', 'delta', 'close_y']].round(2).values.tolist()

indexList = [['000001.SH','上证综指'],['000002.SH','上证A指'],['000003.SH','上证B指'],['000004.SH','上证工业类指数'],['000005.SH','上证商业类指数'],['000006.SH','上证房地产指数'],['000007.SH','上证公用事业股指数'],['000008.SH','上证综合股指数'],['000009.SH','上证380'],['000010.SH','上证180'],['000015.SH','上证红利'],['000016.SH','上证50'],['000017.SH','新综指'],['000018.SH','180金融'],['000019.SH','治理指数'],['000020.SH','中型综指'],['000021.SH','180治理'],['000025.SH','180基建'],['000026.SH','180资源'],['000027.SH','180运输'],['000028.SH','180成长'],['000029.SH','180价值'],['000030.SH','180R成长'],['000031.SH','180R价值'],['000032.SH','上证能源'],['000033.SH','上证材料'],['000034.SH','上证工业'],['000035.SH','上证可选'],['000036.SH','上证消费'],['000037.SH','上证医药'],['000038.SH','上证金融'],['000039.SH','上证信息'],['000040.SH','上证电信'],['000041.SH','上证公用'],['000042.SH','上证央企'],['000043.SH','超大盘'],['000044.SH','上证中盘'],['000045.SH','上证小盘'],['000046.SH','上证中小'],['000047.SH','上证全指'],['000048.SH','责任指数'],['000049.SH','上证民企'],['000050.SH','50等权'],['000051.SH','180等权'],['000052.SH','50基本'],['000053.SH','180基本'],['000054.SH','上证海外'],['000055.SH','上证地企'],['000056.SH','上证国企'],['000057.SH','全指成长'],['000058.SH','全指价值'],['000059.SH','全R成长'],['000060.SH','全R价值'],['000062.SH','上证沪企'],['000063.SH','上证周期'],['000064.SH','非周期'],['000065.SH','上证龙头'],['000066.SH','上证商品'],['000067.SH','上证新兴'],['000068.SH','上证资源'],['000069.SH','消费80'],['000070.SH','能源等权'],['000071.SH','材料等权'],['000072.SH','工业等权'],['000073.SH','可选等权'],['000074.SH','消费等权'],['000075.SH','医药等权'],['000076.SH','金融等权'],['000077.SH','信息等权'],['000078.SH','电信等权'],['000079.SH','公用等权'],['000090.SH','上证流通'],['000091.SH','沪财中小'],['000092.SH','资源50'],['000093.SH','180分层'],['000094.SH','上证上游'],['000095.SH','上证中游'],['000096.SH','上证下游'],['000097.SH','高端装备'],['000098.SH','上证F200'],['000099.SH','上证F300'],['000100.SH','上证F500'],['000102.SH','沪投资品'],['000103.SH','沪消费品'],['000104.SH','380能源'],['000105.SH','380材料'],['000106.SH','380工业'],['000107.SH','380可选'],['000108.SH','380消费'],['000109.SH','380医药'],['000110.SH','380金融'],['000111.SH','380信息'],['000112.SH','380电信'],['000113.SH','380公用'],['000114.SH','持续产业'],['000115.SH','380等权'],['000117.SH','380成长'],['000118.SH','380价值'],['000119.SH','380R成长'],['000120.SH','380R价值'],['000121.SH','医药主题'],['000122.SH','农业主题'],['000123.SH','上证180动态'],['000125.SH','上证180稳定'],['000126.SH','上证消费50'],['000128.SH','380基本'],['000129.SH','180波动'],['000130.SH','380波动'],['000131.SH','上证高新'],['000132.SH','上证100'],['000133.SH','上证150'],['000134.SH','上证银行'],['000135.SH','上证180高贝塔'],['000136.SH','上证180低贝塔'],['000137.SH','上证380高贝塔'],['000138.SH','上证380低贝塔'],['000141.SH','上证380动态'],['000142.SH','上证380稳定'],['000145.SH','优势资源'],['000146.SH','优势制造'],['000147.SH','优势消费'],['000148.SH','消费领先'],['000149.SH','上证180红利'],['000150.SH','上证380红利'],['000151.SH','上证国企红利'],['000152.SH','上证央企红利'],['000153.SH','上证民企红利'],['000155.SH','上证市值百强'],['000158.SH','上证环保'],['000159.SH','沪股通'],['000160.SH','沪新丝路'],['000802.SH','500沪市'],['000849.SH','300非银'],['000850.SH','300有色'],['000901.SH','小康指数'],['000970.SH','ESG.SH','40'],['000972.SH','300沪市'],['000976.SH','新华金牛'],['000999.SH','两岸三地'],['399001.SZ','深证成指'],['399002.SZ','深成指R'],['399003.SZ','深成B指'],['399004.SZ','深证100R'],['399005.SZ','中小板指'],['399006.SZ','创业板指'],['399007.SZ','深证300'],['399008.SZ','中小300'],['399009.SZ','深证200'],['399010.SZ','深证700'],['399011.SZ','深证1000'],['399012.SZ','创业300'],['399013.SZ','深市精选'],['399015.SZ','中小创新'],['399100.SZ','深证新综指'],['399101.SZ','中小板综'],['399102.SZ','创业板综'],['399106.SZ','深证综指'],['399107.SZ','深证A指'],['399108.SZ','深证B指'],['399231.SZ','农林指数'],['399232.SZ','采矿指数'],['399233.SZ','制造指数'],['399234.SZ','水电指数'],['399235.SZ','建筑指数'],['399236.SZ','批零指数'],['399237.SZ','运输指数'],['399238.SZ','餐饮指数'],['399239.SZ','IT指数'],['399240.SZ','金融指数'],['399241.SZ','地产指数'],['399242.SZ','商务指数'],['399243.SZ','科研指数'],['399244.SZ','公共指数'],['399248.SZ','文化指数'],['399249.SZ','综企指数'],['399300.SZ','沪深300'],['399303.SZ','国证2000'],['399310.SZ','国证50'],['399311.SZ','国证1000'],['399312.SZ','国证300'],['399313.SZ','巨潮100'],['399314.SZ','巨潮大盘'],['399315.SZ','巨潮中盘'],['399316.SZ','巨潮小盘'],['399317.SZ','国证A指'],['399318.SZ','国证B指'],['399319.SZ','资源优势'],['399320.SZ','国证服务'],['399321.SZ','国证红利'],['399322.SZ','国证治理'],['399324.SZ','深证红利'],['399326.SZ','成长40'],['399328.SZ','深证治理'],['399330.SZ','深证100'],['399332.SZ','深证创新'],['399333.SZ','中小板指R'],['399335.SZ','深证央企'],['399337.SZ','深证民营'],['399339.SZ','深证科技'],['399341.SZ','深证责任'],['399344.SZ','深证300R'],['399346.SZ','深证成长'],['399348.SZ','深证价值'],['399350.SZ','皖江30'],['399351.SZ','深圳报业指数'],['399352.SZ','深报综指'],['399353.SZ','国证物流'],['399354.SZ','分析师指数'],['399355.SZ','CBN长江'],['399356.SZ','CBN珠江'],['399357.SZ','CBN渤海'],['399358.SZ','泰达环保指数'],['399359.SZ','国证基建'],['399360.SZ','国证装备'],['399361.SZ','国证商业'],['399362.SZ','国证民营'],['399363.SZ','计算机指'],['399364.SZ','中金消费'],['399365.SZ','国证农业'],['399366.SZ','国证大宗'],['399367.SZ','巨潮地产'],['399368.SZ','国证军工'],['399369.SZ','CBN-兴全'],['399370.SZ','国证成长'],['399371.SZ','国证价值'],['399372.SZ','大盘成长'],['399373.SZ','大盘价值'],['399374.SZ','中盘成长'],['399375.SZ','中盘价值'],['399376.SZ','小盘成长'],['399377.SZ','小盘价值'],['399378.SZ','南方低碳'],['399381.SZ','1000能源'],['399382.SZ','1000材料'],['399383.SZ','1000工业'],['399384.SZ','1000可选'],['399385.SZ','1000消费'],['399386.SZ','1000医药'],['399387.SZ','1000金融'],['399388.SZ','1000信息'],['399389.SZ','国证通信'],['399390.SZ','1000公用'],['399391.SZ','投资时钟'],['399392.SZ','国证新兴'],['399393.SZ','国证地产'],['399394.SZ','国证医药'],['399395.SZ','国证有色'],['399396.SZ','国证食品'],['399397.SZ','OCT文化'],['399398.SZ','绩效指数'],['399399.SZ','中经GDP'],['399400.SZ','大中盘'],['399401.SZ','中小盘'],['399402.SZ','周期100'],['399403.SZ','防御100'],['399404.SZ','大盘低波'],['399405.SZ','大盘高贝'],['399406.SZ','中盘低波'],['399407.SZ','中盘高贝'],['399408.SZ','小盘低波'],['399409.SZ','小盘高贝'],['399410.SZ','苏州率先'],['399411.SZ','红利100'],['399412.SZ','国证新能'],['399415.SZ','I100'],['399416.SZ','I300'],['399417.SZ','新能源车'],['399418.SZ','国证国安'],['399419.SZ','国证高铁'],['399420.SZ','国证保证'],['399423.SZ','中关村50'],['399427.SZ','专利领先'],['399428.SZ','国证定增'],['399429.SZ','新丝路'],['399431.SZ','国证银行'],['399432.SZ','国证汽车'],['399433.SZ','国证交运'],['399434.SZ','国证传媒'],['399435.SZ','国证农牧'],['399436.SZ','国证煤炭'],['399437.SZ','国证证券'],['399438.SZ','国证电力'],['399439.SZ','国证油气'],['399440.SZ','国证钢铁'],['399441.SZ','生物医药'],['399550.SZ','央视50'],['399551.SZ','央视创新'],['399552.SZ','央视成长'],['399553.SZ','央视回报'],['399554.SZ','央视治理'],['399555.SZ','央视责任'],['399556.SZ','央视生态'],['399557.SZ','央视文化'],['399602.SZ','中小成长'],['399604.SZ','中小价值'],['399606.SZ','创业板指R'],['399608.SZ','科技100'],['399610.SZ','TMT50'],['399611.SZ','中创100R'],['399612.SZ','中创100'],['399613.SZ','深证能源'],['399614.SZ','深证材料'],['399615.SZ','深证工业'],['399616.SZ','深证可选'],['399617.SZ','深证消费'],['399618.SZ','深证医药'],['399619.SZ','深证金融'],['399620.SZ','深证信息'],['399621.SZ','深证电信'],['399622.SZ','深证公用'],['399623.SZ','中小基础'],['399624.SZ','中创400'],['399625.SZ','中创500'],['399626.SZ','中创500成长'],['399627.SZ','中创500价值'],['399628.SZ','700成长'],['399629.SZ','700价值'],['399630.SZ','1000成长'],['399631.SZ','1000价值'],['399632.SZ','深100EW'],['399633.SZ','深300EW'],['399634.SZ','中小板EW'],['399635.SZ','创业板EW'],['399636.SZ','深证装备'],['399637.SZ','深证地产'],['399638.SZ','深证环保'],['399639.SZ','深证大宗'],['399640.SZ','创业基础'],['399641.SZ','深证新兴'],['399642.SZ','中小新兴'],['399643.SZ','创业新兴'],['399644.SZ','深证时钟'],['399645.SZ','100低波'],['399646.SZ','深消费50'],['399647.SZ','深医药50'],['399648.SZ','深证GDP100'],['399649.SZ','中小板红利'],['399650.SZ','中小板治理'],['399651.SZ','中小板责任'],['399652.SZ','中创高新'],['399653.SZ','深证龙头'],['399654.SZ','深证文化'],['399655.SZ','深证绩效'],['399656.SZ','100绩效'],['399657.SZ','300绩效'],['399658.SZ','中小绩效'],['399659.SZ','深成指EW'],['399660.SZ','中创EW'],['399661.SZ','深证低波'],['399662.SZ','深证高贝'],['399663.SZ','中小低波'],['399664.SZ','中小高贝'],['399665.SZ','中创低波'],['399666.SZ','中创高贝'],['399667.SZ','创业板G'],['399668.SZ','创业板V'],['399669.SZ','深证农业'],['399670.SZ','深周期50'],['399671.SZ','深防御50'],['399672.SZ','深红利50'],['399673.SZ','创业板50'],['399674.SZ','深A医药'],['399675.SZ','深互联网'],['399676.SZ','深医药EW'],['399677.SZ','深互联EW'],['399678.SZ','深次新股'],['399679.SZ','深证200R'],['399701.SZ','深证F60'],['399702.SZ','深证F120'],['399703.SZ','深证F200'],['399704.SZ','深证上游'],['399705.SZ','深证中游'],['399706.SZ','深证下游'],['399802.SZ','500深市'],['399901.SZ','小康指数'],['399908.SZ','沪深300能源'],['399909.SZ','沪深300材料'],['399910.SZ','沪深300工业'],['399911.SZ','沪深300可选'],['399912.SZ','沪深300消费'],['399913.SZ','沪深300医药'],['399914.SZ','沪深300金融'],['399915.SZ','沪深300信息'],['399916.SZ','沪深300电信'],['399917.SZ','沪深300公用'],['399918.SZ','沪深300成长'],['399919.SZ','沪深300价值'],['399920.SZ','沪深300R成长'],['399925.SZ','基本面50'],['399927.SZ','央企100'],['399939.SZ','民企200'],['399941.SZ','新能源'],['399942.SZ','内地消费'],['399943.SZ','内地基建'],['399944.SZ','内地资源'],['399945.SZ','内地运输'],['399946.SZ','内地金融'],['399947.SZ','内地银行'],['399948.SZ','内地地产'],['399949.SZ','内地农业'],['399950.SZ','300基建'],['399951.SZ','300银行'],['399952.SZ','300地产'],['399954.SZ','地企100'],['399956.SZ','国企200'],['399957.SZ','300运输'],['399958.SZ','创业成长'],['399968.SZ','300周期'],['399969.SZ','300非周'],['399972.SZ','300深市'],['399977.SZ','内地低碳'],['399978.SZ','医药100'],['399979.SZ','大宗商品'],['399982.SZ','500等权']]