use std::fs::File;
use std::io::{BufRead, BufReader};
use std::path::Path;

pub fn read_lines<P>(filename: P) -> Vec<String>
where
    P: AsRef<Path>,
{
    let file = File::open(filename).unwrap();
    let lines = BufReader::new(file).lines();
    return lines.map(|line| line.unwrap()).collect();
}
