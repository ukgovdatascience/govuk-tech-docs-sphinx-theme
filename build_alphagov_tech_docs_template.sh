#!/bin/sh

# If `jq` is installed, get the latest commit hash from the `alphagov/tech-docs-template` repository using GitHub API
if hash jq 2>/dev/null ; then
  LATEST_COMMIT=$(curl https://api.github.com/repos/alphagov/tech-docs-template/commits/master -s | jq .sha -r)
  if [ ! $? -eq 0 ]; then
    echo 'Could not get latest commit hash from `alphagov/tech-docs-template` GitHub repository!'
    exit 1
  fi
else
  echo '`jq` package not installed! See https://stedolan.github.io/jq/'
  exit 127
fi

# Delete any existing local build of `alphagov/tech-docs-template`
if [ -d ${DIR_SOURCE_ALPHAGOV_TECH_DOCS_TEMPLATE} ]; then rm -rf ${DIR_SOURCE_ALPHAGOV_TECH_DOCS_TEMPLATE}; fi

# If `middleman` is installed, initialise the Middleman `alphagov/tech-docs-template` with some default settings, move
# into the local build directory, and build the template. Then delete everything except the `build` folder, and the
# `.template_version` file
if hash middleman 2>/dev/null ; then
  FIRST_TIME=true USE_PAAS=true APPLICATION_NAME=source CANONICAL_HOST=source middleman init ${DIR_SOURCE_ALPHAGOV_TECH_DOCS_TEMPLATE} -T alphagov/tech-docs-template &&
    cd ${DIR_SOURCE_ALPHAGOV_TECH_DOCS_TEMPLATE} &&
    bundle exec middleman build &&
    ls -A | grep -v 'build\|.template_version' | xargs rm -rf &&
    cd $(pwd)

  # Raise an error if the build does not complete
  if [ $? -ne 0 ]; then
    echo 'Could not build Middleman `alphagov/tech-docs-template` template!'
    exit 1
  fi

else
  echo 'Middleman is not installed! See https://github.com/alphagov/tech-docs-template'
  exit 127
fi
