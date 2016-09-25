class Attributes(object):
    happiness = "happiness"
    excitement = "excitement"
    socialization = "socialization"
    confidence = "confidence"
    intelligence = "intelligence"
    culture = "culture"
    fitness = "fitness"
    soberity = "soberity"
    energy = "energy"
    neatness = "neatness"
    charisma = "charisma"


class Activity(object):
    tiny_influence = 1
    small_influence = 5
    big_influence = 10
    influenced_attributes = {}
    duration = 4
    cost = 0


class Read(Activity):

    influenced_attributes = {
        Attributes.intelligence: Activity.small_influence,
        Attributes.culture: Activity.small_influence,

        Attributes.socialization: -Activity.small_influence,
        Attributes.fitness: -Activity.small_influence,
    }


class Run(Activity):
    influenced_attributes = {
        Attributes.fitness: Activity.big_influence,
        Attributes.confidence: Activity.small_influence,
        Attributes.energy: Activity.small_influence,

        Attributes.socialization: -Activity.tiny_influence,
        Attributes.neatness: -Activity.small_influence,
    }


class Sleep(Activity):
    influenced_attributes = {
        Attributes.energy: Activity.big_influence
    }


class TakeAWalk(Activity):
    influenced_attributes = {
        Attributes.fitness: Activity.tiny_influence,
        Attributes.energy: Activity.small_influence,

        Attributes.excitement: -Activity.tiny_influence
    }


class GoToGym(Activity):
    influenced_attributes = {
        Attributes.energy: Activity.small_influence,
        Attributes.fitness: Activity.small_influence,

        Attributes.neatness: -Activity.tiny_influence
    }


class Study(Activity):  # TODO
    influenced_attributes = {
        Attributes.intelligence: Activity.small_influence,
        Attributes.confidence: Activity.small_influence,

        Attributes.energy: -Activity.small_influence,
        Attributes.fitness: -Activity.small_influence,
    }


class Job(Activity):  # TODO

    def __init__(self):
        self.duration = 8
        self.drive = 1

    pass  # TODO


class Meet(Activity):  # TODO
    pass


class Shopping(Activity):  # TODO
    pass


def activities():
    return {
        "read": Read,
        "run": Run,
        "sleep": Sleep,
        "takeAWalk": TakeAWalk,
        "goToGym": GoToGym,
        "study": Study,
        "meet": Meet,
        "job": Job,
        "shopping": Shopping
    }
