#!/bin/bash
excludes="$(cat "scripts/lint_folder_excludes")"
docker run -e RUN_LOCAL=true -e FILTER_REGEX_EXCLUDE="$excludes" -v "${1:-$("pwd" "${BASH_SOURCE[0]}")}":/tmp/lint github/super-linter:v4.8.1
