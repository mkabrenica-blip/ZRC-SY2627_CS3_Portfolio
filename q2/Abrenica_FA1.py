class Publication:
    def __init__(self, __title, __author):
        self.title = __title
        self.author = __author

    def get_title(self):
        return self.title

    def get_author(self):
        return self.author

    def set_title(self, title):
        self.title = title

    def set_author(self, author):
        self.author = author

    def display_info(self):
        print("Title:", self.title)
        print("Author:", self.author)


class Book(Publication):
    def __init__(self, __title, __author, number_of_pages: int):
        super().__init__(__title, __author)
        self.number_pages = number_of_pages

    def get_number_pages(self):
        return self.number_pages

    def set_number_pages(self, number_pages):
        if number_pages <= 0:
            print("The number of pages must be positive")
        else:
            self.number_pages = number_pages

    def display_info(self):
        super().display_info()
        print("Number of Pages:", self.number_pages)


class Magazine(Publication):
    def __init__(self, __title, __author, issue_number):
        super().__init__(__title, __author)
        self.issue_number = issue_number

    def get_issue_number(self):
        return self.issue_number

    def set_issue_number(self, issue_number):
        if issue_number <= 0:
            print("The issue number must be positive")
        else:
            self.issue_number = issue_number

    def display_info(self):
        super().display_info()
        print("Issue Number:", self.issue_number)


pub1 = Publication("pub1", "vince")
pub2 = Publication("pub2", "vince2")

book1 = Book("book1", "myke", 143)
book2 = Book("book2", "myke2", 6767)

mag1 = Magazine("mag1", "calex", 1)
mag2 = Magazine("mag2", "calex2", 67)


print("Public Information:")
pub1.display_info()
pub2.display_info()

print("\nBook Information:")
book1.set_number_pages(-100)
book1.display_info()

book2.set_number_pages(1000)
book2.display_info()

print("\nMagazine Information:")
mag1.set_issue_number(-1)
mag1.display_info()
mag2.display_info()