import asyncio
from pathlib import Path

from social_auto_upload.conf import BASE_DIR
from social_auto_upload.uploader.tk_uploader.main_chrome import tiktok_setup

if __name__ == '__main__':
    account_file = Path(BASE_DIR / "cookies" / "tk_uploader" / "account.json")
    cookie_setup = asyncio.run(tiktok_setup(str(account_file), handle=True))
