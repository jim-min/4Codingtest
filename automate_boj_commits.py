import os
import re
import json
import time
import subprocess
import requests

# Configuration
BOJ_DIR = "BOJ"
SOLVED_AC_API_URL = "https://solved.ac/api/v3/problem/lookup"
COMMIT_MESSAGE_FILE = "commit_message.txt"

# Mapping from numerical level to tier name
LEVEL_TO_TIER = {
    1: "Bronze V", 2: "Bronze IV", 3: "Bronze III", 4: "Bronze II", 5: "Bronze I",
    6: "Silver V", 7: "Silver IV", 8: "Silver III", 9: "Silver II", 10: "Silver I",
    11: "Gold V", 12: "Gold IV", 13: "Gold III", 14: "Gold II", 15: "Gold I",
    16: "Platinum V", 17: "Platinum IV", 18: "Platinum III", 19: "Platinum II", 20: "Platinum I",
    21: "Diamond V", 22: "Diamond IV", 23: "Diamond III", 24: "Diamond II", 25: "Diamond I",
    26: "Ruby V", 27: "Ruby IV", 28: "Ruby III", 29: "Ruby II", 30: "Ruby I",
}

def get_tier_from_level(level):
    return LEVEL_TO_TIER.get(level, "Unrated")

def run_command(command, cwd=None):
    print(f"Executing command: {command}") # Added print statement
    try:
        result = subprocess.run(command, cwd=cwd, capture_output=True, text=True, check=True, shell=True, encoding='utf-8', errors='replace')
        return result.stdout.strip()
    except subprocess.CalledProcessError as e:
        print(f"Error running command: {command}")
        print(f"Stdout: {e.stdout}")
        print(f"Stderr: {e.stderr}")
        return None
    except Exception as e:
        print(f"An unexpected error occurred while running command: {command}")
        print(f"Error: {e}")
        return None

def get_last_commit_message(file_path):
    # Replace backslashes with forward slashes for git command
    normalized_file_path = file_path.replace('\\', '/')
    cmd = "git log -1 --pretty=%B -- \"{}\"".format(normalized_file_path)
    return run_command(cmd)

def fetch_problem_info(problem_id):
    url = f"{SOLVED_AC_API_URL}?problemIds={problem_id}"
    headers = {"Accept": "application/json"}
    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()  # Raise an exception for HTTP errors
        data = response.json()
        # If data is a list, take the first item. Otherwise, assume it's a dict with 'items'
        if isinstance(data, list) and data: # If it's a non-empty list
            return data[0]
        elif isinstance(data, dict) and data.get("items"): # If it's a dict with 'items'
            return data["items"][0]
        return None
    except requests.exceptions.RequestException as e:
        print(f"Error fetching problem {problem_id} from solved.ac: {e}")
        return None

def create_commit_message(problem_info):
    title = problem_info.get("title", "Unknown Title")
    level = problem_info.get("level", 0)
    tags = [tag["displayNames"][0]["name"] for tag in problem_info.get("tags", []) if tag.get("displayNames")]
    
    tier = get_tier_from_level(level)
    tags_str = "/".join(tags) if tags else "No Tags"
    
    return f"[{tier}, {tags_str}] {title}"

def modify_file_trivially(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Add a newline if not present, or remove if already present and then add
        if content.endswith('\r\n'):
            content = content.rstrip('\r\n')
        else:
            content += '\r\n'
            
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(content)
        return True
    except Exception as e:
        print(f"Error modifying file {file_path}: {e}")
        return False

def main():
    current_dir = os.getcwd()
    boj_path = os.path.join(current_dir, BOJ_DIR)

    if not os.path.isdir(boj_path):
        print(f"Error: {boj_path} directory not found.")
        return

    processed_files = []
    skipped_files = []
    
    for filename in os.listdir(boj_path):
        file_path = os.path.join(boj_path, filename)
        
        if not os.path.isfile(file_path):
            continue
            
        # Extract problem ID from filename (e.g., 1002.py -> 1002)
        match = re.match(r'(\d+)\.py$', filename)
        if not match:
            print(f"Skipping non-problem file: {filename}")
            continue
        
        problem_id = match.group(1)
        
        print(f"Processing {filename} (Problem ID: {problem_id})...")
        
        last_commit_msg = get_last_commit_message(file_path)
        if last_commit_msg and last_commit_msg.startswith('[') and ']' in last_commit_msg:
            print(f"  Skipping {filename}: Already has a formatted commit message.")
            skipped_files.append(filename)
            continue
            
        problem_info = fetch_problem_info(problem_id)
        if not problem_info:
            print(f"  Skipping {filename}: Could not fetch problem info.")
            skipped_files.append(filename)
            continue
            
        commit_msg = create_commit_message(problem_info)
        
        if not modify_file_trivially(file_path):
            print(f"  Skipping {filename}: Failed to modify file.")
            skipped_files.append(filename)
            continue
            
        # Write commit message to a temporary file
        commit_msg_file_path = os.path.join(current_dir, COMMIT_MESSAGE_FILE)
        try:
            with open(commit_msg_file_path, 'w', encoding='utf-8') as f:
                f.write(commit_msg)
        except Exception as e:
            print(f"  Error writing commit message file for {filename}: {e}")
            skipped_files.append(filename)
            continue
            
        # Stage and commit
        commit_cmd = f"git add \"{file_path}\" && git commit -F \"{commit_msg_file_path}\""
        commit_result = run_command(commit_cmd)
        
        if commit_result:
            print(f"  Successfully committed {filename}.")
            processed_files.append(filename)
        else:
            print(f"  Failed to commit {filename}.")
            skipped_files.append(filename)
            
        # Clean up temporary commit message file
        try:
            os.remove(commit_msg_file_path)
        except Exception as e:
            print(f"  Error deleting temporary commit message file: {e}")
            
        time.sleep(1) # Be kind to the API
        
    print("\n--- Summary ---")
    print(f"Processed {len(processed_files)} files:")
    for f in processed_files:
        print(f"  - {f}")
    print(f"Skipped {len(skipped_files)} files:")
    for f in skipped_files:
        print(f"  - {f}")

if __name__ == "__main__":
    main()