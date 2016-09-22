import datetime


class Person(object):

    def __init__(self, attributes):
        default_value = 500  # TODO: 1000 is max
        self.time = Time()
        self.money = default_value  # TODO: money
        self.attributes = attributes
        self.stats = {
            attributes.happiness: default_value,
            attributes.excitement: default_value,
            attributes.socialization: default_value,
            attributes.confidence: default_value,
            attributes.intelligence: default_value,
            attributes.culture: default_value,
            attributes.fitness: default_value,
            attributes.soberity: default_value,
            attributes.energy: default_value,
            attributes.neatness: default_value,
            attributes.charisma: default_value,
        }

    def apply_activity(self, activity_cls):
        for act, value in activity_cls.influenced_attributes.items():
            self.stats[act] += value
        self.time.add_hours(activity_cls.duration)


class Time(object):

    def __init__(self):
        self.start_date = datetime.datetime(2010, 1, 1, 0, 0, 0)
        self.current_date = datetime.datetime(2010, 1, 1, 0, 0, 0)
        self.end_date = datetime.datetime(2010, 2, 1, 0, 0, 0)

    def next_day(self): # TODO: remove
        self.current_date += datetime.timedelta(days=1)

    def add_hours(self, hours):
        delta = datetime.timedelta(hours=hours)
        self.current_date = self.current_date + delta

    def is_last_day(self):
        return self.current_date == self.end_date

