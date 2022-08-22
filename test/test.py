def upgradeJunction(junctions):
        older_generation = []
        newer_generation = []
        for junction in junctions:
            if junction.split(' ')[1].isnumeric():
                newer_generation.append(junction)
            else:
                older_generation.append(junction)

        return sorted(older_generation, key=lambda x: str(x.split(' ')[1:]) + str(x.split(' ')[0])) + newer_generation

ordered = upgradeJunction(["ykc 82 01", "eo first qpx", "09z cat hamster", "06f 12 25 6", "az0 first qpx", "236 cat dog rabbit snake"])
print(ordered)