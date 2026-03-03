---
name: worktree
description: Cleans up a given git worktree and branch
---

Clean up the git worktree for branch: $ARGUMENTS

Follow these steps exactly:

1. Run `git worktree list --porcelain` to get the list of existing worktrees.

2. Parse the output to find the worktree associated with branch `$ARGUMENTS`.

3. **If no worktree exists for that branch:** Inform the user and stop. Do not proceed further.

4. **If the worktree exists:**
   a. Confirm the worktree path from the list output.
   b. Check if there are any uncommitted changes in the worktree by running `git -C <worktree-path> status --porcelain`. If there are uncommitted changes, warn the user and stop. Do not proceed until the user has committed everything.
   c. Check if the local branch is fully pushed to its remote tracking branch:
      ```
      git -C <worktree-path> log @{u}.. --oneline
      ```
      If this command returns any commits, those commits exist locally but have not been pushed. Warn the user listing the unpushed commits and stop. Do not proceed until the user has pushed everything. If there is no upstream tracking branch configured, also warn the user and stop.
   d. Remove the worktree from git's tracking:
      ```
      git worktree remove --force <worktree-path>
      ```

5. Report the worktree was cleaned up to the user.
