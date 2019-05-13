from github import Github

g = Github("BaseMax", "*******************************************")

username = raw_input("Enter a github username : ")

user = g.get_user(username)
print( user.name )
print( user.email )
