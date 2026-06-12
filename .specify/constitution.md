# Career Bridge AI Constitution

## Principles

1. Student outcomes come first: features must improve clarity, access, or actionability for learners.
2. Recommendations must be explainable: every ranked result should expose the main match signals and gaps.
3. Privacy is a product requirement: resumes, profile data, and generated plans must be handled with least privilege.
4. Quality gates protect trust: linting, tests, coverage, and security scans run before release.
5. Accessibility is part of done: user-facing workflows should remain understandable and keyboard-friendly.

## Engineering Standards

- Keep data contracts explicit for CSV-backed engines.
- Prefer deterministic rules before adding probabilistic ranking.
- Document user-visible changes in `CHANGELOG.md`.
- Add tests for parsing, scoring, matching, and fallback behavior.

## Governance

Changes to this constitution require a pull request that explains the motivation, migration impact, and affected templates.
