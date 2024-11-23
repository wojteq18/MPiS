use crate::cn;
use crate::dn;

pub fn calculate_difference(cn_results: &Vec<usize>, dn_results: &Vec<usize>) -> Vec<usize>
{
    cn_results.iter().zip(dn_results.iter()).map(|(&cn, &dn)| dn - cn).collect()
}