# Essential Git Commands

## Setup
```bash
git config --global user.name "Your Name"
git config --global user.email "you@example.com"
```

## Basic Workflow
```bash
git init                  # Initialize repo
git clone <url>           # Clone remote repo
git status                # Check working tree status
git add .                 # Stage all changes
git commit -m "message"   # Commit staged changes
git push origin main      # Push to remote
git pull                  # Fetch and merge from remote
```

## Branching
```bash
git branch feature        # Create branch
git checkout feature      # Switch to branch
git checkout -b feature   # Create and switch
git merge feature         # Merge branch into current
git branch -d feature     # Delete branch
```

## Useful Commands
```bash
git log --oneline         # Compact history
git diff                  # Show unstaged changes
git stash                 # Stash changes temporarily
git stash pop             # Restore stashed changes
git reset --hard HEAD     # Discard all local changes
git revert <sha>          # Revert a commit
```
