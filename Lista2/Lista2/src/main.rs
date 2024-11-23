use std::fs::File;
use std::io::{Write, BufWriter};

mod bn;
mod cn;

fn main() 
{
    let n_values: Vec<usize> = {1000..=100000}.step_by(1000).collect();
    let repeats = 50;

    //otwierany pliki tekstowe
    let mut bn_file = BufWriter::new(File::create("bn_results.txt").unwrap());
    let mut cn_file = BufWriter::new(File::create("cn_results.txt").unwrap());

    for &n in &n_values
    {
        //zapisywanie wyników do plików
        let bn_results = bn::calculate_bn(n, repeats);
        let cn_results = cn::calculate_cn(n, repeats);

        //zapis do odpowiednich plików
        for result in bn_results
        {
            writeln!(bn_file, "{} {}", n, result).unwrap();
        }

        for result in cn_results
        {
            writeln!(cn_file, "{} {}", n, result).unwrap();
        }
    }
}
