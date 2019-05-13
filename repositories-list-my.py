from github import Github

g = Github("BaseMax", "*******************************************")

for repo in g.get_user().get_repos():
	print(repo.name)
