# Downloader Module

This module handles the downloading and preparation of Sefer HaMitzvot content from Wikisource.

## Files

- `generate_prep_file.py` - Generates a preparation file with all URLs and metadata for downloading
- `download_sefer_hamitzvot.py` - Downloads content from Wikisource based on the prep file

## Usage

1. First, generate the prep file:
   ```bash
   cd downloader
   python generate_prep_file.py
   ```

2. Then download the content:
   ```bash
   python download_sefer_hamitzvot.py
   ```

## Output

- Creates `sefer_hamitzvot_prep.json` with download metadata
- Downloads content to `../content/` directory

## Dependencies

- requests
- beautifulsoup4
- pathlib
- json
- logging
- concurrent.futures
- threading 