use std::fs::File;
use std::io::{Write, BufWriter};

mod bn;
mod cn;
mod un;
mod dn;
mod difference;

fn main() 
{
    let n_values: Vec<usize> = {1000..=100000}.step_by(1000).collect();
    let repeats = 50;

    //otwierany pliki tekstowe
    let mut bn_file = BufWriter::new(File::create("bn_results.txt").unwrap());
    let mut un_file = BufWriter::new(File::create("un_results.txt").unwrap()); 
    let mut cn_file = BufWriter::new(File::create("cn_results.txt").unwrap());
    let mut dn_file = BufWriter::new(File::create("dn_results.txt").unwrap());
    let mut difference_file = BufWriter::new(File::create("dn-cn.txt").unwrap());

    for &n in &n_values
    {
        //zapisywanie wyników do plików
        let bn_results = bn::calculate_bn(n, repeats);
        let un_results = un::calculate_un(n, repeats);
        let cn_results = cn::calculate_cn(n, repeats);
        let dn_results = dn::calculate_dn(n, repeats, &cn_results);
        let difference_results = difference::calculate_difference(&cn_results, &dn_results);

        //zapis do odpowiednich plików
        for result in bn_results
        {
            writeln!(bn_file, "{} {}", n, result).unwrap();
        }

        for result in cn_results
        {
            writeln!(cn_file, "{} {}", n, result).unwrap();
        }

        for result in un_results
        {
            writeln!(un_file, "{} {}", n, result).unwrap();
        }

        for result in dn_results
        {
            writeln!(dn_file, "{} {}", n, result).unwrap();
        }

        for result in difference_results
        {
            writeln!(difference_file, "{} {}", n, result).unwrap();
        }

    }
}
