---
name: worktree
description: Creates isolated git worktree and branch inside repo/.worktrees
---

Create or reuse a git worktree for branch: $ARGUMENTS

Follow these steps exactly:

1. Run `git worktree list --porcelain` to get the list of existing worktrees.

2. Parse the output to check if any worktree is already using the branch `$ARGUMENTS`.

3. **If the worktree already exists:** Report the path to the user and stop. Do not create anything new.

4. **If the worktree does not exist:**
   a. Determine the repo root with `git rev-parse --show-toplevel`.
   b. Derive the worktree path: `<repo-root>/.worktrees/$ARGUMENTS`. Example: if the repo is at `/dev/myapp`, the worktree goes at `/dev/myapp/.worktrees/$ARGUMENTS`.
   c. Ensure `.worktrees/` is listed in the repo's `.gitignore`. If it is not, append it.
   d. Check whether the branch `$ARGUMENTS` already exists locally (`git branch --list $ARGUMENTS`) or remotely (`git ls-remote --heads origin $ARGUMENTS`).
   e. If the branch exists remotely but not locally, create the worktree tracking the remote branch:
      ```
      git worktree add <worktree-path> --track -b $ARGUMENTS origin/$ARGUMENTS
      ```
   f. If the branch exists locally (but has no worktree), create the worktree from it:
      ```
      git worktree add <worktree-path> $ARGUMENTS
      ```
   g. If the branch does not exist anywhere, first ensure you are on the main branch or fetch the latest main, then create a new branch and worktree in one step:
      ```
      git fetch origin main
      git worktree add -b $ARGUMENTS <worktree-path> origin/main
      ```

5. After creating the worktree, report the full path to the user so they can open it.
