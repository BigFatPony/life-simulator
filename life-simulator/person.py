import datetime

from attribute import Attributes


class Person(object):
    default_value = 500  # 1000 is max
    number_of_activities = 2
    number_of_activities_weekends = 4
    stats = {
        Attributes.happiness: default_value,
        Attributes.excitement: default_value,
        Attributes.socialization: default_value,
        Attributes.confidence: default_value,
        Attributes.intelligence: default_value,
        Attributes.culture: default_value,
        Attributes.fitness: default_value,
        Attributes.soberity: default_value,
        Attributes.energy: default_value,
        Attributes.neatness: default_value,
        Attributes.charisma: default_value,
    }

    def __init__(self):
        self.time = Time()
        self.money = self.default_value

    def apply_activity(self, activity_cls):
        for attribute in activity_cls.influenced_attributes:
            self.stats[attribute] += activity_cls.influenced_attributes[attribute]
        # self.time.current_hour += activity_cls.duration


class Time(object):

    def __init__(self):
        self.start_date = datetime.date(2010, 1, 1)
        self.current_date = datetime.date(2010, 1, 1)
        self.end_date = datetime.date(2010, 2, 1)
        self.current_hour = datetime.time(12, 0, 0)

    def next_day(self):
        self.current_date += datetime.timedelta(days=1)

    def add_hours(self, hours):
        temp_hour = self.current_hour
        self.current_hour = datetime.timedelta(hours=hours)
        if self.current_hour < temp_hour:  # it means it's a new day
            self.next_day()

    def is_last_day(self):
        return self.current_date == self.end_date

