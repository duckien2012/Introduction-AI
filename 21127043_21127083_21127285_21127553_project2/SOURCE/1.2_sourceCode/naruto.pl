%male
male(hagoromo_otsutsuki).
male(hamura_otsutsuki).
male(patriarch_clan_otsutsuki).
male(indra_otsutsuki).
male(asura_otsutsuki).
male(tajima_uchiha).
male(fugaku_uchiha).
male(kagami_uchiha).
male(madara_uchiha).
male(izuna_uchiha).
male(ashina_uzumaki).
male(butsuma_senju).
male(itama_senju).
male(kawarama_senju).
male(hashirama_senju). 
male(tobirama_senju).
male(hyuga_elder).
male(shisui_uchiha).
male(hiashi_hyuga).
male(hizashi_hyuga).
male(ise).
male(minato_namikaze).
male(itachi_uchiha).
male(sasuke_uchiha).
male(nagato_uzumaki).
male(naruto_uzumaki).
male(neji_hyuga).
male(toneri_otsutsuki).
male(boruto_uzumaki).

%female
female(mikoto_uchiha). 
female(kaguya_otsutsuki).
female(mito_uzumaki).
female(kushina_uzumaki).
female(fuso_uzumaki). 
female(hinata_hyuga). 
female(hanabi_hyuga).
female(sarada_uchiha).
female(himawari_uzumaki).
female(sakura_haruno).

%otsutsuki
otsutsuki(kaguya).
otsutsuki(hagoromo).
otsutsuki(hamura).
otsutsuki(patriarch_clan).
otsutsuki(indra).
otsutsuki(asura).
otsutsuki(toneri).

%uzumaki 
uzumaki(ashina).
uzumaki(nagato).
uzumaki(naruto).
uzumaki(boruto).
uzumaki(kushina).
uzumaki(fuso).
uzumaki(himawari).

%uchiha 
uchiha(tajima).
uchiha(fugaku).
uchiha(itachi).
uchiha(sasuke).
uchiha(kagami).
uchiha(madara).
uchiha(izuna).
uchiha(shisui).
uchiha(mikoto).

%hyuga
hyuga(hiashi).
hyuga(neji).
hyuga(hizashi).
hyuga(hinata).
hyuga(hanabi).

%married
married(fugaku_uchiha,mikoto_uchiha).
married(mikoto_uchiha,fugaku_uchiha).
married(ise,fuso_uzumaki).
married(fuso_uzumaki,ise).
married(naruto_uzumaki,hinata_hyuga).
married(hinata_hyuga,naruto_uzumaki).
married(sasuke_uchiha,sakura_haruno).
married(sakura_haruno,sasuke_uchiha).
married(kushina_uzumaki,minato_namikaze).
married(minato_namikaze,kushina_uzumaki).

%parent
parent(kaguya_otsutsuki,hagoromo_otsutsuki).
parent(kaguya_otsutsuki,hamura_otsutsuki).
parent(hagoromo_otsutsuki,indra_otsutsuki).
parent(hagoromo_otsutsuki,asura_otsutsuki).
parent(hamura_otsutsuki,hyuga_elder).
parent(hamura_otsutsuki,patriarch_clan_otsutsuki).
parent(hyuga_elder,hiashi_hyuga).
parent(hyuga_elder,hizashi_hyuga).
parent(kagami_uchiha,shisui_uchiha).
parent(hiashi_hyuga,hinata_hyuga).
parent(hiashi_hyuga,hanabi_hyuga).
parent(hizashi_hyuga,neji_hyuga).
parent(patriarch_clan_otsutsuki,toneri_otsutsuki).
parent(indra_otsutsuki,tajima_uchiha).
parent(indra_otsutsuki,fugaku_uchiha).
parent(indra_otsutsuki,kagami_uchiha).
parent(tajima_uchiha,madara_uchiha).
parent(tajima_uchiha,izuna_uchiha).
parent(asura_otsutsuki,butsuma_senju).
parent(asura_otsutsuki,ashina_uzumaki).
parent(asura_otsutsuki,kushina_uzumaki).
parent(asura_otsutsuki,fuso_uzumaki).
parent(butsuma_senju,kawarama_senju).
parent(butsuma_senju,itama_senju).
parent(butsuma_senju,tobirama_senju).
parent(butsuma_senju,hashirama_senju).
parent(hashirama_senju,mito_uzumaki).
parent(ashina_uzumaki,mito_uzumaki).
parent(fugaku_uchiha,itachi_uchiha).
parent(fugaku_uchiha,sasuke_uchiha).
parent(mikoto_uchiha,itachi_uchiha).
parent(mikoto_uchiha,sasuke_uchiha).
parent(ise,nagato_uzumaki).
parent(fuso_uzumaki,nagato_uzumaki).
parent(naruto_uzumaki,boruto_uzumaki).
parent(naruto_uzumaki,himawari_uzumaki).
parent(hinata_hyuga,boruto_uzumaki).
parent(hinata_hyuga,himawari_uzumaki).
parent(sasuke_uchiha,sarada_uchiha).
parent(sakura_haruno,sarada_uchiha).
parent(minato_namikaze,naruto_uzumaki).
parent(kushina_uzumaki,naruto_uzumaki).

%died 
died(tajima_uchiha).
died(fugaku_uchiha).
died(kagami_uchiha).
died(madara_uchiha).
died(izuna_uchiha).
died(shisui_uchiha).
died(mikoto_uchiha).
died(minato_namikaze).
died(kushina_uzumaki).
died(itachi_uchiha).

%assualt
assualt(itachi_uchiha,tajima_uchiha).
assualt(itachi_uchiha,fugaku_uchiha).
assualt(itachi_uchiha,kagami_uchiha).
assualt(itachi_uchiha,izuna_uchiha).
assualt(itachi_uchiha,shisui_uchiha).
assualt(itachi_uchiha,mikoto_uchiha).
assualt(sasuke_uchiha,itachi_uchiha).

%bestfriend
bestfriend(shisui_uchiha,itachi_uchiha).
bestfriend(itachi_uchiha,shisui_uchiha).
bestfriend(naruto_uzumaki,sasuke_uchiha).
bestfriend(sasuke_uchiha,naruto_uzumaki).


son(X,Y):-parent(Y,X),male(X).
daughter(X,Y):-parent(Y,X),female(X).
child(Child, Parent) :-parent(Parent, Child).
brother(X,Y):-son(X,Z),(son(Y,Z);daughter(Y,Z)),X\=Y.
sister(X,Y):-daughter(X,Z),(daughter(Y,Z);son(Y,Z)),X\=Y.
father(X,Y):-parent(X,Y),male(X).
mother(X,Y):-parent(X,Y),female(X).
wife(X,Y):-married(Y,X),female(X).
husband(X,Y):-married(X,Y),male(X).
orphanage(X):-parent(Y,X),died(Y).
predecessor(X, Z) :- parent(X, Z).
predecessor(X, Z) :- parent(X, Y),predecessor(Y, Z).
husgrandpa(X,Y):-parent(X,Z),parent(Z,Y),male(Z),male(X).
husgrandma(X,Y):-parent(X,Z),parent(Z,Y),female(X),male(Z).
sibling(X,Y):-parent(Z,X),parent(Z,Y),X\=Y.
whiteeyes(X):-hyuga(X).
sharingan(X,Y,Z):-(bestfriend(X,Y);parent(Y,X)),assualt(X,Y),uchiha(Z).
uncle(U,T):-
  (brother(U,Z);sister(Z,U)),parent(Z,T);
  (sister(Z,U),husband(H,Z)),male(U).
aunt(A,T):-
  ((brother(Z,A);sister(A,Z)),parent(Z,T)),female(A);
  ((brother(Z,Y),wife(W,Y))),female(A).
cousin(C1,C2):-
  (parent(Pc1,C1),
  parent(Pc2,C2),
  sibling(Pc1,Pc2)). 
nephew(Ne,Ua):-
  uncle(Ua,Ne);
  aunt(Ua,Ne);
  sibling(Ua,P),parent(P,Ne),
  male(Ne).
niece(Ni,Ua):-
  uncle(Ua,Ni);
  aunt(Ua,Ni);
  sibling(Ua,P),parent(P,Ni),
  female(Ni).
%conre
conre(X,Y):-married(X,Z),daughter(Z,Y),male(X),X\=Z.
%condau
condau(X,Y):-married(X,Z),son(Z,Y),female(X),X\=Z.
%lucdaotiennhan 
lucdaotiennhan(X):-otsutsuki(X).



  















