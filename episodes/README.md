# Episode manuscripts

This directory is the target location for the 31 episode scripts listed in `episodes.jsonl`.

## Naming

Use the existing numbered filenames, for example `01-marx-and-ai.md` and `31-arendt-and-ai.md`.

## Production flow

`episodes.jsonl` is the episode index. Its `path` field identifies the Markdown manuscript consumed by `scripts/build_episode_video.py`. Keep those paths synchronized when moving manuscripts.

The existing manuscripts and metadata paths are being kept unchanged until the move can be applied atomically, so video production remains functional.