use rand_mt::Mt64;
use rand::Rng;
use std::fs::File;
use std::io::{Write, BufWriter};

fn caulculate(n: i32, p: f64, file: &mut BufWriter<File>) {
    let mut rng = Mt64::new(rand::thread_rng().gen()); // Losowe ziarno w funkcji
    let mut knots = vec![0; n as usize];
    let mut arrived: i32 = 0;
    let mut repetitions = 0;
    let mut random_number: f64;

    while arrived != (n - 1) {
        for i in 1..n {
            random_number = rng.gen_range(0.0..1.0);
            if knots[i as usize] == 0 && random_number < p {
                knots[i as usize] = 1;
                arrived += 1;
            }
        }
        repetitions += 1;
    }
    writeln!(file, "{}, {}", n, repetitions).unwrap();
}

fn main() {
    let n_values: Vec<i32> = (10000..=1000000).step_by(10000).collect();
    let p = 0.5;
    let mut file = BufWriter::new(File::create("results.txt").unwrap());

    for &n in n_values.iter() {
        for _ in 0..50 {
            caulculate(n, p, &mut file);
        }
    }
}
