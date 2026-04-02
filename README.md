# 🐍 Vetlog Calendar
<!-- ALL-CONTRIBUTORS-BADGE:START - Do not remove or modify this section -->
[![All Contributors](https://img.shields.io/badge/all_contributors-2-orange.svg?style=flat-square)](#contributors-)
<!-- ALL-CONTRIBUTORS-BADGE:END -->

**Installation**

1. Clone the repository

```sh
git clone https://github.com/josdem/py-vetlog-calendar
cd py-vetlog-calendar
```

2. Install the dependencies

```sh
uv sync

# To include dev dependencies (e.g., for testing):
uv sync --extra dev
```

3. (Optional) Verify installation

```sh
uv run version
```

## Usage

**Run**

```sh
# List upcoming events
uv run events

# List user's token paths
uv run paths
```

**Test**

```sh
# Test everything
uv run pytest tests/unit -v

# Test a specific file
uv run pytest tests/unit/test_config.py

# Test a matching keyword
uv run pytest -k config
```

**Format**

```sh
# Check code for linting/formatting issues (does not fix)
uv run ruff check

# Format code automatically
uv run ruff format

# Automatically fix linting issues
uv run ruff check --fix
```

**Links**
- https://github.com/josdem/py-vetlog-calendar/wiki
- https://github.com/josdem/vetlog-spring-boot



## Contributors ✨

Thanks goes to these wonderful people ([emoji key](https://allcontributors.org/docs/en/emoji-key)):

<!-- ALL-CONTRIBUTORS-LIST:START - Do not remove or modify this section -->
<!-- prettier-ignore-start -->
<!-- markdownlint-disable -->
<table>
  <tbody>
    <tr>
      <td align="center" valign="top" width="14.28%"><a href="https://github.com/habartakh"><img src="https://avatars.githubusercontent.com/u/177358275?v=4?s=100" width="100px;" alt="Hajar Bartakh"/><br /><sub><b>Hajar Bartakh</b></sub></a><br /><a href="https://github.com/josdem/py-vetlog-calendar/commits?author=habartakh" title="Documentation">📖</a></td>
      <td align="center" valign="top" width="14.28%"><a href="https://itsiiie.github.io/resume-site/"><img src="https://avatars.githubusercontent.com/u/111443349?v=4?s=100" width="100px;" alt="Shashank Singh"/><br /><sub><b>Shashank Singh</b></sub></a><br /><a href="https://github.com/josdem/py-vetlog-calendar/commits?author=itsiiie" title="Code">💻</a> <a href="#infra-itsiiie" title="Infrastructure (Hosting, Build-Tools, etc)">🚇</a></td>
    </tr>
  </tbody>
</table>

<!-- markdownlint-restore -->
<!-- prettier-ignore-end -->

<!-- ALL-CONTRIBUTORS-LIST:END -->

This project follows the [all-contributors](https://github.com/all-contributors/all-contributors) specification. Contributions of any kind welcome!