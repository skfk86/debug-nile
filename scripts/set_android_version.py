#!/usr/bin/env python3
"""Set versionCode / versionName in android/app/build.gradle (Groovy or Kotlin DSL, with or without '=').

Usage: set_android_version.py --code 42 --name 1.2.0 [--gradle android/app/build.gradle]
Idempotent. Exits 1 if the file has no versionCode/versionName to replace.
"""
import argparse, re, sys

def patch(text, code=None, name=None):
    n_code = n_name = 0
    if code is not None:
        text, n_code = re.subn(r'(versionCode\s*=?\s*)\d+', lambda m: m.group(1) + str(int(code)), text, count=1)
    if name is not None:
        text, n_name = re.subn(r'(versionName\s*=?\s*)"[^"]*"', lambda m: m.group(1) + '"' + name + '"', text, count=1)
    return text, n_code, n_name

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--gradle", default="android/app/build.gradle")
    ap.add_argument("--code", type=int)
    ap.add_argument("--name")
    a = ap.parse_args()
    text = open(a.gradle, encoding="utf-8").read()
    new, c, n = patch(text, a.code, a.name)
    if (a.code is not None and not c) or (a.name is not None and not n):
        print("could not find versionCode/versionName in", a.gradle, file=sys.stderr)
        return 1
    open(a.gradle, "w", encoding="utf-8").write(new)
    print(f"versionCode={a.code} versionName={a.name}")
    return 0

if __name__ == "__main__":
    sys.exit(main())
