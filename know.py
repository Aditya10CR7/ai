% Define the male and female genders
male(john).
male(james).
male(peter).
female(jane).
female(lisa).
female(anne).

% Define the parent-child relationship
parent_of(john, james).
parent_of(john, jane).
parent_of(james, peter).
parent_of(jane, lisa).
parent_of(jane, anne).

% Define the spouse relationship
married(john, jane).

% Define the sibling relationship
sibling(X, Y) :- parent_of(Z, X), parent_of(Z, Y), X \= Y.

% Define the grandparent relationship
grandparent(X, Y) :- parent_of(X, Z), parent_of(Z, Y).

% Define the aunt/uncle relationship
aunt_or_uncle(X, Y) :- parent_of(Z, Y), sibling(X, Z).

% Define the cousin relationship
cousin(X, Y) :- parent_of(A, X), parent_of(B, Y), sibling(A, B).

% Define the query-based family relationship
family_relationship(X, Y, Relationship) :-
    parent_of(X, Y),
    Relationship = 'parent-child';
    parent_of(Y, X),
    Relationship = 'child-parent';
    married(X, Y),
    Relationship = 'spouse';
    married(Y, X),
    Relationship = 'spouse';
    sibling(X, Y),
    Relationship = 'sibling';
    grandparent(X, Y),
    Relationship = 'grandparent-grandchild';
    grandparent(Y, X),
    Relationship = 'grandchild-grandparent';
    aunt_or_uncle(X, Y),
    Relationship = 'aunt-uncle-niece-nephew';
    cousin(X, Y),
    Relationship = 'cousin'.
