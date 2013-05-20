lines = open("users.txt").readlines()

for line in lines:
    name, user, univ, topic = line.strip().split("\t")

    print "%s\t%s\t%s\t%s" % (name, univ, topic, user)
