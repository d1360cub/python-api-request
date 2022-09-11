import requests

response = requests.get("https://api.github.com/users/d1360cub/repos")
my_projects = response.json()

for project in my_projects:
  print(f"Project name: {project['name']}\nProject url: {project['html_url']}\n")