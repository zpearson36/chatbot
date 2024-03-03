import json
import requests

from pprint import pprint

class RedditComment():
    
    def __init__(self, comment, depth=0):
        self.replies = []
        temp_comment = comment["body"].split('\n')
        self.comment = ""
        print(depth)
        for index, line in enumerate(temp_comment):
            if(line == ""): continue
            tmp_str = ""
            tmp_str = '   ' * depth if index else ' - ' * depth
            self.comment += tmp_str + line + '\n'

        if(comment["replies"] != ""):
            for index, reply in enumerate(comment["replies"]["data"]["children"]):
                if('body' in comment["replies"]["data"]["children"][index]["data"].keys()):
                    self.add_reply(RedditComment(comment["replies"]["data"]["children"][index]["data"], depth=depth+1))

    def add_reply(self, reply):
        self.replies.append(reply)

    def print_comments(self):
        print(self.comment, end="")
        for reply in self.replies:
            reply.print_comments()

    def __str__(self):
        return self.comment

def reply_depth(comment, responses):
    if('body' not in comment.keys()): return
    responses.append(comment["body"])
    reply_depth(comment["replies"]["data"]["children"][0]["data"], responses)
    return responses

def get_comments():
    r = requests.get('https://www.reddit.com/r/Music/comments/1b0d3j3/i_just_heard_parabola_by_tool_and_it_blew_me_away.json', headers={'User-agent': 'ActuallyABot'})
    with open(".ignnore/temp", 'w') as f:
        f.write(r.text)

if __name__ == "__main__":
    with open(".ignore/temp") as f:
        r = f.read()
        json_obj = json.loads(r)
        comment_thread = []
        for index, comment in enumerate(json_obj[1]["data"]["children"]):
            if('body' in json_obj[1]["data"]["children"][index]["data"].keys()):
                comment_thread.append(RedditComment(json_obj[1]["data"]["children"][index]["data"]))

    for comment in comment_thread:
        print(comment)
