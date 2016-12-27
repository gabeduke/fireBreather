from enum import Enum


# # GET data # #
wio_url = "https://us.wio.seeed.io/"
token = "ef371a81ba3722b602dbdabc1fa6b967"
wio_token = "?access_token=" + token

# # Nodes # #
wio_tempNode = "v1/node/GroveTempA0/temp"


class NodeProperties(Enum):
    temperature = wio_tempNode
