#! /usr/bin/env python3
# Author: DCameron
# Description: This script will demo HOWTO handle ERRORS gracefully
# using exception handlers (try/except blocks)
"""
    Docstring:
"""
import re
import sys

class HolyDublin(BaseException):
    pass

def search_pattern(pattern=r"^.{19}$", file=r"C:\Users\Donal\course\Python_labs_Mar_2025\labs\words"):
    if file == None:
        raise HolyDublin("No file to search")

    lines = 0
    try:
        fh_in = open(file, mode="rt")
    except FileNotFoundError as err:
        print(f"ERROR CODE={err.args[0]}, message={err.args[1]}, file={err.filename}", file=sys.stderr)
        sys.exit(1)
    except PermissionError as err:
        print(f"ERROR, {err.args}, filename={err.filename}", file=sys.stderr)
        sys.exit(2)
    except BaseException as err:
        print(f"ERROR occurred - investigate", file=sys.stderr)
        sys.exit(3)
    else:
        # Executes if try block succeeds!
        reobj = re.compile(pattern) # Precompile pattern ONCE
        for line in fh_in:
            m = reobj.search(line)
            if m:
                lines += 1
                print(f"Matched {m.group()} on {line.rstrip()} at {m.start()}-{m.end()}")
            fh_in.close()
    finally:
        # Always executes!
        print("And now for something completely different")

    return lines

def main():
    lines_matched = 0
    lines_matched += search_pattern(file=None)
    print(f"Lines matched = {lines_matched}")
    return None

if __name__ == "__main__":
    main()
    sys.exit(0)