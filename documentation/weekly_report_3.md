# Week 3

## What did I do this week?

Implemented the trie structure and added the first version for generating haikus + a bunch of tests for the new classes

## How has the program progressed?

Solid progress at least compared to last week. The core logic seems to be working, and the user is now able to generate valid(ish) haikus from the UI. Still plenty of room for improvement, though. For example the input file is hard coded for the time being and the haiku logic itself still need some refinement.

## Was there something that felt difficult, or that was left unclear?

Maybe still a bit unclear, if it's ok to import for example `random` or should there be a hand-crafted implementation? I'm currently using `random.choices` as a helper when generating new words based on the weight.

## What's next?

Refining the haiku logic and formatting (for example suffixes shoudn't be allowed as first words of a line, extra white spaces need to be removed etc.). Adding more tests and documentation (inside the code as well). Adding more options to the UI, maybe moving away from a text based UI if there's time. Also aiming to improve error handling, and might restructure a bit - there's currently maybe a bit too much stuff in `haiku_generator.py`

## Time spent on the project during this week

Approximately 15-20 hours in total this week, didn't keep close count.
