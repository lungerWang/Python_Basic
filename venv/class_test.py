class People(object):

    count = 0

    @classmethod
    def eat(cls):

        pass

    @classmethod
    def show_count(cls):
        print("there is %s" % cls.count)

    def __init__(self, name):
        self.name = name
        People.count += 1


people1 = People("Jan")
People.show_count()
people2 = People("Allen")
People.show_count()
