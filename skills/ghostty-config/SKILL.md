---
name: ghostty-config
description: Configure, theme, and validate Ghostty terminal settings on macOS. Use when editing Ghostty preferences, keybindings, fonts, or troubleshooting configuration errors.
license: MIT
---

# Ghostty Configuration (macOS)

Manage Ghostty's plain-text configuration safely and validate every change before finishing.

## Locations

- Primary config: `~/.config/ghostty/config`
- Binary: `/Applications/Ghostty.app/Contents/MacOS/ghostty` (or `ghostty` if symlinked in `~/.local/bin`)

## Workflow

1. Read `~/.config/ghostty/config` before making edits to preserve existing preferences.
2. Discover available options or themes when needed:
   ```zsh
   ghostty +show-config --default --docs | head -n 60
   ghostty +list-themes
   ghostty +list-fonts
   ```
3. Apply focused `key = value` edits (e.g., `font-size`, `theme`, `macos-option-as-alt`, `copy-on-select`, `keybind`).
4. Always validate after editing:
   ```zsh
   ghostty +validate-config
   ```
   A clean exit code `0` with no errors confirms the configuration is valid. Reload in Ghostty with `Cmd+Shift+,`.
