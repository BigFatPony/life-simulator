from attribute import Attributes


class Activity(object):
    tiny_influence = 1
    small_influence = 5
    big_influence = 10
    influenced_attributes = {}
    duration = 4
    cost = 0


class Study(Activity):
    influenced_attributes = {
        Attributes.intelligence: Activity.small_influence,
        Attributes.confidence: Activity.small_influence,

        Attributes.energy: -Activity.small_influence,
        Attributes.fitness: -Activity.small_influence,
    }


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

class TakaAWalk(Activity):
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


class Activities(object):
    all = {
        "study": Study,
        "read": Read,
        "run": Run,
        "sleep": Sleep,
        "takeawalk": TakaAWalk,
        "gotogym": GoToGym
    }