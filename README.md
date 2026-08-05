# claude-certified-architect

Code and preparation material for the Anthropic Claude Certified Architect Exam

## Examples

| Directory | Source | What it does |
| --- | --- | --- |
| [`my-agent/`](my-agent/) | [Agent SDK quickstart](https://code.claude.com/docs/en/agent-sdk/quickstart#python-uv) | An agent that reads `utils.py`, finds crash bugs, and fixes them autonomously |

### Running `my-agent`

Requires Python 3.10+ and [uv](https://docs.astral.sh/uv/). The SDK bundles the
Claude Code binary, so no separate install is needed.

```bash
cd my-agent
export ANTHROPIC_API_KEY=your-api-key   # the SDK does not read .env automatically
uv run agent.py
```

## Anthropic references

### Claude Agent SDK

Claude Code packaged as a library — ships built-in tools (Read/Edit/Bash/Glob/Grep),
the agent loop, permissions, and sessions. This is what `my-agent/` uses.

- [Quickstart](https://code.claude.com/docs/en/agent-sdk/quickstart)
- [Python SDK reference](https://code.claude.com/docs/en/agent-sdk/python)
- [TypeScript SDK reference](https://code.claude.com/docs/en/agent-sdk/typescript)
- [Permissions](https://code.claude.com/docs/en/agent-sdk/permissions)
- [Hooks](https://code.claude.com/docs/en/agent-sdk/hooks)
- [Sessions](https://code.claude.com/docs/en/agent-sdk/sessions)
- [MCP servers](https://code.claude.com/docs/en/agent-sdk/mcp)
- [Hosting](https://code.claude.com/docs/en/agent-sdk/hosting)
- [Example agents](https://github.com/anthropics/claude-agent-sdk-demos)

### Claude API

The `/v1/messages` API you call directly — a different product from the Agent SDK.

- [Models overview](https://platform.claude.com/docs/en/about-claude/models/overview)
- [Model migration guide](https://platform.claude.com/docs/en/about-claude/models/migration-guide)
- [Pricing](https://platform.claude.com/docs/en/pricing)
- [Tool use](https://platform.claude.com/docs/en/agents-and-tools/tool-use/overview)
- [Adaptive thinking](https://platform.claude.com/docs/en/build-with-claude/adaptive-thinking)
- [Prompt caching](https://platform.claude.com/docs/en/build-with-claude/prompt-caching)
- [Streaming](https://platform.claude.com/docs/en/build-with-claude/streaming)
- [Structured outputs](https://platform.claude.com/docs/en/build-with-claude/structured-outputs)
- [Errors](https://platform.claude.com/docs/en/api/errors)

### Managed Agents

Server-managed stateful agents — Anthropic runs the loop and hosts a per-session sandbox.

- [Overview](https://platform.claude.com/docs/en/managed-agents/overview)
- [Quickstart](https://platform.claude.com/docs/en/managed-agents/quickstart)
- [Agent setup](https://platform.claude.com/docs/en/managed-agents/agent-setup)
- [Sessions](https://platform.claude.com/docs/en/managed-agents/sessions)
- [Environments](https://platform.claude.com/docs/en/managed-agents/environments)
- [Events and streaming](https://platform.claude.com/docs/en/managed-agents/events-and-streaming)

### Claude Code

- [Docs](https://code.claude.com/docs/en/overview)
- [Setup](https://code.claude.com/docs/en/setup)
- [Troubleshooting](https://code.claude.com/docs/en/troubleshooting)
