use rand_mt::Mt64; // Import generatora Mersenne Twister
use rand::Rng;     // Import traitu Rng, by korzystać z losowych liczb
use std::fs::File;
use std::io::Write;

fn main()
{
    println!("Podaj liczbę powtórzeń: ");
    let mut input = String::new();
    std::io::stdin().read_line(&mut input).expect("Błąd wczytywania danych");
    let repetitions = input.trim().parse::<i64>().expect("Błąd wczytywania danych");

    let mut file = File::create("pi_aprox.txt").expect("Błąd tworzenia pliku");
    writeln!(file, "attempt, points, estimate").expect("Błąd zapisu do pliku");

    let mut rng = Mt64::default(); //inicjalizacja generatora Mt raz na początku

    for points in(50..=5000).step_by(50)
    {
        for i in 0..repetitions
        {
            let mut points_inside_circle = 0;
            for _ in 0..points
            {
                let x = rng.gen_range(-1.0..=1.0);
                let y = rng.gen_range(-1.0..=1.0);

                if x*x + y*y <= 1.0
                {
                    points_inside_circle = points_inside_circle + 1;
                }
            }
            let mut pi_aprox = 4.0 * points_inside_circle as f64 / points as f64;
            writeln!(file, "{}, {}, {}", i, points, pi_aprox).expect("Błąd zapisu do pliku");
        }
    }
}


