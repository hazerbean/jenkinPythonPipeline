===============================
Build Configuration Walkthrough
===============================
Every CircleCI project requires a configuration file called .circleci/config.yml.
The following steps are made to create a complete config.yml file for simple-calc.


Specify a Version
-----------------
Every config.yml starts with the version key.
This key is used to issue warnings about breaking changes.

version: 2


Install Dependencies
--------------------
After choosing a job, create steps to run specific commands.
Use the checkout step to check out source code.
By default, source code is checked out to the path specified by working_directory.

version: 2
jobs:
  build:
    steps:
      - checkout  # checkout source code to working directory


Cache Dependencies
------------------
To save time between runs, consider caching dependencies or source code.
Use the save_cache step to cache certain files or directories.

jobs:
  build-and-test:
    executor: python/default
    steps:
      - checkout
      - python/load-cache
      - python/install-deps
      - python/save-cache


Run Tests
---------
Use the run step to run your test suite.

jobs:
  build-and-test:
    executor: python/default
    steps:
      - checkout
      - python/load-cache
      - python/install-deps
      - python/save-cache
      - run:
          command: python tests.py
          name: Test


Define Workflows
----------------
Finally, we define a workflow to execute the above steps.

workflows:
  main:
    jobs:
      - build-and-test
