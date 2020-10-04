from pypresence import Presence

def connectPresence(clientId):
    RPC = Presence(clientId)
    RPC.connect()

    return RPC

def updatePresence(state = None, details = None, start = None,
large_image = None, large_text = None, small_image = None, small_text = None):
    RPC.update(
        state = state,
        details = details,
        start = start,
        large_image = large_image,
        large_text = large_text,
        small_image = small_image,
        small_text = small_text
        )

RPC = connectPresence("757909870258159646")
updatePresence(details = "11", state = None, start = None, large_image = None, large_text = "111", small_image = None, small_text = None)
