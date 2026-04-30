class Phone:
    def __init__(self, vendor, name, codename, support):
        self.name = name
        self.vendor = vendor
        self.codename = codename
        self.support = support

    def __str__(self):
        return f"{self.vendor} {self.name} {self.codename} {self.support}"
