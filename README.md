# Auto push git with python


## TUTORIAL
`git clone https://github.com/YuriKun11/Autopush-git`

First commit
`py main.py`

Update Repo

`py update.py`

Upload to Another Repo
`py move.py`


#Additional Info

## Migrate Repository
`git remote remove origin`

`git remote add origin (paste-repo-link here remove parenthesis)` 

`git push -u origin master`

## Update Repository
`git pull origin master`

`git add .`

`git commit -m "Update"`

`git push -u origin master`

## Remove Connections 
`rmdir /s /q .git`


## Reinitialize git after Removing Connection
`git pull origin master --allow-unrelated-histories`

`git add .`

`git commit -m "Resolved merge conflicts and merged unrelated histories"`

`git push origin master`
