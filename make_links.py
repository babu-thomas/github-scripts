# Get all source code files in a github repo and output them as markdown links.
# No error checking or other nice things. Also supports files in the repo root only for now.

import requests

r = requests.get('https://api.github.com/repos/babu-thomas/ds-algos/contents//')
contents = r.json()
code_extensions = ('.py', '.cpp')
for file in contents:
    if file['name'].lower().endswith(code_extensions):
        text = {'name': file['name'], 'url': file['html_url']}
        print('### [{name}]({url})'.format(**text))