class News():
    def __init__(self, title, url, time) -> None:
        self._title = title
        self._url = url
        self._time = time

    @property
    def title(self):
        return self._title
    
    @property
    def url(self):
        return self._url
    
    @property
    def time(self):
        return self._time
    
    def __str__(self) -> str:
        return f"""## {self.title}\n{self.url}\n### {self.time}
        """