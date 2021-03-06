class GDAL_functions(object):

    def __init__():
        pass


def world2Pixel(geoMatrix, x, y):
    """
    Uses a gdal geomatrix (gdal.GetGeoTransform()) to calculate
    the pixel location of a geospatial 
    """
    ulX = geoMatrix[0]
    ulY = geoMatrix[3]
    xDist = geoMatrix[1]
    yDist = geoMatrix[5]
    rtnX = geoMatrix[2]
    rtnY = geoMatrix[4]
    pixel = int((x - ulX) / xDist)
    line = int((ulY - y) / xDist)
    
    return (pixel, line)

def Pixel2world(geoMatrix, row, col):
    """
    Uses a gdal geomatrix (gdal.GetGeoTransform()) to calculate
    the x,y location of a pixel location
    """

    ulX = geoMatrix[0]
    ulY = geoMatrix[3]
    xDist = geoMatrix[1]
    yDist = geoMatrix[5]
    rtnX = geoMatrix[2]
    rtnY = geoMatrix[4]
    x_coord = (ulX + (row * xDist))
    y_coord = (ulY - (col * xDist))

    return (x_coord, y_coord)