import json

local_repos = """
[
  {
    "key": "local-repo-1",
    "packageType": "maven",
    "description": "Local Repository 1"
  }
]
"""

remote_repos = """
[
  {
    "key": "remote-repo-1",
    "packageType": "maven",
    "url": "https://repo1.maven.org/maven2",
    "description": "Remote Repository 1"
  }
]
"""

virtual_repos = """
[
  {
    "key": "virtual-repo-1",
    "packageType": "maven",
    "url": "https://repo.jfrog.org/artifactory/api/npm/npm-virtual"
  }
]
"""

remote_repos = json.loads(remote_repos)
local_repos = json.loads(local_repos)
virtual_repos = json.loads(virtual_repos)


target_file = "templates/configuration.yml"

## Initialize Configuration File
with open(target_file, "w") as f:
  print("", file=f, end="")

## Configure Local Repositories
with open(target_file, "a") as f:
  print("localRepositories:", file=f, end="")
  for i in local_repos:
      print(f"""
  { i['key'] }:
    type: {i['packageType']}
    description: {i['description']}
""", file=f, end="")
  print(file=f)

## Configure Remote Repositories
with open(target_file, "a") as f:
  print("remoteRepositories:", file=f, end="")
  for i in remote_repos:

      print(f"""
  { i['key'] }:
    type: {i['packageType']}
    url: {i['url']},
    description: {i['description']}
    proxy: artfiactory-proxy
    handleReleases: true
    handleSnapshots: true
    blockMismatchingMimeTypes: true
    listRemoteFolderItems: true
    xray:   
      enabled: false
    bower:
      bowerRegistryUrl: https://registry.bower.io
    nuget:
      downloadContextPath: api/v2/package 
        v3FeedUrl:"https://api.nuget.org/v3/index.json"
      feedContextPath: api/v2
    vcs:
      git:
        provider: github
        downloadUrl: https://github.com/
      type: git
""", file=f, end="")
  print(file=f)

## Configure Virtual Repositories
with open(target_file, "a") as f:
  print("virtualRepositories:", file=f, end="")
  for i in virtual_repos:
      print(f"""
  { i['key'] }:
    type: {i['packageType']}
    url: {i['url']},
""", file=f, end="")
  print(file=f)