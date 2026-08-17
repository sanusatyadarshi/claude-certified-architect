# my-agent

The [Claude Agent SDK quickstart](https://code.claude.com/docs/en/agent-sdk/quickstart#python-uv):
an agent that reads `utils.py`, finds bugs that would cause crashes, and fixes
them autonomously.

## Files

- `agent.py` — the agent. Calls `query()` with `Read`, `Edit`, and `Glob`
  pre-approved and `permission_mode="acceptEdits"`, then streams messages from
  the agentic loop.
- `utils.py` — the target file. Started with two crash bugs (division by zero on
  an empty list, and a `TypeError` on a `None` user); the agent has since fixed
  both.

## Run

```bash
export ANTHROPIC_API_KEY=your-api-key   # the SDK does not read .env automatically
uv run agent.py
```

The SDK bundles the Claude Code binary, so no separate Claude Code install is
needed. The agent prints its reasoning and each tool it calls, ending with
`Done: success`.

To see it work from scratch again, revert `utils.py` to the buggy version from
the quickstart and re-run.

## Try other prompts

Edit the `prompt` in `agent.py`:

- `"Add docstrings to all functions in utils.py"`
- `"Add type hints to all functions in utils.py"`
- `"Write unit tests for utils.py, run them, and fix any failures"` (needs
  `"Bash"` added to `allowed_tools`)
