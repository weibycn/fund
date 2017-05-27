



---------------------------------------------------------------------------------
readme

一、fund-rank.py

(1)获取在一个时间段内，特定基金的增长率
(2)从所有基金中查询在一个时间段内，top50个增长率最高的基金，结果存到文件中。

fund-rank.py usage:
        python fund.py start-date end-date fund-code=none

        date format ****-**-**
                start-date must before end-date
        fund-code default none
                if not input, get top 20 funds from all more than 6400 funds
                else get that fund's rate of rise

        eg:     python fund-rank.py 2017-03-01 2017-03-25
        eg:     python fund-rank.py 2017-03-01 2017-03-25 377240


流程
(1)、获取基金列表
	如果存在文件 fundlist-*.txt 文件，则读取该文件
	如果该文件不存在 url获取列表 然后存文件
	
(2)、for循环查询基金净值
	为了简化处理 查询2次净值 只查询时间段开始和结束2天的净值
	
	累计净值处理
	
	将其放到合适位置 只存储前50个基金

二、avg-rank.py
对多个top50结果文件进行处理，计算平均排名并进行排序，结果存到文件中。

三、fund-zf.py
天天基金网可以获取基金排名 可以获取基金排名 可以获取基金排名
MD 不用计算 不用计算 不用计算 上面2个文件 留着吧 警示一下
获取近1月 近3月 近6月 近12个月的收益率最高的50个基金
计算平均排名并进行排序，结果存到文件中。


四、基金数据来源
需要获得3类数据，数据均来自天天基金网。
(1)基金列表
http://fund.eastmoney.com/js/fundcode_search.js
格式：["000001","HXCZ","华夏成长","混合型","HUAXIACHENGZHANG"]

(2)基金净值数据
http://fund.eastmoney.com/f10/F10DataApi.aspx?type=lsjz&code=377240
http://fund.eastmoney.com/f10/F10DataApi.aspx?type=lsjz&code=160220&page=1
http://fund.eastmoney.com/f10/F10DataApi.aspx?type=lsjz&code=160220&page=1&per=50
http://fund.eastmoney.com/f10/F10DataApi.aspx?type=lsjz&code=377240&page=1&per=20&sdate=2017-03-01&edate=2017-03-01

格式：var apidata={ content:"<table class='w782 comm lsjz'><thead><tr><th class='first'>净值日期</th><th>单位净值</th><th>累计净值</th><th>日增长率</th><th>申购状态</th><th>赎回状态</th><th class='tor last'>分红送配</th></tr></thead><tbody><tr><td>2017-03-01</td><td class='tor bold'>2.1090</td><td class='tor bold'>2.1090</td><td class='tor bold red'>0.29%</td><td>开放申购</td><td>开放赎回</td><td class='red unbold'></td></tr></tbody></table>",records:1,pages:1,curpage:1};

格式化以后：
净值日期	单位净值	累计净值	日增长率	申购状态	赎回状态	分红送配
2017-03-01	2.1090	2.1090			0.29%		开放申购	开放赎回	

(3)基金增幅排名
http://fund.eastmoney.com/data/rankhandler.aspx?op=ph&dt=kf&ft=gp&rs=&gs=0&sc=zzf&st=desc&sd=2016-03-29&ed=2017-03-29&qdii=&tabSubtype=,,,,,&pi=1&pn=50&dx=1&v=0.6370068000914493
ft： fund type类型 所有-all 股票型-gp 混合型-hh 债券型-zq 指数型-zs 保本型-bb QDII-qdii LOF-lof


更多筛选
http://fund.eastmoney.com/data/rankhandler.aspx?op=ph&dt=kf&ft=all&rs=3yzf,50&gs=0&sc=3yzf&st=desc&sd=2016-03-29&ed=2017-03-29&qdii=&tabSubtype=,,,,,&pi=1&pn=50&dx=1&v=0.013834315347261095
http://fund.eastmoney.com/data/rankhandler.aspx?op=ph&dt=kf&ft=all&rs=6yzf,20&gs=0&sc=6yzf&st=desc&sd=2016-03-29&ed=2017-03-29&qdii=&tabSubtype=,,,,,&pi=1&pn=50&dx=1&v=0.5992681832027366
http://fund.eastmoney.com/data/rankhandler.aspx?op=ph&dt=kf&ft=all&rs=1nzf,20&gs=0&sc=1nzf&st=desc&sd=2016-03-29&ed=2017-03-29&qdii=&tabSubtype=,,,,,&pi=1&pn=50&dx=1&v=0.6093838416906625

rs=3yzf,50 近3月涨幅排名前50
rs=1nzf,20 近1年涨幅排名前20

五、测试情况

python fund.py 2016-01-21 2017-03-24
截至2017.03.27，共有6400多个基金。全部跑一遍，用了半小时。各地网速不同，用时有差异。
排序	编码				名称										类型		2016-01-21	2017-03-24	净增长	增长率
1		502022	国金上证50分级B							分级杠杆		0.0118		0.4511			0.44		3728.81%
2		150296	南方中证国有企业改革分级B		分级杠杆		0.0290		0.4494			0.42		1448.28%
3		150294	南方中证高铁产业指数分级B		分级杠杆		0.0404		0.5472			0.51		1262.38%
4		502008	易方达国企改革指数分级B			分级杠杆		0.0562		0.5280			0.47		836.3%
5		502015	长盛中证申万一带一路分级B		分级杠杆		0.0510		0.3945			0.34		666.67%



python fund-zf.py
1	161725	招商中证白酒指数分级	股票指数	19	4	3	4	7.5
2	002230	华夏大中华混合(QDII)	QDII	8	7	21	6	10.5
3	110022	易方达消费行业	股票型	30	11	10	9	15.0
4	002534	华安稳固收益债券A	债券型	100	1	2	3	26.5
5	160632	鹏华酒分级	股票指数	100	26	11	11	37.0
6	180012	银华富裕主题混合	混合型	100	23	20	10	38.25
7	050015	博时大中华亚太精选股票	QDII	100	9	27	20	39.0
8	000988	嘉实全球互联网股票人民币	QDII	25	21	100	24	42.5
9	050018	博时行业轮动混合	混合型	27	18	100	25	42.5
10	110011	易方达中小盘混合	混合型	38	19	100	18	43.75


---------------------------------------------------------------------------------
ChangeLog:
V1.0  2017.03.27
