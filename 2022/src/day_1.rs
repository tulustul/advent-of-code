use std::cmp;

pub fn day_1() {
    part_1();
    part_2();
}

fn part_1() {
    let lines = crate::utils::read_lines("./input-1");

    let (mut max_calories, mut current_calories) = (0, 0);
    for line in lines {
        if line == "".to_string() {
            current_calories = 0;
            continue;
        }
        current_calories += line.parse::<i32>().unwrap();
        max_calories = cmp::max(max_calories, current_calories);
    }
    println!("{}", max_calories);
}

fn part_2() {
    let lines = crate::utils::read_lines("./input-1");

    let mut calories = Vec::<i32>::new();
    let mut current_calories = 0;

    for line in lines {
        if line == "".to_string() {
            calories.push(current_calories);
            current_calories = 0;
            continue;
        }
        current_calories += line.parse::<i32>().unwrap();
    }

    calories.sort();
    let best_3_total: i32 = calories.iter().rev().take(3).sum();

    println!("{}", best_3_total);
}
