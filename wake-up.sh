#!/bin/bash
cd /home/kart2000/project/autonomous-project

opencode run "Read GOAL.md, STATE.md (if it exists), and DECISIONS.md (if it exists) 
to understand the project and what has been done so far.
Then decide ONE small, specific task to do next that moves the project forward.
Do that task: write the code, run any tests, and fix issues if tests fail.
Update STATE.md with what you did and the current status.
If you made any notable decision or tradeoff, add a note to DECISIONS.md.
Then commit your changes with a clear commit message." --auto

git push origin main
