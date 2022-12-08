use std::collections::{HashMap, HashSet};

pub fn day_3() {
    part_1();
    part_2();
}

fn part_1() {
    let lines = crate::utils::read_lines("./input-3");
    let mut sum = 0;
    for line in lines {
        let middle = line.len() / 2;
        let first_half = &line[..middle];
        let second_half = &line[middle..];
        for c in second_half.chars() {
            if first_half.contains(c) {
                sum += get_priority(c);
                break;
            }
        }
    }
    println!("{}", sum);
}

fn part_2() {
    let lines = crate::utils::read_lines("./input-3");
    let mut sum = 0;
    for i in (0..lines.len()).step_by(3) {
        let first = line_to_set(&lines[i]);
        let second = line_to_set(&lines[i + 1]);
        let third = line_to_set(&lines[i + 2]);

        let first_two: Vec<&char> = first.intersection(&second).collect();
        // WTF?
        let mut x: HashSet<char> = HashSet::new();
        for c in first_two {
            x.insert(*c);
        }

        let intersection = x.intersection(&third);
        sum += intersection
            .map(|c| get_priority(*c))
            .reduce(|acc, val| acc + val)
            .unwrap();
    }
    println!("{}", sum);
}

fn get_priority(c: char) -> i32 {
    let offset = if c.is_uppercase() { 64 - 26 } else { 96 };
    let value = c as i32 - offset;
    return value;
}

fn line_to_set(line: &String) -> HashSet<char> {
    let mut set = HashSet::new();
    for c in line.chars() {
        set.insert(c);
    }
    return set;
}
