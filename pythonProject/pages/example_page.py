class ExamplePage:
    def __init__(self, page):
        self.page = page
        self.url = "https://example.com"
        self.title = "Example Domain"

    def navigate(self):
        self.page.goto(self.url)

    def is_title_correct(self):
        return self.title in self.page.title()
