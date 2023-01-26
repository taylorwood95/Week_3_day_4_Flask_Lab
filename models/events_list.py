from models.event import Event
from datetime import datetime

event1 = Event(datetime, "Party time ", 25, "party room", "Party")
event2 = Event(datetime, "Wedding", 100, "Main room", "Big Wedding")
events = [event1, event2]