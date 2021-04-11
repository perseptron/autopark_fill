class DictSearch:
    def __init__(self):
        self.data = {}

    def __add(self, key):
        global id
        last = self.__get_last()
        if last:
            id = self.get_id(last)
        else:
            id = 0
        self.data[key] = id +1

    def __get_last(self):
        if len(list(self.data)) > 0:
            return list(self.data)[-1]
        else:
            return None

    def get_id(self, key):
        val = self.data.get(key)
        if val:
            return val
        self.__add(key)
        return -self.get_id(key)