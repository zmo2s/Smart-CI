import os
import subprocess
from collections import defaultdict

# Function to get the modified files from the git diff
def get_modified_files(diff_range):
    result = subprocess.run(["git", "diff", "--name-only", diff_range], capture_output=True, text=True)
    return [line.strip() for line in result.stdout.splitlines() if line.strip()]

# Function to extract required files from a test file
def extract_references_from_test_file(test_path):
    references = set()
    try:
        with open(test_path, 'r', encoding='utf-8') as f:
            for line in f:
                # Look for require() or import statements (e.g., import { something } from '../app.js')
                if 'require(' in line or 'import ' in line:
                    # Extract the path within the require or import statement
                    parts = line.split('(') if 'require(' in line else line.split('from')
                    for part in parts:
                        if '../' in part:  # This indicates a reference to a file in another directory
                            references.add(part.strip().strip('"').strip("'"))
    except Exception as e:
        print(f"Error reading test file {test_path}: {e}")
    return references
def file_exists_in_repo(file_path):
    return os.path.exists(file_path)


def clean_string(input_string):
    # Remove '..' and '/'
    cleaned_string = input_string.replace('..', '').replace('/', '').replace('\'', '').replace(';', '').replace(')', '')
    return cleaned_string


# Build the dependency map based on references to files outside of the test directory
def build_dependency_map():
    dep_map = defaultdict(list)

    # Scan the test directory for test files
    for root, _, files in os.walk("."):
        for file in files:
            if file.endswith(".test.js"):  # Only process test files
                test_file = os.path.join(root, file)
                #print(f"Processing test file: {test_file}")

                # Extract references to other files in the repository
                references = extract_references_from_test_file(test_file)
                
                # If the test file references something outside of test, add it to the map
                if references:
                    for ref in references:
                        dep_map[test_file].append(clean_string(ref))
    filtered_dep_map = {test_file: [ref for ref in refs if file_exists_in_repo(ref)] for test_file, refs in dep_map.items()}
    return dict(dep_map)

# CLI to demonstrate
def main():
    diff_range = "origin/main...HEAD"  # Adjust this range as needed
    #print("🔍 Getting modified files...")
    files = get_modified_files(diff_range)
    #print(f"✅ Modified files: {files}")

    #print("🌳 Building dependency map...")
    dep_map = build_dependency_map()
    #print(f"Dependency map: {dep_map}")

    #print("🧠 Analyzing impacted files...")
    impacted_files = []
    for file in files:
        for test_file, refs in dep_map.items():
            # Check if any reference in the dependency map is in the modified files list
            if any(ref in file for ref in refs):  # If a modified file matches a reference
                impacted_files.append(test_file)

    #print(impacted_files)
    #if impacted_files:
        #for test in impacted_files:
            #print(f"- {test}")
    #else:
        #print("✅ No impacted tests detected.")
    
    separated_files = []
    separated_files = set()  # Using a set to avoid duplicates
    for file in impacted_files:
        parts = file.split('/')
        if len(parts) > 1:
            separated_files.add(parts[2])  # This will add the second part of the path

    # Print the separated second parts without duplicates
    for part in separated_files:
        print(f"- {part}")

if __name__ == "__main__":
    main()
