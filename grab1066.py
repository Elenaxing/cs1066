### cs1066-dev/utils/grab1066.py - VERSION 20260724
"""
This script simplifies the work a learner in one of my classes
must do to grab the files needed for a course unit, which are
stored in a public GitHub repository.

If a learner wants the files for `m04b`, they'd run this script in
the course codespace as follows:

$ python3 grab{COURSE_NUM}.py m04b

The input parameter (i.e., `m04b` in this example) should match the
name of a public GitHub repo for this course.  The script will place
this unit's files in the `m04` subdirectory of the user's codespace,
where `m04` stands for the course's Module 4 and `b` is the module's
second shard.

If a subdirectory of the same name already exists, this script assumes
that the user wants a new clean copy of the repo's files.  It will name
the clean copy `REPO_clean` (e.g., `m04_clean`).

Author: Mike Smith (with an AI copilot)
Date: June 2026
"""

import os
import re
import subprocess
import sys
from urllib import request, error
import zipfile

######
###
### COURSE-SPECIFIC CHANGES GO IN THIS BLOCK ONLY
###

# Course-specific global constants and configuration parameters
COURSE_NUM = '1066'
COURSE_NAME = f'cs{COURSE_NUM}'

# Global constants and configuration parameters
ORG_URL = f'https://github.com/{COURSE_NAME}/'
CODESPACES_ROOT = f'/workspaces/{COURSE_NAME}'
MAIN_ZIP_PATH = '/archive/refs/heads/main.zip'

def determine_dst(module, item):
    """Determine the destination directory for a given file item"""
    # In CS1066, we move the classnotes files (cnXX.ipynb) and
    # section notes (secXX.ipynb) into the classnotes directory.
    if re.match(r"^cn\d{2}\.ipynb$", item):
        return os.path.join('classnotes', item)
    elif re.match(r"^sec\d{2}\.ipynb$", item):
        return os.path.join('classnotes', item)  
    else:
        return os.path.join(module, item)

###
### END COURSE-SPECIFIC CHANGES
###
######


def repo_exists(repo: str, timeout: float = 10.0):
    """Used to check if a repo exists with this url"""
    url = ORG_URL + repo + MAIN_ZIP_PATH
    req = request.Request(url, method="HEAD")
    try:
        with request.urlopen(req, timeout=timeout) as resp:
            return 200 <= resp.status < 400
    except error.HTTPError as e:
        # e.code will have the HTTP status (404, 403, etc.)
        return False
    except error.URLError:
        # DNS failure, refused connection, etc.
        return False


def validate_working_dir():
    """Validates and returns the root directory of the user's codespace"""
    # Grab the current directory path
    cwd = os.getcwd()

    # If cwd is the codespace root directory, use it
    if cwd == CODESPACES_ROOT:
        return cwd

    # If we get here, we're not in the codespace root directory, and we
    # need to check that CODESPACES_ROOT exists.
    if not os.path.exists(CODESPACES_ROOT) or not os.path.isdir(CODESPACES_ROOT):
        sys.exit(f"ERROR: {CODESPACES_ROOT} doesn't exist")

    # It exists. Jump to CODESPACES_ROOT and return that path.
    try:
        os.chdir(CODESPACES_ROOT)
    except Exception as e:
        sys.exit(f"ERROR changing directory: {e}")

    return CODESPACES_ROOT


def my_rename(frompath, topath):
    """Rename a file or directory path from `frompath` to `topath`"""
    try:
        os.rename(frompath, topath)
    except FileNotFoundError:
        sys.exit(f"ERROR: the directory `{frompath}` does not exist")
    except FileExistsError:
        sys.exit(f"ERROR: a directory or file named `{topath}` already exists")
    except Exception as e:
        sys.exit(f"ERROR: {e}")


def move_item(src, dst, clean_dir, clean_exists, relpath):
    """Move `src` to `dst`, merging into `dst` when both are directories.

    When `dst` already exists as a non-directory conflict (or a file),
    move `src` into `clean_dir` if it exists; otherwise leave `src` in
    place and report that a clean copy is needed.

    Returns True if any conflicting item was left in place for a later
    rename of the remaining zip tree to `clean_dir`.
    """
    if not os.path.exists(dst):
        # Destination is free. Move src there.
        my_rename(src, dst)
        print(f"... Moved {src} to {dst}")
        return False

    if os.path.isdir(src) and os.path.isdir(dst):
        # Both are directories: merge by moving each child individually.
        clean_needed = False
        for item in os.listdir(src):
            child_src = os.path.join(src, item)
            child_dst = os.path.join(dst, item)
            child_rel = os.path.join(relpath, item) if relpath else item
            if move_item(child_src, child_dst, clean_dir, clean_exists, child_rel):
                clean_needed = True
        # Remove src if it is now empty (all children were moved).
        try:
            if not os.listdir(src):
                os.rmdir(src)
                print(f"... Removed empty directory {src}")
        except Exception as e:
            sys.exit(f"ERROR removing directory {src}: {e}")
        return clean_needed

    if clean_exists:
        # Conflict, and clean_dir already exists: move src into it,
        # preserving relative path under clean_dir.
        dst_clean = os.path.join(clean_dir, relpath)
        parent = os.path.dirname(dst_clean)
        if parent and not os.path.exists(parent):
            os.makedirs(parent, exist_ok=True)
        my_rename(src, dst_clean)
        print(f"... Moved {src} to {dst_clean}")
        return False

    # Conflict and no clean_dir yet: leave src in place for later rename.
    print(f"... Not moving {src}")
    return True


def process_zipfile(repo):
    """Downlads, extracts, and deletes the zipfile for the specified repo"""
    # Create URL to a zipfile of the specified github repo
    url = ORG_URL + repo + MAIN_ZIP_PATH
    zip_fname = os.path.basename(url)

    # Download the repo's files (quietly)
    try:
        command = ['wget', url]
        subprocess.run(command, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL, check=True)
    except Exception as e:
        sys.exit(f"ERROR executing wget command: {e}")
    print(f"... Zip file downloaded from: {url}")

    # Unzip the downloaded file
    try:
        # Open the zip file
        with zipfile.ZipFile(zip_fname, 'r') as zip_ref:
            # Extract contents to the current directory
            zip_ref.extractall()
    except zipfile.BadZipFile:
        sys.exit(f"ERROR: {zip_fname} is not a valid ZIP file")
    except Exception as e:
        sys.exit(f"Error unzipping {zip_fname}: {e}")
    print(f"... Unzipped {zip_fname} into {repo}-main")

    # Remove the downloaded zip file
    try:
        os.remove(zip_fname)
    except Exception as e:
        sys.exit(f"ERROR removing file {zip_fname}: {e}")
    print(f"... Removed {zip_fname}")


def move_files(repo, module):
    """Moves the files from repo-main to the appropriate location(s)"""
    # Create the directory names we'll possibly need
    zip_dir = repo + '-main'
    clean_dir = module + '_clean'

    # Set flag indicating whether clean_dir exists
    clean_exists = os.path.exists(clean_dir)

    # Flag indicating whether we need to rename zip_dir as clean_dir after processing all files
    clean_needed = False

    # Process the unzipped files in zip_dir. If module doesn't yet
    # exist, we create it. The code moves a file if it doesn't already
    # exist at the destination directory. If a directory already exists
    # at the destination, its children are merged in recursively. If a
    # conflicting file (or non-mergeable item) exists, we move it to
    # clean_dir (if this directory exists) or mark that we need to
    # rename zip_dir as clean_dir when we're done. Some files have
    # special handling.
    if not os.path.exists(module):
        # Module doesn't exist. Create it.
        os.mkdir(module)
        print(f"... Created {module} folder")

    # Process each file in zip_dir
    for item in os.listdir(zip_dir):
        src = os.path.join(zip_dir, item)
        dst = determine_dst(module, item)
        if move_item(src, dst, clean_dir, clean_exists, item):
            clean_needed = True

    if clean_needed:
        # Move the remaining files in zip_dir to clean_dir
        my_rename(zip_dir, clean_dir)
        print(f"... Renamed {zip_dir} to {clean_dir}")
    else:
        # Remove the now-empty zip_dir
        try:
            os.rmdir(zip_dir)
            print(f"... Removed empty directory {zip_dir}")
        except Exception as e:
            sys.exit(f"ERROR removing directory {zip_dir}: {e}")


def main():
    # Check usage and grab the repo name
    if len(sys.argv) != 2:
        sys.exit(f"Usage: python3 grab{COURSE_NUM}.py REPO")

    repo = sys.argv[1]

    # Check validity of input parameter and gracefully handle bad parameters
    if not repo_exists(repo):
        sys.exit(f"ERROR: {repo} is not valid; did you mistype it?")

    # Start alerting the user to our progress
    print(f"STARTING grab{COURSE_NUM}.py ...")

    # Make sure the script is in CODESPACES_ROOT
    codespace_path = validate_working_dir()
    print(f"... Working in directory: {codespace_path}")

    # Download the repo as a zipfile and process it
    process_zipfile(repo)

    # Determine module name (e.g., m04) from repo name (e.g., m04b)
    # and then move the files to the right places.
    module = repo[0:3]
    move_files(repo, module)

    # Alert the user that we're done
    print(f"grab{COURSE_NUM}.py COMPLETE")
    print()
    print(f"To run a script in {module}, make sure to put yourself")
    print(f"in that directory by executing: cd {module}")
    print()

if __name__ == '__main__':
    main()
