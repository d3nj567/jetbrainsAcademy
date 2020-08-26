def tallest_people(**people):

    for key in sorted(people.keys()):
        if people[key] == max(people.values()):
            print(key, ':', people[key])
