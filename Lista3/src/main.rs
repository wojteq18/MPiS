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
            let mut max_balls_an = 0;
            let mut max_balls_bn = 0;
            //let mut an = 0;

            for i in 1..n {
                //obliczmy an - maxymalna ilosc kul w urnie
                let urn = rng.gen_range(0..n);
                urns[urn] += 1;
                if urns[urn] > max_balls_an {
                    max_balls_an = urns[urn];
                }

                //obliczmy bn - odejmujemy kule dodana, losujemy nastepna urne i wybieramy do ktorej z tych dwoch ma trafic kula
                urns[urn] -= 1;
                
                let mut urn2;
                loop {
                    urn2 = rng.gen_range(0..n);
                    if urn != urn2 {
                        break; // nie chcemy wylosowac urny, ktora juz wylosowalismy
                    }
                }

                if urns[urn2] > urns[urn] {
                    urns[urn2] += 1;
                } else {
                    urns[urn] += 1;
                }
                if max_balls_bn < urns[urn] {
                    max_balls_bn = urns[urn];
                }
                else if max_balls_bn < urns[urn2] {
                    max_balls_bn = urns[urn2];
                }
            }
            writeln!(an_file, "{} {}", n, max_balls_an).unwrap();
            writeln!(bn_file, "{} {}", n, max_balls_bn).unwrap();
        }
    }
}

fn main() {
    let n_values: Vec<usize> = (1000..=100000).step_by(1000).collect(); //zakres wartosci n
    let repeats = 5; //ilosc powtorzen dla kazdej wartosci n

    calculate(n_values, repeats);
}