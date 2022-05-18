""" CSV """
requests_file = "wmts_csv_user.csv"

# test settings
layer = "2022_04_04T12_01_48Z_MAS_6_ORT_247557-Orthophoto"
gridName = "newGrids"
version = "1.0.0"
projection = "newGrids"
image_format = ".png"
users = 25

runTimeMin = 90
delayBetweenTileRequests = 100  # ms
delayBetweencapabilitiesRequests = 0  # ms

zMin = 0
zMax = 21
""" connection settings """
port = 80
layer_type = "wmts"  # ToDo: Fix it?
host = f""
path_builder = f"{layer_type}/{layer}/{projection}/TileMatrix/TileCol/TileRow{image_format}"

default_headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.100 Safari/537.36',
    'X-API-KEY': 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiIxMjM0NTY3ODkwIiwicmVzb3VyY2VUeXBlcyI6WyJyYXN0ZXIiLCJkZW0iLCJ2ZWN0b3IiLCIzZCJdLCJpYXQiOjE1MTYyMzkwMjJ9.kidhXiB3ihor7FfkaduJxpJQXFMJGVH9fH7WI6GLGM0'}


