git remote 
1. file:///tmp/myproject.git
2. https://github.com/username/myproject.git
3. ssh://github.com/username/myproject.git
	git:github.com/username/myproject.git



fetch vs pull  -- will fetch the history and modify your files

get you history of changes


git clone git@github.com:BalajiTechs/git_training.git

git clone will download a copy of repo on you local machine


Remotes
	local
	github
	how to use vscode for chaning files, adding files, making commits, pushing changes.

----
Git branches
	git clone <remote url>
		-- copies git repository on local
		-- checkout default branch( main/master)
		-- default branch is protected most of time - admin related activities/meant to be deployed to prod.
	-- You want to make changes
		--- what to do?
			-- create your own branch
				branch name is related to your work
				jira id, ticket it
				you branch out from some current branch

		-- how we create branch (lets create your branch from main --- branchout from main)
			git checkout main # checkout main branch or branch that you want to branch out from
			git pull # make sure we have latest changes
			git branch feature1
			git checkout feature1

		-- How to make changes and push to new branch
			make changes, add files
			git add 
			git commit -m "your message"
			git push -u origin feature1  
			--- 

		-- How to merge your changes to main branch.
			-- main is not protected
			git checkout main
			git merge origin/feature1

			-- main is protected.
			raise PR from feature1 -> main

Branching strategies (for reading)
https://medium.com/@grazibonizi/the-best-branching-model-to-work-with-git-4008a8098e6a


https://github.com/Krishnom/github_docker_training

Excersie
1. Create a new repo called syeda-git-learnigs. Make sure to check README.md and license
2. Clone repo in local folder (~/repo/)
3. Add file start.sh and commit the file and push.
4. Add "echo hello world" in start.sh file and commit the changes and push.
5. Make your main branch protected from direct merges. (Require a pull request before merging and Do not allow bypassing the above settings ) in Branch Protection Rules.
6. Create a new branch "feature1" locally. CHeckout the branch, Add a new file called "stop.sh" and commit it.
7. Push the new branch and raise Pull request to main branch on github.
8. Merge pull requests.