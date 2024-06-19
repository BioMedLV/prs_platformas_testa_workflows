#!/bin/bash

# Determine the script's directory
project_dir=$(dirname $(realpath $0))

source "${project_dir}/venv/bin/activate" && python "${project_dir}/build_output.py" "${project_dir}"