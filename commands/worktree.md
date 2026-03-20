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

5. **Auto-install claude-code-config if installed per-project:**

   a. Check whether `<repo-root>/.claude/.git` exists **and** that its remote URL is the claude-code-config repo:
      ```bash
      [ -d <repo-root>/.claude/.git ] && echo "has_git" || echo "no_git"
      ```
      If `has_git`, also verify the remote URL by checking both `origin` and `workflow` remotes:
      ```bash
      git -C <repo-root>/.claude remote get-url origin 2>/dev/null | grep -q "jonatanmichael/claude-code-config" && echo "url_match" || \
      git -C <repo-root>/.claude remote get-url workflow 2>/dev/null | grep -q "jonatanmichael/claude-code-config" && echo "url_match" || echo "no_match"
      ```

   b. Skip silently and proceed to step 6 if **either** condition is true:
      - `<repo-root>/.claude/.git` does not exist, **or**
      - neither the `origin` nor `workflow` remote URL contains `jonatanmichael/claude-code-config`

   c. If it does exist (`has_git`), perform a per-project installation into the new worktree. Follow the **Per-project** path from `<repo-root>/.claude/INSTALL.md` — specifically **Step 3 only** — treating `<worktree-path>` as the current directory. Skip Steps 1, 2, 3.5, 4, and 5 from that file.

      Check whether `<worktree-path>/.claude` exists and has git history:
      ```bash
      [ -d <worktree-path>/.claude/.git ] && echo "has_git" || echo "no_git"
      ```

      **Case A — `<worktree-path>/.claude` does not exist:**
      ```bash
      git clone https://github.com/jonatanmichael/claude-code-config.git <worktree-path>/.claude
      ```

      **Case B — `<worktree-path>/.claude` exists but has no git history:**
      ```bash
      git -C <worktree-path>/.claude init
      git -C <worktree-path>/.claude remote add workflow https://github.com/jonatanmichael/claude-code-config.git
      git -C <worktree-path>/.claude fetch workflow
      git -C <worktree-path>/.claude merge workflow/main --allow-unrelated-histories -m "Install claude-code-workflow"
      ```

      **Case C — `<worktree-path>/.claude` exists and already has git history:**
      ```bash
      git -C <worktree-path>/.claude remote add workflow https://github.com/jonatanmichael/claude-code-config.git
      git -C <worktree-path>/.claude fetch workflow
      git -C <worktree-path>/.claude merge workflow/main --allow-unrelated-histories -m "Install claude-code-workflow"
      ```

      If the merge produces conflicts, stop and tell the user which files conflict. Do not resolve conflicts automatically.

   d. After installation, tell the user:
      > claude-code-config was automatically installed in `<worktree-path>/.claude/`.

6. After creating the worktree, report the full path to the user so they can open it.
