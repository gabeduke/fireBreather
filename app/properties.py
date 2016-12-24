from enum import Enum


# # GET data # #
wio_url = "https://us.wio.seeed.io"
wio1_token = "?access_token=6da94989e6da2106dc7f8d569cc52a3c"

# # Nodes # #
wio_moistureNode = "/v1/node/GroveMoistureA0/moisture"
wio_humidityNode = "/v1/node/GroveTempHumD0/humidity"
wio_tempNode = "/v1/node/GroveTempHumD0/temperature_f"
wio_airQuality = "/v1/node/GroveAirqualityA0/quality"


class NodeProperties(Enum):
    moisture = wio_moistureNode
    humidity = wio_humidityNode
    fahrenheit_degree = wio_tempNode
    airQuality = wio_airQuality
