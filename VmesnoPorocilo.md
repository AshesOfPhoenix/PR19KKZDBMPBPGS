# Vmesno poročilo o opravljenem delu

Datum oddaje poročila: 2.4.2020

Avtorji:

- Kristjan Križman,
- Boštjan Perkan,
- Gregor Šink,
- Martin Potočan,
- Žan Dodič Bržan.

Mentor:

- doc. dr. Tomaž Curk

## Opis Problema

Za problem smo si izbrali bolj raziskovalno nalogo. Zadali smo si da bomo še več raziskovali po svetu filmov in seriji. V domači nalogi smo se spoznali z eno bazo takega tipa podatkov, podobno naši zadani raziskovalni nalogi, vendar so bli podatki starejši ter pomanjkljivi.

Torej za začetek smo si izbrali par nalog, ki jih želimo rešit oziroma raziskat:

- Poiskat filme z največ zaslužka
- Najbolj popularne filme ( Na Netflixu oz. kjerkoli)
- Ali so filmi oz. serije od Netflixa slabši kot navadni filmi (iste žanre npr.)
- Kako se je spreminjala količina filmov in seriji na Netflixu
- Najbolj gledane žanre
- in še več nalog si bomo zadali do končnega poročila.

## Podatki

Podatke jemljemo iz treh različnih virov:

- Netflixova (officialna) baza z kaggla kjer so meli tekmovanje (<https://www.kaggle.com/netflix-inc/netflix-prize-data)>
Datoteka "training_set.tar" je imenik, ki vsebuje 17770 datotek, eno
na film. Prva vrstica vsake datoteke vsebuje ID filma, ki mu sledi vrstica.
Vsaka naslednja vrstica v datoteki ustreza oceni stranke in datum v naslednji obliki:

    CustomerID,Rating,Date

    MovieIDs range from 1 to 17770 sequentially.

    CustomerIDs range from 1 to 2649429, with gaps. There are 480189 users.

    Ratings are on a five star (integral) scale from 1 to 5.

    Dates have the format YYYY-MM-DD.

- IMDB baza z imdb.com spletne strani (<https://www.imdb.com/interfaces/https://www.imdb.com/interfaces/)>

- Ter še ena Netflixova baza z kaggla vendar neuradna (<https://www.kaggle.com/shivamb/netflix-shows)>

## Priprava podatkov
    Za začetek smo prebrali posebej prebrali netflix_titles.csv ter vse IMDB csv datoteke. Ustvarili smo svoj csv file kjer smo vse neznane direktorje v netflixu probali najti te direktorje v IMDB bazi ter prazne prostore tako nadomestili z imenom oz -1, če ta direktor tega filma sploh ne obstaja. Datoteko smo še izvozili ter z njim delali v nadalnjih raziskavah.
## Glavne Ugotovitve

Zaenkrat imamo par ugotovitev, kot so:

- Amerika ma največ filmov, in za njo je Indija
- Če delimo podatke na dva tipa torej filmi in serije, Netflix vsebuje kar 40% serij
- Najboljše ocenjen filem na Netflixu je God of War
- Najboljše ocenjena serija na Netflix je Planet Earth II

## Izvedene analize in zanimivi rezultati

- V datoteki taksB.ipynb
