import os
import geopandas as gpd
from rasterstats import zonal_stats
import rasterio
import fiona
from rasterio.mask import mask

def ExtractROITiffByMask(tiff, roiFeatures, filename, nodata=0):  # 提取ROI区域
    roiData, roiTransform = mask(tiff, roiFeatures, nodata=nodata)
    roiMeta = tiff.meta.copy()
    roiMeta['nodata'] = nodata
    roiMeta['height'] = roiData.shape[1]
    roiMeta['width'] = roiData.shape[2]
    roiMeta['transform'] = roiTransform
    roiMeta['compress'] = 'lzw'
    roiTiff = rasterio.open(filename, 'w', **roiMeta)
    roiTiff.write(roiData)
    roiTiff.close()

if __name__ == '__main__':
    shp = fiona.open(f'{os.getcwd()}/Data/Subway/Subway_Stations_Buffer3km2019.shp', 'r')
    features = [feature['geometry'] for feature in shp]   # 地点站3km缓冲区的人们会乘坐地铁出行
    shp.close()

    for date in ['20180704', '20180707', '20190501', '20190505']:
        for hour in range(5, 24):
            # 地点站3km缓冲区的人们会乘坐地铁出行
            tiff = rasterio.open(f'{os.getcwd()}/Results/grid_move_{date}_{hour}.tif')
            ExtractROITiffByMask(tiff, features, f'{os.getcwd()}/Results/grid_move_{date}_{hour}_buffer3km.tif')
            tiff.close()

            # 统计每个地铁站每天每小时的出行需求
            geoms = zonal_stats(f'{os.getcwd()}/Data/Subway/Subway_Stations_Voronoi2019.shp', f'{os.getcwd()}/Results/grid_move_{date}_{hour}_buffer3km.tif', stats='sum', geojson_out=True)

            # 保存为shp文件
            stats_gdf = gpd.GeoDataFrame.from_features(geoms, crs='EPSG:4326')
            stats_gdf.to_file(f'{os.getcwd()}/Results/grid_demand_{date}_{hour}.shp')