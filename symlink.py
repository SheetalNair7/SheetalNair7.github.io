import json, os, platform

with open("symlinks.json") as f:
    links = json.load(f)

system = platform.system()

for link, target in links.items():
    if system == "Windows":
        os.system(f'mklink /D "{link}" "{target}"')
    else:
        os.system(f'ln -s "{target}" "{link}"')

print("✨ All symlinks created!")
