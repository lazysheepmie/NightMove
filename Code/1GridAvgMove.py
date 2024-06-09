import os
import numpy as np
import rasterio

def Points2Raster(points, filename):
    leftY, bottomX, rightY, topX = 115.4, 39.4, 117.6, 41.1
    pWidth, pHeight = 0.01, -0.01
    rRows, rCols = round((bottomX - topX) / pHeight), round((rightY - leftY) / pWidth)
    data = np.ones((rRows, rCols)) * -999   # -999表示nodata
    for (lat, lon) in points:
        xIdx = int((lat - topX) / pHeight)
        yIdx = int((lon - leftY) / pWidth)
        data[xIdx, yIdx] = points[(lat, lon)]
    transform = rasterio.transform.from_bounds(leftY, bottomX, rightY, topX, rCols, rRows)
    tiff = rasterio.open(filename, 'w', driver='GTiff', height=data.shape[0], width=data.shape[1],
                         count=1, dtype=data.dtype, crs='EPSG:4326', transform=transform, compress='lzw', nodata=-999)
    tiff.write(data, 1)
    tiff.close()

if __name__ == '__main__':
    gridVNums = {}   # 每个网格每天的平均出行次数，key为网格的经纬度索引，value为平均出行次数
    for date in ['20180704', '20180707', '20190501', '20190505']:
        fr = open(f'{os.getcwd()}/Data/Move/{date}.csv', 'r')
        fr.readline()
        while True:
            line = fr.readline()
            if not line:
                break
            items = line.split(',')
            date = items[0]
            sHour = int(items[1])   # 出发小时
            sLatIndex = int(items[2])   # 出发网格纬度索引，除以100+0.005得到纬度
            sLonIndex = int(items[3])   # 出发网格经度索引，除以100+0.005得到经度
            pNum = int(items[4])   # 从该网格出发的出行人数
            vNum = int(items[5])   # 从该网格出发的出行次数
            if (sLatIndex, sLonIndex) not in gridVNums:
                gridVNums[(sLatIndex, sLonIndex)] = 0
            gridVNums[(sLatIndex, sLonIndex)] += vNum
        fr.close()

    points = {}
    for (sLatIndex, sLonIndex) in gridVNums:
        lat = float(sLatIndex) / 100 + 0.005
        lon = float(sLonIndex) / 100 + 0.005
        points[(lat, lon)] = gridVNums[(sLatIndex, sLonIndex)] / 4    # 每个网格每天的平均出行次数，没有则视为0
    Points2Raster(points, f'{os.getcwd()}/Results/grid_average_move.eps')