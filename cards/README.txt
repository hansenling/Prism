I wrote this in Python. It's a small, object oriented task, so it was easy to do in this language. There are two classes, a 
Card class and a Deck class. These are two clear objects, so it was natural to create two classes to represents these. I changed
the tostrings of each of the classes to print out the names of the cards and a better representation of the cards in the deck. 
This makes testing easier. 

To quickly test the framework I would look at the cards in the deck before and after shuffling. I would call GetNextCard until the 
deck was empty to be sure it returned an error. I would try shuffling with a full, partially empty and empty deck. 

As for ambiguities, I just used a list to represent the deck and popped of the last element of the list for GetNextCard(). Shuffle
generates a new deck. 