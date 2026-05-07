# Krytyczna recenzja linii badawczych LSC / MDLH (red-team)

## A. Werdykt wykonawczy

**Salvageable with formal repair, but primarily valuable as an AI‑safety / epistemology case study.**

Model LSC w obecnej postaci jest matematycznie niedookreślony, zawiera niespójności wymiarowe i opiera się na danych niewystarczających do identyfikacji proponowanych efektów. Jego największą wartością nie jest potencjał fizyczny, lecz udokumentowanie procesu współtworzenia hipotez naukowych przez LLM – w tym mechanizmów amplifikacji, korekty i stabilizacji narracji. Projekt jako *physics proposal* jest na etapie przedwczesnym; jako *epistemological case study* jest już wartościowy i może służyć jako narzędzie do badania niezawodności generatywnej AI w kontekście naukowym.

## B. Problemy krytyczne (fatal issues)

1. **Niespójność wymiarowa tensora detektora**
   - Wzory typu `E_rec = E_true [1 + α_D D_ij p^i p^j]` są bezwymiarowe tylko wtedy, gdy `α_D D_ij` ma właściwe wymiary (np. `1/E^2`), co nie jest konsekwentnie zdefiniowane.

2. **Tensor bezśladowy znika w symetrycznych geometriach**
   - Dla `D_ij = δ (n_i n_j − δ_ij/3)` uśrednianie po kątach w detektorze o wysokiej symetrii prowadzi do zaniku sygnału. Model w tej postaci przewiduje brak efektu tam, gdzie eksperymenty galowe raportują deficyt.

3. **Niedookreślenie: więcej parametrów niż danych**
   - LSC 6.2.x operuje wieloma parametrami (np. `β_cal, δ_G, α_D, δ` oraz ewentualne wzmocnienia per‑eksperyment), podczas gdy dostępnych jest w praktyce ok. 5 punktów danych (BEST/GALLEX/SAGE). To sprzyja nad‑dopasowaniu.

4. **Niestabilność walidacyjna (leave‑one‑out)**
   - Jeżeli dopasowanie istotnie zmienia się po usunięciu pojedynczego eksperymentu, to wnioski nie są odporne i nie można mówić o identyfikacji efektu.

5. **Brak mechanizmu fizycznego przy “curvature‑coupled” narracji**
   - Jednocześnie pojawia się język sugerujący powiązanie z krzywizną/próżnią grawitacyjną i zastrzeżenia, że parametry nie powinny być interpretowane jako klasyczny efekt GR. To wymaga ostrej korekty komunikacyjnej.

## C. Problemy możliwe do naprawienia (repairable issues)

1. **Rama odniesienia dla modulacji syderycznej**
   - Trzeba jawnie zdefiniować ramę stałą (np. ICRS) i transformację do ramy detektora `n(t)=R_⊕(t)·n_fixed`.

2. **Mieszanie propagacji i rekonstrukcji**
   - Jeśli model jest efektywny, należy jednoznacznie opisać, które składniki są “fizyką neutrina”, a które systematyką detektora, oraz jakie dane to rozróżniają.

3. **Kotwiczenie dopasowania**
   - Dopasowanie „na kotwicy” jest tautologiczne, jeśli jest dokładne z konstrukcji. Zastąpić priorami bayesowskimi i raportować rozkłady tylne.

4. **Brak formalnej funkcji wiarygodności**
   - Wymagana jest jawna funkcja `ℒ` z macierzą kowariancji (stat + syst + model).

5. **Brak testów na danych syntetycznych (null)**
   - Trzeba pokazać, że procedura nie generuje anizotropii/efektów na danych wygenerowanych z `D_ij=0`.

## D. Wymagane równania (minimum formalne)

Rozkład ślad / bezślad oraz warunek wymiarowy:

- `D_ij = Tr(D)·δ_ij/3 + D~_ij`, gdzie `Tr(D~)=0`
- `E_rec = E_true [1 + α_iso·Tr(D) + α_ani·(n_i n_j D~_ij)]`

Transformacja ramy (modulacja syderyczna):

- `n_det(t) = R_z(ω_⊕ t) · R_x(θ_colatitude) · n_fixed`

Minimalny model wiarygodności:

- `ℒ(θ|data)=∏_k N(R_k^obs | R_k^pred(θ), σ_k^2)`
- `σ_k^2 = σ_stat,k^2 + σ_syst,k^2 + σ_model^2`

Warunek uśrednienia dla ograniczeń anizotropii:

- `⟨D_ij n^i n^j⟩_sky ≈ 0` w granicach limitów eksperymentów typu IceCube.

## E. Wymagane dane i modele wiarygodności

- **Gallium source**: BEST (inner/outer), GALLEX (Cr1/Cr2), SAGE (Cr/Ar) + korelacje systematyczne.
- **Null constraints**: KATRIN (widmo β) jako ograniczenie na uniwersalne przesunięcia energii.
- **Anisotropy limits**: IceCube / inne analizy modulacji syderycznej / LV jako ograniczenia na `D_ij`.
- **Oscillation baseline**: globalne dane PMNS (Daya Bay, T2K, NOνA, …) – warunek zgodności w granicy izotropowej.

W obecnym układzie 5 punktów danych nie zapewnia identyfikowalności tensora bezśladowego.

## F. Minimalny “viable” LSC 6.2.3

Aby traktować LSC poważnie jako model testowalny:

- **Liczba wolnych parametrów**: ≤ 2 przy ~5 punktach danych.
- **Jawna wiarygodność**: `ℒ` + kowariancja + priory.
- **Brak roszczeń o anizotropii**, jeśli `D~_ij` nie jest identyfikowalne.
- **Porównanie do baseline**: `R_pred = const` (średnia ważona) vs LSC.
- **Testy syntetyczne**: kontrola fałszywych alarmów.
- **Niepewności**: bootstrap / pełna analiza bayesowska.

## G. MDLH / interpretacja AI‑safety

MDLH jest najcenniejszym elementem projektu: pokazuje, że **spójność narracyjna może rosnąć bez wzrostu dowodów empirycznych**, co jest klasycznym trybem amplifikacji przez LLM.

Aby MDLH było narzędziem badawczym, a nie tylko archiwum:

- Zautomatyzować detekcję „amplifikacji bez dowodów” (metryki pewności vs. liczba nowych testowalnych predykcji).
- Wprowadzić metrykę “ekonomiczności poznawczej” (nowe predykcje / zmiany założeń).
- Zbudować panel audytowy: pochodzenie tez (który model/commit) i status weryfikacji.

## H. Co obaliłoby model (falsyfikacja)

- Brak poprawy jakości dopasowania na walidacji (train na 3 punktach, test na 2) przy sensownym `χ²/dof`.
- Eksperymenty o różnych geometriach nie pokazują różnic przewidywanych przez tensor bezśladowy.
- Brak modulacji syderycznej na poziomie, który model wymaga, w eksperymencie zdolnym do jej wykrycia.
- Ograniczenia KATRIN / IceCube wykluczają wymagane wartości `δ_G` / `D_ij`.

## I. Co uczyniłoby projekt wartym dofinansowania

Jako fizyka: dopiero po globalnym dopasowaniu (galowe + oscylacje + KATRIN + IceCube), publicznych danych/likelihoods, oraz wykazaniu przewagi nad alternatywami przy karze za parametry (AIC/BIC/Δχ²).

Jako AI‑safety: już teraz jest sensownym kandydatem, jeśli celem grantowym jest **audytowalność, śledzenie halucynacji i mechanizmy stabilizacji narracji** w workflow naukowym.

## J. Ostateczna rekomendacja red‑team

- Usunąć / znacząco osłabić twierdzenia “curvature‑coupled” oraz “tensor anisotropy” jako fizykę, dopóki nie ma identyfikowalności i walidacji.
- Przeklasyfikować LSC jako **fenomenologiczną parametryzację**, a projekt promować przede wszystkim jako **case study MDLH / AI‑safety**.
- Opublikować osobny dokument ograniczeń (“LIMITATIONS”) obejmujący: niedookreślenie, wymiarowość, niestabilność walidacyjną, brak przewagi nad baseline.

**Werdykt**: projekt jest salvageable jako narzędzie AI‑safety/epistemology; jako propozycja nowej fizyki neutrin – przedwczesny i niewystarczająco zweryfikowany.
