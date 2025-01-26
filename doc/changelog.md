
# Change Log
All notable changes to this project will be documented in this file.
 
The format is based on [Keep a Changelog](http://keepachangelog.com/)
and this project adheres to [Semantic Versioning](http://semver.org/).

 
## [1.3.0] - 2025-02-01

### Added
- [changelog.md](changelog.md) has been added.
- Data and User Data dirs has been added.
- `logs` directory has been added.
- New `import logging` in `index.py`.
- Now you can send messages to all your configured objetive accounts.
- New exceptions have been added to the `install.py` file.
- New line "...to update it go to python.org" has been added to the `install.py` file.
- `install.py` support for Linux added.

### Changed
- All files has been adapted to don't use "wuser" variable (Windows profile name)
- Windows profile name (wuser) is not necesary anymore.
- The `install.py` file has been updated to use the new exceptions and create the `logs` directory.
- The `index.py` file has been updated to use the `logs` directory.
- "Message sent successfully." -> "Message sent successfully to {user}." where {user} is the objetive account.

### Fixed
Nothing