# 1. Record architecture decisions

Date: 2026-07-31

## Status

Accepted

## Context

We need to record the architectural decisions made on this project so that
future contributors (human or agent) understand *why* the codebase looks the
way it does, not just what it currently looks like.

## Decision

We will use Architecture Decision Records (ADRs), as described by Michael
Nygard, to capture significant technical and structural decisions for
`atm-fleet-toolkit`.

Each ADR is a short markdown file in `docs/adr/`, numbered sequentially
(`0001-...`, `0002-...`), following the template in `docs/adr/template.md`.

## Consequences

- Decisions and their rationale are discoverable in-repo rather than living
  only in PR discussions, chat history, or someone's memory.
- Every new ADR is immutable once accepted — if a decision changes, a new ADR
  supersedes the old one rather than editing history.
