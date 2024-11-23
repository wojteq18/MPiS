use rand_mt::Mt64;
use rand::Rng;

pub fn calculate_dn(n: usize, repeats: usize, cn_results: &Vec<usize>) -> Vec<usize>
{
    let mut rng = Mt64::default();
    let mut results = Vec::new();

   for &c in cn_results.iter()
   {
        let mut urns = vec![1; n];
        let mut is_more_than_one: usize = 0;
        let mut additional_throwes: usize = 0;

        while is_more_than_one < n
        {
            let urn = rng.gen_range(0..n);
            urns[urn] = urns[urn] + 1;
            if urns[urn] == 2
            {
                is_more_than_one = is_more_than_one + 1;
            }
            additional_throwes = additional_throwes + 1;
        }
        results.push(c + additional_throwes);
   }
   return results;
}