from pypresence import Presence
import time

def connectPresence(clientId):
    RPC = Presence(clientId)
    RPC.connect()

    return RPC

def updatePresence(
    clientId,
    state = None,
    details = None,
    large_image = None,
    large_text = "Haruka v1.0.0b",
    small_image = None,
    small_text = None,
    start = None
    ):
    RPC = connectPresence(clientId)
    RPC.update(
        state = state,
        details = details,
        start = start,
        large_image = large_image,
        large_text = large_text,
        small_image = small_image,
        small_text = small_text
        )

    return RPC

def stopPresence():
    RPC.clear()

