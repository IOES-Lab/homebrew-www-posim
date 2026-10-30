# Direct release publication

The private application release workflow creates a draft here with a version and
full source revision in its machine-readable body marker. Each platform runner
uploads its own files and a small producer receipt. Matching retries reuse the
existing bytes; changed assets require a new version.

Mac checks the local native archive, its reconstructed parts and the installed
DMG, then uploads its own files and commits `release-input.json` with asset IDs,
sizes, SHA-256 hashes and acceptance evidence. `scripts/direct_release.py` checks
these values against the draft API and producer receipts before publishing it.
The workflow then updates the Homebrew cask. It downloads only three small JSON
receipts and uses no Actions artifact storage or installer cache in this mode.

The application keeps APT signing and website/runtime activation on their existing
owner-local host. The APT stage downloads only the published Linux package for
signing. Release downloads remain GitHub Release assets and have no Actions
artifact retention deadline.

Legacy release inputs retain the older origin-download verification path for
manual recovery. Workflow-only maintenance does not republish an existing input.
Run `python -m unittest discover -s scripts` to check both publication paths.
