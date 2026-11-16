# goodnbad-agent-skills

A collection of `skills.sh`-compatible agent skills for macOS developer tooling—built for Antigravity, Claude Code, Codex, and Cursor.

## Install

Install all skills globally with the [Skills CLI](https://skills.sh):

```bash
npx skills add Goodnbadexe/goodnbad-agent-skills -g
```

Or install a specific skill:

```bash
npx skills add Goodnbadexe/goodnbad-agent-skills@ghostty-config -g
npx skills add Goodnbadexe/goodnbad-agent-skills@proxyman-debug -g
npx skills add Goodnbadexe/goodnbad-agent-skills@orbstack-containers -g
npx skills add Goodnbadexe/goodnbad-agent-skills@bruno-api-collections -g
```

## Included Skills

| Skill | Purpose |
| :--- | :--- |
| `ghostty-config` | Configure, theme, and validate Ghostty on macOS (`~/.config/ghostty/config`) |
| `orbstack-containers` | Manage lightweight containers, Compose stacks, and Linux VMs via `orb`, `orbctl`, and `docker` |
| `proxyman-debug` | Automate HTTP/HTTPS debugging, Map Local/Remote, and breakpoints via `proxyman-cli` |
| `bruno-api-collections` | Author and organize Git-friendly `.bru` API collections and environments |

## Local Validation

Validate all skill manifests locally:

```bash
python3 scripts/validate_skills.py
```

## License

[MIT](LICENSE)
