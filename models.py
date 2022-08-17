# simple request object


class VisitRequest:
    def __init__(self, apiKey, format="CSV"):
        self.apiKey = apiKey
        self.key = ""
        self.data = ""
        self.format = format
        self.headless = False

    def toJson(self):
        return {
            "apiKey": self.apiKey,
            "key": self.key,
            "data": self.data,
            "format": self.format,
            "headless": self.headless,
        }
