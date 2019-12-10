import shapefile
LATITUDE_INDEX = 3
LONGITUDE_INDEX = 4


def get_coordinates_matrix():
    shape = shapefile.Reader("shapefile/romania.shp")
    coordinates_matrix = []
    for i in range(len(shape.shapeRecords())):
        point = shape.shapeRecord(i)
        coordinates = [float(point.record[LATITUDE_INDEX]), float(point.record[LONGITUDE_INDEX])]
        coordinates_matrix.append(coordinates)
    return coordinates_matrix
