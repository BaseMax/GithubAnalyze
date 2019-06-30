from github import Github

g = Github("********_token_access_******")

repositories = g.search_repositories(query='search_here')
for repo in repositories:
	print(repo)

