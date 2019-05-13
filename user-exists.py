from github import Github

g = Github("BaseMax", "*******************************************")

username = raw_input("Enter a github username : ")

try:
	user = g.get_user(username)
	print( True )
except:
	print( False )
