#!/bin/bash

# Function to run a list of scripts
run_scripts() {
    # List of script files to run
    local scripts=("script1.sh" "script2.sh")

    for script in "${scripts[@]}"; do
        if [[ -x "$script" ]]; then
            echo "Executing $script..."
            ./"$script" # or you can use `bash $script` if execution permission is an issue
        else
            echo "Error: $script is not executable or not found"
        fi
    done
}

# Call the function
run_scripts
