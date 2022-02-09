set /p excludes=<lint_folder_excludes
docker run -e RUN_LOCAL=true -e FILTER_REGEX_EXCLUDE=%excludes% -v %~dp0..:/tmp/lint github/super-linter:v4.8.1
