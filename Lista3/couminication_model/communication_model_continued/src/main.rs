use rand_mt::Mt64;
use rand::Rng;
use std::fs::File;
use std::io::{Write, BufWriter};

fn calculate(p: f64, n: i32, file: &mut BufWriter<File>) {
    let mut rng = Mt64::default();
    let mut stations = vec![0; n as usize];
    let mut arrived: i32 = 0;
    let mut repetitions: usize = 1;

    while arrived != n {
        for i in 0..n {
            let random_number = rng.gen_range(0.0..1.0);
            if stations[i as usize] == 0 && random_number < p {
                stations[i as usize] = repetitions;
                arrived += 1;
            }
        }
        repetitions += 1;
    }

    for k in 0..n {
        writeln!(file, "{}, {}", k, stations[k as usize]).unwrap();
    }    
}

fn main() {
    let mut file = BufWriter::new(File::create("results_p=0.5.txt").unwrap());
    let p: f64 = 0.5;
    let n: i32 = 100000;
    
    calculate(p, n, &mut file);
}