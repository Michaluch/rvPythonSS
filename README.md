rvPythonSS
==========

git clone - get repository from server

git checkout [branch_name] - switch branch

git pull - sync local branch with remote one

git add [path/to/file] - prepare local changes in selected file to commit

git commit -m "commit message" - commit staged files with "commit message"

git push origin [branch_name] - push local branch to remote one




Please follow the instruction:
=

Clone remote repository

Checkout to the appropriate branch

Don't forget to pull branch one time per day at least 

Commit your changes into the appropriate folder in the repository


Generate SSH KEY on Linux
=========================
Into terminal run command for generate SSH KEY:

    ssh-keygen -t rsa -C "your_email@example.com"
  
    ssh-add id_rsa
  
Copy SSH KEY
============
Install xclip for copy SSH KEY:

    sudo apt-get install xclip
    
    xclip -sel clip < ~/.ssh/id_rsa.pub
