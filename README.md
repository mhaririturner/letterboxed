NYT Letterbox solver

Not super effificent, and definitely not efficient for finding all possible solutions. Amortized complexity to find any minimally long solution is efficient.

I wasn't able to find a good dictionary for what words are actually allowable in the puzzle, so I'm just using some old scrabble dictionary. May generate solutions using words not allowed by puzzle.

Bunch of stuff is hardcoded and unoptimized, and word list is not optimized as well (2-letter words, and doubled letter words (eg "aardvark") can be pre-culled).
