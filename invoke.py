import requests
import time


def auth(user):
    if user == "guest":
        return 'Basic MjNiYzQ2YjEtNzFmNi00ZWQ1LThjNTQtODE2YWE0ZjhjNTAyOjEyM3pPM3haQ0xyTU42djJCS0sxZFhZRnBYbFBrY2NPRnFtMTJDZEFzTWdSVTRWck5aOWx5R1ZDR3VNREdJd1A='

    if user == "user1":
        return 'Basic MDhkMTc5ZWUtNzhlMy00ZTQ2LWJkZGMtZGFhMTlmYWQ3NjQzOmt0OHVOcmdIMkhidTVTc0lGZUtHd0xrdTNQUXVoVTZZSWpRRmE0SElhTkM1SlV2WXlpMHRrN0I0UUZ5Ymc2VEo='

    if user == "user2":
        return 'Basic MDliOTUwZGMtMWFiYy00YTk3LWEzZjItMzI3MWI3ZGNkMDIyOmxxNWVtZ05OVE1oYzJ0WkNnU0MwVWQwaU42Zng2dldjVE1LTjlraWhkQUhaNmVSTTF1eUhVdlBpNVRzYUhuQ2c='

    if user == "user3":
        return 'Basic NmM4Y2FiMTMtMTc2YS00OTJjLWE5MGMtMjI5MzJjNTljYmFmOkZ6a3FGc3Y4ZGgwRFVaNUJ1MUFHYUJtNm9Pa2h2c0lBcG5YWXA5QnBCSG01VktlY0w1QXF5Y3YzdEZhYWJYV2g='

    if user == "user4":
        return 'Basic MmY2OWFjNDEtMzA5NC00MzgwLWE0ODktOGYzMzYwNTU5ZDU4OkVKWnE5dXk2MFRzMTZIa1NMd0lRQmE1akhhaWZSNTV4QXJFUnNwNzRSZGJCTGk3QmRyVklzUjBUM0NxNm5Wdm0='

    if user == "user5":
        return 'Basic NGMzODAyZTgtNDdiOS00YmI2LWE3OWEtMzIwYTY3YzA2NDFmOnV5aER1Z2dLUTJNa2dUTURKSjM2Z3lpNWpkV0Z1Mmt3QXJhbUkyc2I1b2VkUUtuM2xtcXJ4QzA4RUJZcmNLWFU='


def invoker(id, user, action, data):

    headers = {
        'authorization': auth(user),
        'content-type': 'application/json',
    }

    params = (
        ('blocking', 'true'),
        ('result', 'true'),
    )

    data = data

    url = 'https://10.10.0.2/api/v1/namespaces/' + user + '/actions/' + action
    start = time.time()
    response = requests.post(url, headers=headers, params=params, data=data, verify=False)
    end = time.time()
    r_time = end - start

    print ("user = " + user + "\t" + "action = " + action + "\t" + "rTime = " + repr(r_time) + "\n")
