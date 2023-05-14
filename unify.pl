# # Unifi cation is a process of making two diff erent logical atomic expressions identical
# by fi nding a substitution. Unifi cation depends on the substitution process.

# The UNIFY algorithm is used for unifi cation, which takes two atomic sentences and
# returns a unifi er for those sentences. Unifi cation is a key component of all
# fi rst-order inference algorithms. It returns fail if the expressions do not match with
# each other.

% Define parent relationships
parent(john, mary).
parent(john, peter).
parent(mary, ann).
parent(mary, kate).

% Define grandparent relationship
grandparent(X, Y) :-
  parent(X, Z),
  parent(Z, Y).

% Define sibling relationship
sibling(X, Y) :-
  parent(Z, X),
  parent(Z, Y),X\=Y.