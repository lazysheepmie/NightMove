# 基于移动手机大数据的北京夜间出行及地铁运营需求研究

## 摘要
随着城市化的发展，城市夜间经济蓬勃发展，并已成为推动城市经济发展的重要组成部分。另一方面，夜间经济的发展也造成了城市人群夜间出行的空间不均衡，为城市公共交通运营带来了挑战。然而，高时空精度的城市人群夜间出行需求空间分布数据往往难以获取。得益于GPS定位、移动通讯、物联网等空间感知技术的发展，海量个体移动时空轨迹数据的涌现为我们量化城市夜间出行需求的时空分布提供了新的观测数据和研究视角。本研究基于北京市大规模个体粒度的移动手机时空大数据，对工作日和周末、节假日和非节假日北京市不同时刻的出行需求时空分布模式进行了研究。通过时空分布，本研究揭示了北京工作日和周末、节假日和非节假日不同日期城市夜间出行需求的热点区域、高峰时段等时空分异特征。本研究进一步结合北京市地铁站点数据，利用缓冲区分区、泰森多边形、区域统计等空间分析方法，对北京市地铁站点在夜间的客流承载能力进行了评估，并发现由于夜间经济的发展，存在部分地铁站点承载能力不足的现象。本研究基于移动手机时空大数据，提供了一种实时动态感知城市出行需求空间分布的方法，不仅为城市轨道交通运营优化（特别是针对夜间出行）提供了重要依据，也为城市夜间商业活动的发展和规划提供了一定的参考。

## 数据
- 出行需求数据Move：分别记录了20180704，20180707，20190501，20190505四天每一小时从北京市任一0.01°×0.01°地理网格单元(WGS84坐标系)内出发的人数和出行数。文件以日期命名，每个文件包括四个字段。date代表日期；sHour代表出发时刻（统计到小时）；slatindex为地理网格单元纬度索引，该索引除以100再加上0.005°即为该地理网格单元的中心点坐标纬度；slonindex为地理网格单元经度索引，该索引除以100再加上0.005°即为该地理网格单元的中心点坐标经度；pnum代表这一小时从该地理网格单元出发的总人数；tnum代表这一小时从该地理网格单元出发的总出行数。
- 地铁数据Subway：Subway2019记录了北京市2019年所有地铁站点位置坐标(WGS84坐标系)，其中 uid代表地铁站点ID；name代表地铁站点名称；line_name代表地铁站点所属地铁线路；lat为地铁站点位置坐标纬度；lon为地铁站点位置坐标经度；area为地铁站点所属行政区划。Subway_Stations2019.shp为地铁站点的矢量点Shapefile文件；Subway_Stations_Voronoi2019.shp是地铁站点的Voronoi图，矢量多边形Shapefile文件；Subway_Stations_Buffer3km2019.shp是地铁站点的3km缓冲区，矢量多边形Shapefile文件。
- 北京市行政边界Beijing：矢量Shapefile文件(WGS84坐标系)。

## 代码
- 1GridAvgMove：北京市每个0.01°×0.01°地理网格单元平均天出行次数。
- 2HourMove：每天每小时出行人数变化曲线
- 3HourGridMove：北京市每个0.01°×0.01°地理网格单元每天每小时出行人数
- 4Subway：每天每小时每个地铁站点的Voronoi图及乘坐该站点地铁的出行人数。