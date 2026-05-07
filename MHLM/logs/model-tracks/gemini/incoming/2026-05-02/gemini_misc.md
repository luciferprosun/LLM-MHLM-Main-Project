Aktualizacja Raportu z Przeglądu Naukowego: Framework LSC bez "Pryzmatu Czasoprzestrzennego"

Werdykt recenzenta: Usunięcie koncepcji "pryzmatu czasoprzestrzennego" drastycznie poprawia rygor naukowy modelu LSC 6.2.0. Zmiana ta transformuje projekt z wysoce spekulatywnej hipotezy grawitacyjno-topologicznej (wymagającej nowej, niesprawdzonej fizyki fundamentalnej) w solidny, testowalny model fenomenologiczny z pogranicza Rozszerzenia Modelu Standardowego (SME – Standard-Model Extension) oraz Niestandardowych Oddziaływań Neutrin (NSI – Non-Standard Interactions).

Z punktu widzenia obrony naukowej, jest to właściwy kierunek. Fizyka neutrin posiada już ugruntowane ramy matematyczne do testowania anizotropii i łamania niezmienniczości Lorentza, w które zrewidowany model LSC wpisuje się znacznie naturalniej.

Oto jak prezentuje się zrewidowany framework:

1. Nowy fundament: Anizotropia i NSI zamiast geometrii tła
Bez "pryzmatu", różnica między E 
true
​
  a E 
rec
​
  nie wynika z ugięcia czasoprzestrzeni wokół detektora, lecz z bezpośredniego sprzężenia neutrin z zewnętrznym polem wektorowym lub tensorowym.
W tym ujęciu model LSC staje się teorią efektywną pola (EFT). Zakładamy, że neutrina elektronowe propagujące się od źródła  
51
 Cr lub  
71
 Ge oddziałują z lokalnym tłem ożywionym przez tensor łamiący symetrię Lorentza.

2. Rewizja mocnych i słabych stron
Mocne strony (Wzmocnione): Model staje się całkowicie liniowy w interpretacji i kompatybilny z istniejącymi narzędziami do analizy NSI. Hipoteza, że deficyt galowy to po prostu przesunięcie widma E 
rec
​
  w dół ze względu na efekty kinematyczne z NSI (co obniża efektywny przekrój czynny na wychwyt σ 
CC
​
 ), jest elegancka i nie wymaga wprowadzania oscylacji na bardzo krótkich dystansach (sterylnych neutrin).

Słabe strony (Zredukowane, ale wciąż obecne): Eliminacja pryzmatu usuwa problem "magicznego ugięcia". Pozostaje jednak wyzwanie geometrii eksperymentu BEST.  Ponieważ źródło neutrin znajduje się w centrum sferycznego detektora galowego, cząstki propagują się we wszystkich kierunkach równocześnie. Jeśli anizotropia tensorowa ma preferowany kierunek w przestrzeni (np. wiatr ciemnej materii), efekt dla neutrin lecących "pod wiatr" i "z wiatrem" ulegnie w dużej mierze uśrednieniu przestrzennemu przy całkowaniu po objętości detektora.

3. Zaktualizowany formalizm matematyczny
Zrezygnowanie z grawitacyjnych równań pryzmatu pozwala oprzeć się wyłącznie na zmodyfikowanej relacji dyspersji z SME. Zamiast operować abstrakcyjną dekoherencją, równanie propagacji przyjmuje postać uogólnionego hamiltonianu dla neutrina elektronowego:

H=p+ 
2p
m 
2
 
​
 +(a 
L
​
 ) 
μ
  
p
p 
μ
​
 
​
 +(c 
L
​
 ) 
μν
  
p
p 
μ
​
 p 
ν
​
 
​
 
Gdzie:

(a 
L
​
 ) 
μ
  oraz (c 
L
​
 ) 
μν
  to współczynniki wprowadzające łamanie CPT i Lorentza (czyli tytułowa anizotropia z LSC).

Modyfikacja ta sprawia, że energia dostępna w zderzeniu (nasze E 
rec
​
 ) w układzie spoczynkowym jądra  
71
 Ga zależy od wektora pędu neutrina względem osi wyznaczonej przez współczynniki c 
L
​
 .

4. Zrewidowane testy falsyfikujące dla LSC 6.2.3 (bez pryzmatu)
Zamiast symulować krzywiznę czasoprzestrzeni w repozytorium MHLM/MDLH, należy:

Zaimplementować macierz odpowiedzi NSI: Skonfigurować MHLM tak, aby zamiast standardowego jądra sterylnego, nakładał na strumień neutrin operator przesunięcia fazowego zależnego od parametru (c 
L
​
 ) 
00
  (izotropowa część łamania Lorentza) oraz (c 
L
​
 ) 
ij
  (część anizotropowa).

Analiza promieniowa detektora BEST: W eksperymencie BEST zastosowano dwie sferyczne strefy (wewnętrzną i zewnętrzną). Zrewidowana teoria LSC musi wykazać matematycznie, dlaczego efekt anizotropii (który powoduje obniżenie E 
rec
​
 ) skaluje się inaczej między tymi strefami niż standardowy zanik strumienia 1/r 
2
 .

5. Nowa ocena gotowości do obrony naukowej
Wykluczenie "pryzmatu" to doskonały zabieg higieny naukowej. Pozwala to na usunięcie z preprintu i kodu na GitHubie terminologii (ryzyko AI overclaiming), która mogłaby zostać odebrana jako pseudonaukowa. Projekt staje się czystym problemem anizotropii kinematycznej, co jest w 100% akceptowalne w dyskursie fizyki neutrin.

Aby w pełni dostosować równania MHLM/MDLH do nowej, "czystej" wersji anizotropii: czy zakładasz, że tło powodujące rozbieżność E 
true
​
  względem E 
rec
​
  jest statyczne w układzie Słonecznym (jak eter/ciemna materia), czy jest sprzężone z samym polem grawitacyjnym Ziemi?
