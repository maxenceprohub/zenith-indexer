# Changelog

All notable changes to the **Zenith Loader** project will be documented in this file.

## [1.0.0] - 2026-05-10

### Added
- **Core Search Engine**: Implemented a case-insensitive keyword frequency counter using Python's `.count()` method.
- **Directory Scanner**: Integrated `pathlib` for robust file discovery within local directories.
- **Dynamic File Loading**: Added a selection menu allowing users to choose specific `.txt` files for analysis.
- **UTF-8 Support**: Implemented standard encoding for reading text files to ensure compatibility with special characters.
- **Error Handling**: Added `try/except` blocks to manage invalid user inputs and file system errors gracefully.
- **User Interface**: Created a clean, English-language command-line interface (CLI) for better accessibility.

### Technical Details
- **Normalization**: Standardized text processing by converting both source content and search queries to lowercase.
- **Path Management**: Used cross-platform path handling to ensure functionality across Windows, Linux, and macOS.

---
By Maxence DEV
