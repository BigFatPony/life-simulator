
from activity.activity import Activity
from person.person import Person


def main():
    player = Person()
    while not player.time.is_last_day():
        player.time.next_day()
        inp = raw_input()
        try:
            player.apply_activity(Activity.activities()[inp])
        except KeyError:
            print "you morron pick one of these ", Activity.activities()[inp]

        print player.stats
        print player.time.current_date


if __name__ == "__main__":
    main()