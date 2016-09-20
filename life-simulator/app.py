import person

from activity import Activities


def main():
    player = person.Person()
    while not player.time.is_last_day():
        player.time.next_day()
        inp = raw_input()
        try:
            player.apply_activity(Activities.all[inp])
        except KeyError:
            print "you morron pick one of these ", Activities.all.keys()

        print player.stats
        print player.time.current_date

main()