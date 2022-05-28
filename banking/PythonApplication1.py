class Date:
    layout = "{:2}:{:2} {:2}.{:2}.{:4}"

    def __init__(self, day, month, year, hour = "--", minute = ""):
        pass

class Row:
    #actor -> sender/reciever
    def __init__(self, id, actor, amount, purpose, time):
        #int
        self._ID = id
        #str
        self._actor = str(actor)
        #int
        self._amount = int(amount)
        #str
        self._purpose = purpose
