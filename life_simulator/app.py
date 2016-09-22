from person.person import Person
from activity.activity import Attributes, activities


def main():
    player = Person(Attributes)
    while not player.time.is_last_day():
        inp = input()
        try:
            print("it will take:", activities()[inp].duration, " ok?")
            ok = input()
            if ok != "n":
                player.apply_activity(activities()[inp])
        except KeyError:
            print("you morron pick one of these ", activities()[inp])

        print(player.stats)
        print(player.time.current_date)


if __name__ == "__main__":
    main()
