use rand_mt::Mt64;
use rand::Rng;
use std::fs::File;
use std::io::{Write, BufWriter};
use rand::seq::SliceRandom; // Importujemy SliceRandom dla metody shuffle
use std::io;

fn generate_table (n: usize) -> Vec<usize> {
    let seed = rand::thread_rng().gen(); // Losowe ziarno
    let mut rng = Mt64::new(seed); // Generator inicjalizowany unikalnym ziarnem
    let mut A: Vec<usize> = (0..n).collect(); // Tworzymy wektor z liczbami od 0 do n

    A.shuffle(&mut rng); //Tasowanie tablicy A za pomoca algorytmu Fisher-Yates
    return A
}

fn insertion_sort(mut A: Vec<usize>, file: &mut BufWriter<File>, file2: &mut BufWriter<File>) -> Vec<usize> {
    let mut comparisons = 0; // Liczba porównań
    let mut shifts = 0;      // Liczba przestawień kluczy

    for j in 1..A.len() {
        let key = A[j];
        let mut i = j;

        while i > 0 { 
            comparisons += 1; // Zliczamy porównanie tutaj
            if A[i - 1] > key {
                A[i] = A[i - 1]; // Przesunięcie klucza
                shifts += 1;     // Zliczamy przestawienie tutaj
                i -= 1;
            } else {
                break; // Jeśli warunek nie spełniony, przerywamy
            }
        }
        A[i] = key; // Wstawiamy klucz na miejsce
    }

    // Zapisujemy wyniki do pliku na końcu funkcji
    writeln!(file, "{},{}",A.len(), comparisons).unwrap(); //porównania
    writeln!(file2, "{},{}",A.len(), shifts).unwrap(); //przestawienia

    A
}


fn main () {
    let n: usize = 11;
    let table = generate_table(n);
    let mut file = BufWriter::new(File::create("insertion_sort_comparsion.txt").unwrap()); //zlicza porownania
    let mut file2 = BufWriter::new(File::create("insertion_sort_shifts.txt").unwrap()); //zlicza przestawienia
    
    for n in (100..=10000).step_by(100) {
        for i in 0..5 {
            let mut table = generate_table(n);
            let sorted_table = insertion_sort(table, &mut file, &mut file2);
        }
    }
}