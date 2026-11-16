---
name: proxyman-debug
description: Automate HTTP/HTTPS debugging, toggle Breakpoint/Map Local/Map Remote rules, manage the system proxy, and export/import rule sets with Proxyman CLI and MCP on macOS.
license: MIT
---

# Proxyman CLI & MCP Debugging

Control Proxyman from the terminal to inspect traffic, toggle debugging tools, and version-control rule sets.

## CLI Location

- `/Applications/Proxyman.app/Contents/MacOS/proxyman-cli` (or `proxyman-cli` if symlinked in `~/.local/bin`)

## Common Workflows

1. **Enable MCP integration:**
   ```zsh
   proxyman-cli mcp on
   ```
2. **Toggle debugging tools on/off:**
   ```zsh
   proxyman-cli breakpoint on
   proxyman-cli maplocal on
   proxyman-cli map-remote off
   ```
3. **Export and import debugging rules (great for sharing in Git repos):**
   ```zsh
   proxyman-cli export --output ./proxyman-rules.proxymanconfig
   proxyman-cli import ./proxyman-rules.proxymanconfig
   ```
4. **Clear current capture session before a fresh test run:**
   ```zsh
   proxyman-cli clear-session
   ```
