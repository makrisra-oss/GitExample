# Staging and committing files in Git

- git add
- git commit
- git push
- git pull
- git checkout
- git merge

![fc6eaa033ae6479fa63856c10b5ebb57.png](../../Desktop/fc6eaa033ae6479fa63856c10b5ebb57.png)

# Git Fundamentals and Collaborative Git  

## 1. Git Basics  

### What is Git?  
- Git is a **distributed version control system** for tracking changes in source code.  
- Ensures collaboration, version history, and rollback capability.  

### Key Concepts:  
- **Repository (repo):** A directory that tracks changes.  
- **Working Directory:** Your local directory where files are modified.  
- **Staging Area:** The place where changes are prepared before committing.  
- **Commit:** A snapshot of changes with a message.  
- **Branch:** A separate line of development.  

### Git Lifecycle:  
1. **Modify files** in the working directory.  
2. **Stage changes** with `git add`.  
3. **Commit changes** with `git commit`.  
4. **Push commits** to a remote repository with `git push`.  

---

## 2. Common Git Commands  

### Repository Management  
- `git init` → Initialise a new Git repository.  
- `git clone <repo>` → Clone an existing repository.  

### Tracking Changes  
- `git status` → Check the current state of the working directory.  
- `git add <file>` → Add a file to the staging area.  
- `git commit -m "message"` → Commit staged changes with a message.  

### Branching and Merging  
- `git branch` → List branches.  
- `git branch <branch-name>` → Create a new branch.  
- `git checkout <branch>` → Switch to a branch.  
- `git merge <branch>` → Merge a branch into the current branch.  

### Remote Repositories  
- `git remote add origin <url>` → Link a local repo to a remote one.  
- `git push` → Push changes to the remote repo.  
- `git pull` → Fetch and merge changes from the remote repo.  
- `git fetch` → Fetch changes without merging.  

### Viewing History  
- `git log` → View commit history.  
- `git diff` → Show changes between versions.  

---

## 3. Collaborative Git  

### Key Practices:  
1. **Branching Strategy:**  
   - Use meaningful branch names (e.g., `feature/login`, `bugfix/header`).  
   - Keep `main` (or `master`) stable for production.  

2. **Pull Requests (PRs):**  
   - Used to review and merge changes into the main branch.  
   - Encourage team discussions and peer review.  

3. **Code Reviews:**  
   - Ensure quality and consistency by reviewing PRs.  

4. **Resolving Conflicts:**  
   - Conflicts occur when changes overlap.  
   - Use `git merge` or `git rebase` to resolve conflicts.  

### Collaboration Workflow:  
1. Clone the repo:  
   ```bash
   git clone <repo-url>
   
### Create a branch

- git checkout -b <branch-name>

### Make changes and commit:

- git add .  
- git commit -m "Add feature xyz"

### Push changes to Remote:

git push -u origin <branch-name>

### Open a pull request (PR):

- Submit your branch to be reviewed and merged into main.

### Address Feedback and Resolve Conflicts (if any)

- Fetch and merge main into your branch:
- git pull origin main

