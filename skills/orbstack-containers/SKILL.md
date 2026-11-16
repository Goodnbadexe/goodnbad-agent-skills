---
name: orbstack-containers
description: Manage lightweight Docker containers, Compose stacks, and Linux virtual machines on Apple Silicon using OrbStack (orb, orbctl, docker). Use when starting, inspecting, or debugging local containers and dev VMs.
license: MIT
---

# OrbStack Containers & Linux VMs

Operate local containers and Linux machines efficiently on macOS using OrbStack's CLI tools.

## CLI Tools

- `orb` / `orbctl` (`/Applications/OrbStack.app/Contents/MacOS/bin/orb`)
- `docker` / `docker compose` (automatically routed to OrbStack once launched)

## Common Workflows

1. **Check status & start OrbStack:**
   ```zsh
   orb status || open -a OrbStack
   ```
2. **Manage Linux VMs:**
   ```zsh
   orb list
   orb create ubuntu dev-box
   orb -m dev-box
   ```
3. **Manage Docker containers & Compose:**
   ```zsh
   docker ps
   docker compose up -d
   docker compose logs -f --tail=100
   ```
4. **Cleanup unused images/volumes safely:**
   ```zsh
   docker system df
   docker image prune -f
   ```
