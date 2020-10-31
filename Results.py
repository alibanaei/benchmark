import couchdb

f = open("env.txt", "r")
env = dict()
for line in f:
    word = line.split("=")
    env[word[0]] = word[1]

user = env["user"]
password = env["password"]
ip = env["IP"]
couchserver = couchdb.Server("http://%s:%s@%s" % (user, password, ip))

activation = couchserver["whisk_local_activations"]
logging = couchserver["logging"]

f = open("results.txt", "a")

f.write("enterTime" + " , " + "exitTime" + " , " + "qsize" + " , " + "queueWaitTime" + " , " + "totalWaitTime" + " , " + "duration" + "\n")

for id in logging:
    doc = logging[id]

    enterTime = int(doc["start"])
    exitTime = int(doc["end"])
    qsize = int(doc["queueSize"])
    queueWaitTime = exitTime - enterTime

    active_id = doc["namespace"] + "/" + id
    if active_id in activation:
        waitTime = 0
        annotations = activation[active_id]["annotations"]
        for item in annotations:
            if item["key"] == "waitTime":
                waitTime = int(item["value"])
        duration = int(activation[active_id]["duration"])

        f.write(repr(enterTime) + " , " + repr(exitTime) + " , " + repr(qsize) + " , " + repr(queueWaitTime) + " , " + repr(waitTime) + " , " + repr(duration) + "\n")

    else:
        del logging[doc.id]

f.close()
