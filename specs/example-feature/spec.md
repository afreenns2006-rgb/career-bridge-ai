# Example Feature: Opportunity Search Resilience

## Summary

Improve opportunity search so it remains stable when CSV files use alternate but valid column names.

## Users

- Students searching internships, bootcamps, competitions, and jobs.
- Maintainers updating opportunity datasets.

## Functional Requirements

- The system logs available opportunity dataframe columns when data is loaded.
- The system searches by `name` when present and falls back to `title` when needed.
- The system searches skill fields using `skills`, `skill`, or `required_skills`.
- Missing required columns return an empty result with a warning instead of raising `KeyError`.

## Acceptance Criteria

- Given an opportunities CSV with `title` and `skill`, when a user searches for "python", then matching rows are returned.
- Given an opportunities CSV without a name-like column, when a user searches, then an empty result is returned.
- Given filters for category or type, when the matching column exists, then results are filtered without crashing.

## Test Plan

- Unit test column fallback behavior.
- Unit test missing required columns.
- Run Streamlit Opportunity Dashboard manually after data changes.
