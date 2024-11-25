use rand_mt::Mt64;
use rand::Rng;
use std::fs::File;
use std::io::{Write, BufWriter};

pub fn calucalte(n_values: Vec<usize>, repeats: usize)
{
    let mut bn_file = BufWriter::new(File::create("bn_results.txt").unwrap());
    let mut un_file = BufWriter::new(File::create("un_results.txt").unwrap());
    let mut cn_file = BufWriter::new(File::create("cn_results.txt").unwrap());
    let mut dn_file = BufWriter::new(File::create("dn_results.txt").unwrap());
    let mut difference_file = BufWriter::new(File::create("dn-cn_results.txt").unwrap());

    for &n in &n_values //iterujemy po wartosciach
    {
        let mut rng = Mt64::default();

        for _ in 0..repeats
        {
            let mut urns = vec![0; n];
            let mut empty_urns = n;
            let mut is_empty = 0;
            let mut is_more_than_one = 0;

            let mut bn = 0; //moment pierwszej kolizji
            let mut cn = 0; //liczba rzutow do zapelnienia kazdej urny
            let mut dn = 0; //liczba rzutow do zapelnienia kazdej urny przynajmniej 2 kulami
            let mut un = 0; //liczba pustych urn po wrzuceniu n kul

            for i in 1..
            {
                let urn = rng.gen_range(0..n);

                //jezeli urna byla pusta, zmiejszamy ilosc pustych urn
                if urns[urn] == 0
                {
                    empty_urns -= 1;
                }

                urns[urn] += 1;

                //liczenie b(n)
                if urns[urn] == 2 && bn == 0
                {
                    bn = i;
                }

                //liczenie c(n)
                if urns[urn] == 1
                {
                    is_empty += 1;

                    if is_empty == n && cn == 0
                    {
                        cn = i;
                    }
                }

                //liczenie d(n)
                if urns[urn] == 2
                {
                    is_more_than_one += 1;
                    if is_more_than_one == n && dn == 0
                    {
                        dn = i;
                        break;
                    }
                }

                if i == n
                {
                    un = empty_urns;
                }
            }

            //zapis wynikow do plikow
            writeln!(bn_file, "{} {}", n, bn).unwrap();
            writeln!(un_file, "{} {}", n, un).unwrap();
            writeln!(cn_file, "{} {}", n, cn).unwrap();
            writeln!(dn_file, "{} {}", n, dn).unwrap();
            writeln!(difference_file, "{} {}", n, dn - cn).unwrap();


        }
    }
}    

fn main()
{
    let n_values: Vec<usize> = (1000..=100000).step_by(1000).collect(); //zakres wartosci n
    let repeats = 50; //liczba powtorzen

    calucalte(n_values, repeats);
}