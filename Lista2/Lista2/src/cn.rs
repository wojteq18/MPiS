use rand_mt::Mt64;
use rand::Rng;

pub fn calculate_cn(n: usize, repeats: usize) -> Vec<usize>
{
    let mut rng = Mt64::default();
    let mut results = Vec::new();

    for _ in 0..repeats
    {
        let mut is_empty: usize = 0;
        let mut urns = vec![0; n];

        for i in 1..
        {
            let urn = rng.gen_range(0..n);
            urns[urn] = urns[urn] + 1;
            if urns[urn] == 1
            {
                is_empty = is_empty + 1;
            }
            if is_empty == n
            {
                results.push(i);
                break;
            }
        }
    }
    return results;
}