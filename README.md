# dot_problem
this is a proposition for a python implementation of a program that will search for available path to solve what i call very unoriginally "the dot problem". 
This has been made in the context of the folowing reddit post : https://www.reddit.com/r/numberphile/comments/ms24cn/does_this_dot_path_puzzlesequencewhatever_exist/

by u/booker_vincent :
"""
Does this dot path puzzle/sequence/whatever exist somewhere?

So, I came up with this little puzzle thing that I can do to pass the time, and I realized it seems very much like something that would appear on numberphile. 
Something like trying to figure out how many knots there are for every crossing number, how many ways there are to arrange any number of circles, or the 4 4s puzzle. 
Have you guys seen this somewhere?

Description: You have some number of dots arranged one after another in a line. 
Your goal is to jump from one to another (I do it by simply drawing a semi circle), not touching any dot twice, until you have touched reached all of the dots once. 
You're trying to figure out how many truly unique paths there are for each number of dots.

Rules: You cannot touch any given dot twice. Mirror images of a path don't count as unique paths. Reversed directions don't count as unique paths. 
*IMPORTANT* You cannot jump from whatever dot you're at to one of the dots immediately to your right or left. Every jump MUST skip at least one dot. 
(kind of the whole point of the puzzle)

This is super fun, and in principle you can do it forever for every number of dots.

I find it hard to believe that I'm the only one who has discovered this puzzle, because it seems like a fairly simple premise.
"""

be carefull, this code is not optimised to be fast and it has hard time when you start going above a value of 9 points.
I have tried to optimise it with mumba (using the @jit(nopython=True) decorator) but i got no results.
If you know how to do it feel free to make a pull request and/or contact me.
This code is under no Licence. It is free to use for any purpose.
