---
name: workflow
description: List all available skills with descriptions and example invocations
---

Display the available skills in this workflow. Format as a markdown table followed by usage examples.

Output exactly this:

## Available Skills

| Skill | What it does | When to use |
|---|---|---|
| `deepthink` | Structured reasoning for open-ended analytical questions | Trade-offs, taxonomy design, architecture decisions, "I don't know what shape the answer should take" |
| `planner` | Write and execute implementation plans with review cycles | Any non-trivial change — forces ambiguity to surface before coding starts |
| `codebase-analysis` | Systematic exploration of a repository's structure and patterns | Before working on an unfamiliar codebase or large surface area |
| `problem-analysis` | Root cause investigation | Understanding WHY a problem occurs, not how to fix it |
| `decision-critic` | Stress-test a specific decision | Validating an architectural or design choice before committing |
| `refactor` | Multi-dimensional technical debt analysis | After LLM-generated features, before major changes, when simple changes touch many files |
| `prompt-engineer` | Optimize agent prompts | When a sub-agent isn't performing as expected |
| `doc-sync` | Audit and synchronize CLAUDE.md/README.md hierarchy | Bootstrapping the workflow on an existing repo, after major refactors |
| `incoherence` | Detect mismatches between specs, docs, and implementation | When something feels off but you can't pinpoint it |
| `cc-history` | Query Claude Code conversation history and token usage | Analyzing past sessions, auditing token spend |

## Usage

Skills are invoked with natural language:

```
Use your deepthink skill to think through [question]
Use your planner skill to write a plan to plans/[name].md
Use your planner skill to execute plans/[name].md
Use your codebase-analysis skill to explore [path or description]
Use your problem-analysis skill to investigate [problem]
Use your decision-critic skill on [decision]
Use your refactor skill on [path]
Use your prompt-engineer skill to optimize [file]
Use your doc-sync skill to synchronize documentation across this repository
Use your incoherence skill to check [path or description]
```

## Workflow

For non-trivial changes, use skills in this order:

1. `codebase-analysis` — understand the surface area
2. `deepthink` or `problem-analysis` — think it through
3. `planner` (plan mode) — write the plan
4. `/clear` — reset context
5. `planner` (execute mode) — implement

See the full guide: https://github.com/jonatanmichael/claude-code-config
