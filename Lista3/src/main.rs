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
            let mut urns = vec![0; n];
            let mut urns_bn = vec![0; n];
            let mut max_balls_an = 0;
            let mut max_balls_bn = 0;

            for _ in 1..n {
                // Obliczamy an - maksymalna liczba kul w urnie
                let urn = rng.gen_range(0..n);
                urns[urn] += 1;
                if urns[urn] > max_balls_an {
                    max_balls_an = urns[urn];
                }

                //obliczamy bn
                let mut urn1 = rng.gen_range(0..n);
                let mut urn2;
                loop {
                    urn2 = rng.gen_range(0..n);
                    if urn1 != urn2 {
                        break; // Nie chcemy wylosować urny, którą już wylosowaliśmy
                    }
                }

                if urns_bn[urn2] < urns_bn[urn1] {
                    urns_bn[urn2] += 1;
                } else {
                    urns_bn[urn1] += 1;
                }

                if urns_bn[urn1] > urns_bn[urn2] {
                    if urns_bn[urn1] > max_balls_bn {
                        max_balls_bn = urns_bn[urn1];
                    }
                } else if urns_bn[urn2] > max_balls_bn {
                    max_balls_bn = urns_bn[urn2];
                }
            }

            writeln!(an_file, "{} {}", n, max_balls_an).unwrap();
            writeln!(bn_file, "{} {}", n, max_balls_bn).unwrap();
        }
    }
}

fn main() {
    let n_values: Vec<usize> = (10000..=1000000).step_by(10000).collect(); // Zakres wartości n
    let repeats = 50; // Ilość powtórzeń dla każdej wartości n

    calculate(n_values, repeats);
}