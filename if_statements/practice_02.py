db_username = "Admin"
db_password = "Password"

username = input ("Enter your username: ")
password = input ("Enter the Password:")

if username == db_username and password == db_password:
    print (" You loged in successfully!")
elif username == db_username and password != db_password:
    print ("Incorrect password!  Please try again.")
elif username != db_username and  password == db_password:
    print ("Incorrect username! please try again.")
else:    
    print ("wrong username or password!")

    # test, 
    # code on large laptop (forked from upstream, now after coding, need to push the update to the froked copy on github then send a PR to the original repo) but always before we do any
    # changes here at the forked copy we always wana make sure we sync with the upstream repo to avoid conflicts  here are the steps we follow to sync with the upstrean 
    # 1- git fetch upstream
    # 2- git checkout main
    # 3- git merge upstream/main
    # 4- git push origin main

    # Bonus: Automate This Process => Instead of typing all four commands every time, you can create a Git alias to update your fork in one step:
    # "git config --global alias.updatefork '!git fetch upstream && git checkout main && git merge upstream/main && git push origin main'""
    # Now you can type git updatefork to sync your fork with the upstream repo.

    # after the sync, you can add, commit and push your changes to your forked repo using the usual git commands.
    # After your changes are pushed, send a pull request to the original repo using the github website


    exit()    