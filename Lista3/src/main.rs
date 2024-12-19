use rand_mt::Mt64;
use rand::Rng;
use std::fs::File;
use std::io::{Write, BufWriter};

pub fn calculate(n_values: Vec<usize>, repeats: usize) {
    let mut an_file = BufWriter::new(File::create("an_results.txt").unwrap());
    let mut bn_file = BufWriter::new(File::create("bn_results.txt").unwrap());

    for &n in n_values.iter() {
        let mut rng = Mt64::default();

        for _ in 0..repeats {
            let mut urns_an = vec![0; n];
            let mut urns_bn = vec![0; n];
            let mut max_balls_an = 0;
            let mut max_balls_bn = 0;

            // Obliczamy a_n (po prostu dodajemy kule do urn losowo)
            for _ in 0..n {
                let urn = rng.gen_range(0..n);
                urns_an[urn] += 1;
                if urns_an[urn] > max_balls_an {
                    max_balls_an = urns_an[urn];
                }
            }

            // Obliczamy b_n (wrzucamy kule na podstawie reguły dwóch urn)
            for _ in 0..n {
                let urn1 = rng.gen_range(0..n);
                let mut urn2;
                loop {
                    urn2 = rng.gen_range(0..n);
                    if urn1 != urn2 {
                        break;
                    }
                }

                // Wybieramy urnę z mniejszą liczbą kul i dodajemy kulę
                if urns_bn[urn1] <= urns_bn[urn2] {
                    urns_bn[urn1] += 1;
                    if urns_bn[urn1] > max_balls_bn {
                        max_balls_bn = urns_bn[urn1];
                    }
                } else {
                    urns_bn[urn2] += 1;
                    if urns_bn[urn2] > max_balls_bn {
                        max_balls_bn = urns_bn[urn2];
                    }
                }
            }

            // Zapisujemy wyniki
            writeln!(an_file, "{} {}", n, max_balls_an).unwrap();
            writeln!(bn_file, "{} {}", n, max_balls_bn).unwrap();
        }
    }
}

fn main() {
    let n_values: Vec<usize> = (10000..=1000000).step_by(10000).collect(); // Zakres wartości n
    let repeats = 5; // Ilość powtórzeń dla każdej wartości n

    calculate(n_values, repeats);
}
