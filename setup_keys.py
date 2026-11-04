"""Store one credential using a hidden terminal prompt."""
import argparse
import getpass
from pathlib import Path
import subprocess
from dotenv import set_key

parser = argparse.ArgumentParser()
parser.add_argument("name", choices=["TOKEN", "OPENROUTER_KEY"])
args = parser.parse_args()
tracked = subprocess.run(
    ["git", "ls-files", "--error-unmatch", ".env"],
    stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL
).returncode == 0
if tracked:
    raise SystemExit("Stop: .env is tracked by Git. Remove it from tracking first.")
value = getpass.getpass(f"Paste {args.name} (hidden), then press Enter: ").strip()
if not value or any(character.isspace() for character in value):
    raise SystemExit("No credential saved: empty value or whitespace.")
env_file = Path(".env")
env_file.touch(mode=0o600, exist_ok=True)
env_file.chmod(0o600)
set_key(str(env_file), args.name, value)
print(f"{args.name} saved to private .env. The value was not displayed.")
