import numpy as np
from osgeo import gdal, gdalconst, gdal_array

src = gdal.Open('/Users/takamotokeiji/data/geotiff/gm_el_v1.tif', gdalconst.GA_ReadOnly) # tifの読み込み (read only)
type(src) # "osgeo.gdal.Dataset"

src.RasterXSize # 水平方向ピクセル数
src.RasterYSize # 鉛直方向ピクセル数
src.RasterCount # バンド数

b1 = src.GetRasterBand(1).ReadAsArray() # 第１バンド numpy array

dtid = src.GetRasterBand(1).DataType # 型番号 (ex: 6 -> numpy.float32)
gdal_array.GDALTypeCodeToNumericTypeCode(dtid) # 型番号 -> 型名 変換

# others...

src.GetRasterBand(1).GetNoDataValue()
src.GetRasterBand(1).GetMinimum()
src.GetRasterBand(1).GetMaximum()
src.GetRasterBand(1).GetScale()
src.GetRasterBand(1).GetUnitType()