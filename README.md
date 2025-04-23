# voting_support
Documentation is currently work in progress

## Prepare Raspberry Pi
The steps below should work with recent Raspian version based on Debian 12 (bookworm)

1. Remove current Chromium Version
   ```
   sudo apt-get remove chromium chromium-browser rpi-chromium-mods
   ```
3. Install fixed version
   ```
   sudo apt-get install chromium=134.0.6998.35-1~deb12u1 chromium-common=134.0.6998.35-1~deb12u1
   ```
5. Download proper chromedriver
   ```
   cd /tmp && curl -LO https://github.com/electron/electron/releases/download/v35.2.0/chromedriver-v35.2.0-linux-arm64.zip
   ```
7. Extract and install chromedriver
   ```
   unzip -x chromedriver-v35.2.0-linux-arm64.zip && sudo mv chromedriver /usr/lib/chromium-browser/
   ```
8. Verify versions of Chromium browser and Chromedriver
   ```
   # /usr/bin/chromium --version
   Chromium 134.0.6998.35 built on Debian GNU/Linux 12 (bookworm)
   # /usr/lib/chromium-browser/chromedriver --version
   ChromeDriver 134.0.6998.205 (b76fc0a6561bcfe6646c31a04fa8d5ae2ad41d5b)
   ```

## Setup Python Virtual Environment
Clone this respository and make it your current working directory

1. Create empty venv
   ```
   python3 -m venv .venv
   ```
2. Activate and install requirements
   ```
   source .venv/bin/activate
   pip install -r requirements.txt
   ```
