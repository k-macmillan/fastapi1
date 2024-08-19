#! /usr/bin/bash

# Wrap each check so it hides the output unless there is failure
args_check=$(flake8 --select=DCO020 fastapi1)
if [[ $? == '1' ]]; then
    echo "flake8 check failed"
    echo $args_check
    exit 1
fi

mypy_check=$(mypy fastapi1 --strict)
if [[ $? == '1' ]]; then
    echo "mypy check failed"
    echo $mypy_check
    exit 1
fi

ruff_check=$(ruff check fastapi1)
if [[ $? == '1' ]]; then
    echo "ruff check failed"
    echo $ruff_check
    exit 1
fi

ruff_format=$(ruff format fastapi1)

echo -e "\nAll checks passed"
