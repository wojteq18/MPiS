use rand_mt::Mt64;
use rand::Rng;
use std::fs::File;
use std::io::Write;
use std::f64::consts::PI;

fn main ()
{
    println!("Podaj ilość powtórzeń: ");
    let mut input = String::new();
    std::io::stdin().read_line(&mut input).expect("Błąd wczytywania danych");
    let repetitions = input.trim().parse::<i64>().expect("Błąd wczytywania danych");

    let mut file = File::create("integral_sin.txt").expect("Błąd tworzenia pliku");
    writeln!(file, "attempt, points, estimate").expect("Błąd zapisu do pliku");

    let mut rng = Mt64::default();

    for points in(50..=5000).step_by(50)
    {
        for i in 1..repetitions + 1
        {
            let mut points_inside = 0;
            for _ in 0..points
            {
                let x: f64 = rng.gen_range(0.0..=PI);
                let y: f64 = rng.gen_range(0.0..2.0); //sup zadanej funkcji na przedziale [0, PI] wynosi 1; 2 > 1
                if y <= x.sin()
                {
                    points_inside = points_inside + 1;
                }
            }
            let integral_sin = PI * 2.0 * points_inside as f64 / points as f64; //pole prostokata: PI * 2
            writeln!(file, "{}, {}, {}", i, points, integral_sin).expect("Błąd zapisu danych do pliku");
        }
    }
}