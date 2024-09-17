## [v0.0.2] - Refactor and Security Improvements

### Changed:
- **Security Improvements**: Moved sensitive configuration values such as GitHub token and SMTP credentials from `config.yaml` to environment variables for enhanced security.
  - GitHub API token is now read from the `GITHUB_TOKEN` environment variable.
  - SMTP credentials (username, password) are now read from `SMTP_USERNAME` and `SMTP_PASSWORD` environment variables.

### Fixed:
- Ensured all configurations are safely loaded from environment variables, with necessary defaults remaining in `config.yaml`.
- Tested all changes with existing test cases to verify correct functionality after the refactor.

### How to upgrade:
- **New Environment Variables Required**:
  - `GITHUB_TOKEN`: Your GitHub API token.
  - `SMTP_USERNAME`: Your SMTP username.
  - `SMTP_PASSWORD`: Your SMTP password.

Make sure to set these environment variables before running the application.

## [v0.0.1] - Initial Release

### Added:
- **Project Structure**: Created basic project structure under `src/` and `tests/` directories.
- **YAML Configuration**: Added `config.yaml` for managing GitHub API, SMTP, and scheduling configurations.
- **GitHub API Integration**: Implemented `fetch_github_repo_data()` in `github_api.py` to fetch data from GitHub using the API.
- **Task Scheduling**: Implemented task scheduling in `scheduler.py` to periodically collect GitHub project data using `APScheduler`.
- **Notification System**: Added email notification functionality in `notification.py` using SMTP.
- **Report Generation**: Implemented PDF report generation in `report_generator.py` using `FPDF`.
- **Subscription Management**: Added basic subscription management in `subscription.py` to allow users to subscribe to GitHub projects.
- **Test Suite**: Added unit tests for each major component under `tests/` directory using Python's `unittest`.

### Configuration:
- All configurations (GitHub API, SMTP, and scheduler) are managed through a YAML file (`config.yaml`).

### Future Work:
- Extend functionality with more in-depth data analytics and reporting.
- Add more robust error handling and logging.