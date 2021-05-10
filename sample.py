from osgeo import gdal, gdalconst, gdal_array

fd = open('sample.txt' ,'w' ,encoding='utf-8')

src = gdal.Open('./data/gm_el_v1.tif', gdalconst.GA_ReadOnly) # tifの読み込み (read only)
type(src) # "osgeo.gdal.Dataset"
b1 = src.GetRasterBand(1).ReadAsArray() # 第１バンド numpy array

for line in b1:
    dot=''
    for value in line:
        if(value == -9999):
            dot = dot + '0'
        else:
            dot = dot + '1'
    fd.write(dot+'\n')

print("水平Pix：" ,src.RasterXSize) # 水平方向ピクセル数
print("垂直Pix：" ,src.RasterYSize) # 鉛直方向ピクセル数
print("バンド数：" ,src.RasterCount) # バンド数

b1 = src.GetRasterBand(1).GetMinimum()

dtid = src.GetRasterBand(1).DataType # 型番号 (ex: 6 -> numpy.float32)
print("型番号：" ,dtid)
print("型名　：" ,gdal_array.GDALTypeCodeToNumericTypeCode(dtid)) # 型番号 -> 型名 変換

# others...

print("GetNoDataValue：" ,src.GetRasterBand(1).GetNoDataValue())
print("GetMinimum：" ,src.GetRasterBand(1).GetMinimum())
print("GetMaximum：" ,src.GetRasterBand(1).GetMaximum())
print("GetScale：" ,src.GetRasterBand(1).GetScale())
print("GetUnitType：" ,src.GetRasterBand(1).GetUnitType())