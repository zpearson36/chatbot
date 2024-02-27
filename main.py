import json
import requests

from pprint import pprint

def reply_depth(comment, responses):
    if(comment["replies"].__class__ == str): return
    responses.append(comment["replies"]["data"]["children"][0]["data"]["body"])
    reply_depth(comment["replies"]["data"]["children"][0]["data"], responses)
    return responses

if __name__ == "__main__":
    #r = requests.get('https://www.reddit.com/r/Music/comments/1b0d3j3/i_just_heard_parabola_by_tool_and_it_blew_me_away.json')
    #json_obj = json.loads(r.text)
    #print(json.dumps(json_obj, indent=2))

    with open("temp") as f:
        r = f.read()
        json_obj = json.loads(r)
        pprint(reply_depth(json_obj[1]["data"]["children"][0]["data"], []))
