#!/usr/bin/env python3

import json
import requests
import config

def get_profiles():
    token = config.git_key

    headers = {'Authorization':'Bearer '+token}
    query = '{ repository(owner: "paulienuh", name: "25DaysOfGiphiness") { collaborators(first: 20) {nodes {name login bio avatarUrl }}}}'
    r = requests.post('https://api.github.com/graphql', json.dumps({"query": query}), headers=headers)
    git_bios = r.json()["data"]["repository"]["collaborators"]["nodes"]
    return git_bios
