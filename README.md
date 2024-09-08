# Auto push git with python

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
