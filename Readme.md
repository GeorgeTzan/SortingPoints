## Πρόγραμμα Ταξινόμησης Σημείων

Αυτό το repository περιλαμβάνει προγραμμάτα που διαβάζουν σημέια απο ένα αρχειο, τα ταξινομούν με quicksort με βάση την απόστασή τους απο την αρχή (0, 0, 0) και γράφουν τα ταξινομημένα σημεία στο output.txt. Τα προγράμματα έχουν υλοποιηθεί σε Python (με και χωρίς NumPy), C & Haskell.

- [Instalation](#Installation)
    - [Python - Numpy](#Python-With-Numpy)
    - [Python](#Python-Without-Numpy)
    - [Haskell](#Haskell)
    - [C](#C)
- [Requirements](#Prerequisites)
- [License](#license)

### Prerequisites
- Python 3
- NumPy
- GCC (για την μεταγλώττιση του προγράμματος C)
- GHC (για την μεταγλώττιση του προγράμματος Haskell)

### Installation 
**Clone the Repository:**
   ```bash
   git clone https://github.com/GeorgeTzan/SortingPoints.git
   ```

## Python With Numpy
```bash
python3 sortWithoutNumpy.py -i input*.txt
```

## Python Without Numpy
```bash
python3 sortWithNumpy.py -i input*.txt
```

## Haskell
```bash
ghc -o sortWithHaskell sortWithHaskell.hs
./sortWithHaskell input*.txt output.txt
```

## C
```bash
gcc -o sortWithC sortWithC.c -lm
./sortWithC input*.txt
```

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.