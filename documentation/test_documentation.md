# Test Documentation

## Unit tests

Unit testing is done with automated tests using Pytest. The UI is excluded from the coverage reports, and there are no unit tests for the UI.

### Running the tests

If it's your first time running the tests, make sure you have all the needed dependencies installed by running

`poetry install`

Run tests:

`poetry run invoke test`

Generate test coverage report:

`poetry run invoke coverage-report`

### Test Coverage

<img width="856" alt="Screenshot 2022-08-27 at 18 39 46" src="https://user-images.githubusercontent.com/32310572/187037315-691caa10-1df8-43e1-82f1-d53b2b95e1c0.png">

## Code quality

Code quality is monitored and measured with pylint. The configuration can be found in the [.pylintrc](https://github.com/picada/haikov/blob/main/.pylintrc) file. The UI and the tests are excluded from the style checks.

### Running the style checks

Install the needed dependendies (if not done before)

`poetry install`

Run style checks:

`poetry run invoke lint`

The current code quality score is 9.95/10.0.

## Manual testing

The program has been tested manually with different kinds of input and settings. As there are no automatic unit tests for the UI, testing this part of the program lies also heavily on manual testing.

Manual testing included testing the quality, grammatical structure and similarities to the input data. The exceptation was, that with higher orders of Markov chains results in a more grammatically correct results, but at the same time the generated text is often very similar to the input data.

The results were very much in line with the expectations. For example when the order is set to two, there is more variation in the results compared to the input data, but the substance might not always make sense - although in poetry this isn't necessarily that bad, opposed to "normal" text generation. Then again when the order is set to three, the substance quality might be slightly better, but when comparing to the input we can see, that we're just repeating the input data.

The examples below are generated using `poems_by_emily_dickinson.txt` as the input file.

**Second order:**

Idle hand it has     
a simple arrow sped by    
an archer's bow     

By comparing the results to the input data we can see, that this specific poem was generated as a combination of these two verses from two different poems, "Dead" and "XI".

"...   
Some touch it and some kiss it,   
Some chafe its **idle hand;   
It has a simple** gravity  
I do not understand!   
..."   

"...   
Fell, they will say, in 'skirmish'!   
Vanquished, my soul will know,
By but a simple **arrow   
Sped by an archer's bow.**   
..."   

**Third order:**   

Yesterday, just as   
the dusk was brown, one little   
boat gave up its strife   

In this case we can see, that this is just a direct segment from the poem "XLVII":

"Adrift! A little boat adrift!   
And night is coming down!   
Will no one guide a little boat   
Unto the nearest town?   

So sailors say, on **yesterday,   
Just as the dusk was brown,   
One little boat gave up its strife,**.  
And gurgled down and down.   

But angels say, on yesterday,   
Just as the dawn was red,   
One little boat o'erspent with gales   
Retrimmed its masts, redecked its sails   
Exultant, onward sped!!"      

However, partly because choosing to store commas as a separate node in the trie, there might be some variation also when using the third order, as for example in the haiku below:

Slips away upon   
an ether sea, and yet the   
crowd applauds below   

In this example which are combined by the segment "and ," which has more options for the next word because of its frequency.

The first part comes from the poem "Sunset", and the second one from the poem "The Balloon".

"...   
A sloop of amber **slips away   
Upon an ether sea,   
And** wrecks in peace a purple tar,   
The son of ecstasy.   
..."   

"...   
Their ribbons just beyond the eye,   
They struggle some for breath,   
**And yet the crowd applauds below; **  
They would not encore death.   
..."   

Expanding the size of the input data also results in more variation, even with higher orders, since there are more possible options in the trie. For example below we have an example generated with the source data `combined.txt` which contains the texts in the following files:

`a_hundred_and_seventy_chinese_poems_by_various.txt`   
`collected_poems_by_alfred_noyes.txt`   
`kalevala_in_english.txt`   
`lyrical_ballads.txt`   
`poems_by_emily_dickinson.txt`   
`trees_and_other_poems_joyce_kilmer.txt`   

Inspiring, hastened   
to the deadly hilt, and hurled   
the net of mortal   

In this exapmle which uses the third order we can identify four different poems from the source data: "Origin of the Serpent" and "Restoration of the Sun and Moon" from Kalevala and "Book VIII" and "The Net of Vulcan" by Alfred Noyes

"...   
Then the reckless Lemminkainen   
Ate his meat with beer **inspiring,   
Hastened to** his bath awaiting;   
Only was the bullfinch bathing,   
With the many-colored bunting;   
..."   

"...   
To the court-yard rushed the heroes,   
**Hastened to the deadly** combat,   
On the plains of Sariola.   
Wainamoinen, the magician,   
Strikes one blow, and then a second,   
Strikes a third time, cuts and conquers.   
..."   

"...   
With Spain, against him, up **to the deadly hilt,**   
**And hurled** him into the Tower.   
..."   

"...   
From peaks that clove the heavens asunder   
The hunchback god with sooty claws   
Loomed o'er the night, a cloud of thunder,   
**And hurled the net of mortal laws;**  
It flew, and all the world grew dimmer;   
Its blackness blotted out the stars,   
Then fell across the rosy glimmer   
That told where Venus couched with Mars.   
..."   
