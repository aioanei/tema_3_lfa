# Analizor pentru Gramatici Context-Free

Acest program implementează un analizor pentru gramatici independente de context (CFG) care poate verifica apartenența șirurilor și genera derivări.

## Funcționalități

- **Introducerea gramaticii**: Permite utilizatorului să introducă manual o gramatică CFG
- **Generarea șirurilor**: Generează exemple de șiruri care aparțin gramaticii
- **Verificarea apartenenței**: Verifică dacă un șir aparține limbajului generat de gramatică
- **Trasarea derivărilor**: Afișează pașii derivării pentru un șir dat

## Utilizare

### Rularea programului

```bash
python main.py
```

### Pașii de utilizare

1. **Introducerea simbolului de start**
   - Programul va cere să introduceți simbolul de start al gramaticii

2. **Introducerea regulilor de producție**
   - Formatul: `S -> aA | bbB`
   - Utilizați `#` pentru epsilon (șirul vid)
   - Apăsați Enter fără să introduceți nimic pentru a termina

3. **Vizualizarea exemplelor**
   - Programul va afișa 5 șiruri generate aleatoriu din gramatică

4. **Trasarea derivării**
   - Introduceți un șir pentru a vedea derivarea sa completă

5. **Verificarea apartenenței**
   - Introduceți un șir pentru a verifica dacă aparține gramaticii

## Exemple de teste

### Gramatica 1 (Șiruri simple)
```
Simbolul de start: S
Reguli:
S -> a | b
S -> aa | bb

Șiruri de test:
- a (valid)
- b (valid)
- aa (valid)
- bb (valid)
- ab (invalid)
```

### Gramatica 2 (Șiruri echilibrate)
```
Simbolul de start: S
Reguli:
S -> aSb | #

Șiruri de test:
- (șir vid) (valid)
- ab (valid)
- aabb (valid)
- aaabbb (valid)
- aab (invalid)
```

### Gramatica 3 (Gramatica complexă din cod)
```
Simbolul de start: S
Reguli:
S -> aSd | A
A -> bAcc | bcc

Șiruri de test:
- bcc (valid)
- abccd (valid)
- aabccdd (valid)
- bbcccc (valid)
- abc (invalid)
```

### Gramatica 4 (Palindroame)
```
Simbolul de start: S
Reguli:
S -> aSa | bSb | a | b | #

Șiruri de test:
- a (valid)
- aba (valid)
- ababa (valid)
- ab (invalid)
```

## Structura codului

### Clase principale

- **ContextFreeGrammar**: Clasa principală care reprezintă o gramatică CFG
  - `terminal_symbols`: mulțimea simbolurilor terminale
  - `variable_symbols`: mulțimea simbolurilor non-terminale
  - `rules`: dicționar cu regulile de producție
  - `start_symbol`: simbolul de start

### Funcții principale

- **apply_production_rule()**: Aplică o regulă de producție la un șir
- **verify_string_membership()**: Verifică dacă un șir aparține gramaticii
- **create_all_strings()**: Generează toate șirurile posibile până la o lungime dată
- **display_sample_outputs()**: Afișează exemple de șiruri generate

## Limitări

- Limita de adâncime pentru verificarea apartenenței: 12
- Limita de lungime pentru generarea șirurilor: 10
- Programul nu detectează gramatici infinite sau recursive stânga

## Cerințe

- Python 3.x
- Modulul `random` (inclus în Python standard)

## Note

- Simbolurile non-terminale trebuie să fie litere mari
- Simbolurile terminale pot fi orice caractere în afară de litere mari
- Utilizați `#` pentru a reprezenta epsilon (șirul vid)
- Separați alternativele cu `|` în regulile de producție
