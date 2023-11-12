% male
male(prince_Phillip).
male(prince_Charles).
male(captain_Mark_Phillips).
male(timothy_Laurence).
male(prince_Andrew).
male(prince_Edward).
male(prince_William).
male(prince_Harry).
male(peter_Phillips).
male(mike_Tindall).
male(james_Viscount_Severn).
male(prince_George).

%female
female(queen_Elizabeth_II).
female(princess_Diana).
female(camilla_Parker_Bowles).
female(princess_Anne).
female(sarah_Ferguson).
female(sophie_Rhys_jones).
female(kate_Middleton).
female(autumn_Kelly).
female(zara_Phillips).
female(princess_Beatrice).
female(princess_Eugenie).
female(lady_Louise_Mountbatten_Windsor).
female(princess_Charlotte).
female(savannah_Phillips).
female(isla_Phillips).
feamle(mia_Grace_Tindall).

%married
married(prince_Charles,camilla_Parker_Bowles).
married(timothy_Laurence,princess_Anne).
married(prince_Edward,sophie_Rhys_jones).
married(prince_William,kate_Middleton).
married(peter_Phillips,autumn_Kelly).
married(mike_Tindall,zara_Phillips).

%divorced
divorced(prince_Charles,princess_Diana).
divorced(captain_Mark_Phillips,princess_Anne).
divorced(prince_Andrew,sarah_Ferguson).

%parent
%parent : elizabeth and prince phillips
parent(prince_Phillip,prince_Charles).
parent(prince_Phillip,princess_Anne).
parent(prince_Phillip,prince_Andrew).
parent(prince_Phillip,prince_Edward).
parent(queen_Elizabeth_II,prince_Charles).
parent(queen_Elizabeth_II,princess_Anne).
parent(queen_Elizabeth_II,prince_Andre).
parent(queen_Elizabeth_II,prince_Edward).
%parent : prince charles and princess diana
parent(prince_Charles,prince_William).
parent(prince_Charles,prince_Harry).
parent(princess_Diana,prince_William).
parent(princess_Diana,prince_Harry).
%parent : princess anne and mark phillips
parent(captain_Mark_Phillips,peter_Phillips).
parent(captain_Mark_Phillips,zara_Phillips).
parent(princess_Anne,peter_Phillips).
parent(princess_Anne,zara_Phillips).
%parent: prince andrew and sarah ferguson
parent(prince_Andrew,princess_Beatrice).
parent(prince_Andrew,princess_Eugenie).
parent(sarah_Ferguson,princess_Beatrice).
parent(sarah_Ferguson,princess_Eugenie).
%parent: prince Edward and sophie
parent(prince_Edward,james_Viscount_Severn).
parent(prince_Edward,lady_Louise_Mountbatten_Windsor).
parent(sophie_Rhys_jones,james_Viscount_Severn).
parent(sophie_Rhys_jones,lady_Louise_Mountbatten_Windsor).
%parent : prince william and kate middleton
parent(prince_William,prince_George).
parent(prince_William,princess_Charlotte).
parent(kate_Middleton,prince_George).
parent(kate_Middleton,princess_Charlotte).
%parent: autumn kelly and peter phillips
parent(autumn_Kelly,savannah_Phillips).
parent(autumn_Kelly,isla_Phillips).
parent(peter_Phillips,savannah_Phillips).
parent(peter_Phillips,isla_Phillips).
%parent : zara phillips and mike tindall
parent(zara_Phillips,mia_Grace_Tindall).
parent(mike_Tindall,mia_Grace_Tindall).

husband(Person,Wife):- married(Person,Wife),male(Person).
wife(Person,Husband):- married(Person,Husband),female(Person).
father(Parent,Child):- parent(Parent,Child),male(Parent).
mother(Parent,Child):- parent(Parent,Child),female(Parent).
child(Child,Parent):- parent(Parent,Child).
son(Child,Parent):- parent(Parent,Child),male(Parent).
daughter(Child,Parent):- parent(Parent,Child),female(Child).

grandparent(GP,GC):-
     parent(GP,Person),
     parent(Person,GC).
grandmother(GM,GC):-
     female(GM),
     parent(GM,Person),
     parent(Person,GC).
grandfather(GF,GC):-
     male(GF),
     parent(GF,Person),
     parent(Person,GC).
grandchild(GC,GP):-
     parent(Person,GC),
     parent(GP,Person).
grandson(GS,GP):-
     male(GS),
     parent(Person,GS),
     parent(GP,Person).
granddaughter(GD,GP):-
     female(GD),
     parent(Person,GD),
     parent(GP,Person).
     
sibling(Person1,Person2):- parent(Person,Person1) ,parent(Person,Person2), Person1 \== Person2.
brother(Person,Sibling):- parent(Parent,Person),parent(Parent,Sibling),male(Person), Person\==Sibling.
sister(Person,Sibling):- parent(Parent,Person),parent(Parent,Sibling),female(Person), Person\==Sibling.
aunt(Aunt,NieceNephew) :-
    female(Aunt),
    parent(Parent,NieceNephew), % NieceNephew là con cái c?a Parent
    sibling(Parent,Aunt).  % Aunt là ch?/em c?a Parent
uncle(Uncle,NieceNephew) :-
    male(Uncle),
    parent(Parent,NieceNephew), % NieceNephew là con cái c?a Parent
    sibling(Parent,Uncle).  % Aunt là ch?/em c?a Parent
niece(Person,AuntUncle) :-
    female(Person),
    parent(Parent,Person), % Person là con c?a parent nào dó
    sibling(Parent,AuntUncle).  % mà parent dó là anh em c?a AuntUncle
niece(Person,AuntUncle) :-
    female(Person),
    parent(Parent,Person), % Person là con c?a parent nào dó
    sibling(Parent,AuntUncle).  % mà parent dó là anh em c?a AuntUncle


















