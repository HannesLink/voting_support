# voting_support
Documentation not yet available

## Prepare Raspberry Pi
1. Remove current Chromium Version
   ```sudo apt-get remove chromium chromium-browser rpi-chromium-mods```
2. Install fixed version
   ```sudo apt-get install chromium=134.0.6998.35-1~deb12u1 chromium-common=134.0.6998.35-1~deb12u1```
3. Download proper chromedriver
   ```curl -LO https://github.com/electron/electron/releases/download/v35.2.0/chromedriver-v35.2.0-linux-arm64.zip```
4. Extract and install chromedriver
   ```unzip -x chromedriver-v35.2.0-linux-arm64.zip && sudo mv chromedriver /usr/lib/chromium-browser/```
