import requests

r = requests.get('https://api.github.com/repos/babu-thomas/ds-algos/contents//')
contents = r.json()
code_extensions = ('.py', '.cpp')
for file in contents:
    if file['name'].lower().endswith(code_extensions):
        text = {'name': file['name'], 'url': file['html_url']}
        print('### [{name}]({url})'.format(**text))