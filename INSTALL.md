# Claude Code Workflow — Installation Guide

You are an AI agent executing this installation. Follow these steps exactly.
Do not summarize or explain — act.

---

## Step 1: Check prerequisites

Run: `python3 --version`

If the command fails or the version is below 3.10, stop and tell the user:
> Python 3.10 or higher is required. Please install it and re-run this installation.

Run: `git --version`

If the command fails, stop and tell the user:
> Git is required. Please install it and re-run this installation.

---

## Step 2: Ask the user one question

Ask:

> Where do you want to install this workflow?
>
> 1. **Global** — applies to every project (`~/.claude`)
> 2. **Per-project** — applies only to the current directory (`.claude/`)

Wait for the answer before continuing.

---

## Step 3: Install

### If the user chose Global

Check whether `~/.claude` exists and is a git repository:

```bash
[ -d ~/.claude/.git ] && echo "has_git" || echo "no_git"
```

**Case A — `~/.claude` does not exist:**

```bash
git clone https://github.com/jonatanmichael/claude-code-config.git ~/.claude
```

**Case B — `~/.claude` exists but has no git history:**

```bash
cd ~/.claude
git init
git remote add workflow https://github.com/jonatanmichael/claude-code-config.git
git fetch workflow
git merge workflow/main --allow-unrelated-histories -m "Install claude-code-workflow"
```

**Case C — `~/.claude` exists and already has git history:**

Check whether the `workflow` remote already exists:

```bash
git -C ~/.claude remote | grep workflow
```

If it does not exist, add it:

```bash
git -C ~/.claude remote add workflow https://github.com/jonatanmichael/claude-code-config.git
```

Then fetch and merge:

```bash
git -C ~/.claude fetch workflow
git -C ~/.claude merge workflow/main --allow-unrelated-histories -m "Install claude-code-workflow"
```

If the merge produces conflicts, stop and tell the user which files conflict. Do not resolve conflicts automatically.

---

### If the user chose Per-project

Check whether `.claude` exists in the current directory:

```bash
[ -d .claude/.git ] && echo "has_git" || echo "no_git"
```

**Case A — `.claude` does not exist:**

```bash
git clone https://github.com/jonatanmichael/claude-code-config.git .claude
```

**Case B — `.claude` exists but has no git history:**

```bash
cd .claude
git init
git remote add workflow https://github.com/jonatanmichael/claude-code-config.git
git fetch workflow
git merge workflow/main --allow-unrelated-histories -m "Install claude-code-workflow"
```

**Case C — `.claude` exists and already has git history:**

```bash
git -C .claude remote add workflow https://github.com/jonatanmichael/claude-code-config.git
git -C .claude fetch workflow
git -C .claude merge workflow/main --allow-unrelated-histories -m "Install claude-code-workflow"
```

If the merge produces conflicts, stop and tell the user which files conflict. Do not resolve them automatically.

---

## Step 4: Verify

Determine the install path used in Step 3 (`~/.claude` or `./.claude`), then run:

```bash
cd <install_path>/skills/scripts && python3 -m skills.deepthink.think --step 1
```

If the command succeeds (exit code 0), proceed to Step 5.

If it fails, show the error output and tell the user:
> Verification failed. The files were installed but the skill scripts could not run.
> Check that Python 3.10+ is active and re-run verification manually.

---

## Step 5: Report success

Tell the user:

> Installation complete.
>
> **Installed to:** `<path>`
>
> **What's available:**
> - Skills: `deepthink`, `planner`, `codebase-analysis`, `problem-analysis`, `decision-critic`, `refactor`, `prompt-engineer`, `doc-sync`, `incoherence`
> - Commands: `/worktree`, `/clean-worktree`
>
> **Try it:**
> ```
> Use your deepthink skill to think through [any question]
> Use your planner skill to write a plan to plans/my-feature.md
> ```
>
> See the full workflow guide: https://github.com/jonatanmichael/claude-code-config
