#!/bin/bash
if [ $# != 2 ]; then
    echo "Usage: $0 <commit message> <project name>"
    exit 1
fi
echo $1 $2
git add *
git commit -m "$1"
git push https://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@github.com/ppsilv/$2.git
