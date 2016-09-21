from activity import Activity
from life_simulator.person.attribute import Attributes


class Study(Activity):
    influenced_attributes = {
        Attributes.intelligence: Activity.small_influence,
        Attributes.confidence: Activity.small_influence,

        Attributes.energy: -Activity.small_influence,
        Attributes.fitness: -Activity.small_influence,
    }
