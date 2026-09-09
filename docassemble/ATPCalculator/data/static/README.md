# Static file directory

Files here are served at
`/packagestatic/docassemble.ATPCalculator/<path>`.

| File | Purpose |
| --- | --- |
| `atp-theme.css` | The visual theme. Loaded by `features: css:` in `ATP.yml`. |
| `atp-logo.svg` | The brand mark. Kept as a file for reuse (favicon, print, docs); the navbar copy is inlined in the `set_parts` call in `ATP.yml` so it can inherit the navbar text colour. Edit both together. |
| `datereplace.js` | Date-field behaviour. Loaded by `features: javascript:`. |
| `fonts/` | Self-hosted Public Sans and Source Serif 4. See `fonts/README.md`. |

## The mark

Two bars on one baseline: the amount claimed, drawn as an outline, next to
what the person can actually pay, drawn solid and shorter. It uses
`currentColor`, so it takes the colour of whatever it sits in and works in
dark mode without a second file.

## Bump the version when you change a file here

docassemble serves these with `?v=<package version>` and
`Cache-Control: max-age=31536000`. The version is the only cache key, so
a returning visitor keeps the old file for a year unless `version=` in
`setup.py` changes. Installing the package does not require a bump;
changing a static file does.
