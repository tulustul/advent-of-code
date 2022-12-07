pub fn day_2() {
    part_1();
    part_2();
}

fn part_1() {
    let lines = crate::utils::read_lines("./input-2").unwrap();

    let mut score = 0;
    for line in lines {
        let value = line.unwrap();
        let mut tokens = value.split(" ");
        let (a, b) = (tokens.next().unwrap(), tokens.next().unwrap());

        match (a, b) {
            ("A", "X") => score += 1 + 3,
            ("A", "Y") => score += 2 + 6,
            ("A", "Z") => score += 3 + 0,
            ("B", "X") => score += 1 + 0,
            ("B", "Y") => score += 2 + 3,
            ("B", "Z") => score += 3 + 6,
            ("C", "X") => score += 1 + 6,
            ("C", "Y") => score += 2 + 0,
            ("C", "Z") => score += 3 + 3,
            _ => (),
        }
    }

    println!("{}", score);
}

fn part_2() {
    let lines = crate::utils::read_lines("./input-2").unwrap();

    let mut score = 0;
    for line in lines {
        let value = line.unwrap();
        let mut tokens = value.split(" ");
        let (a, b) = (tokens.next().unwrap(), tokens.next().unwrap());

        match (a, b) {
            ("A", "X") => score += 3 + 0,
            ("A", "Y") => score += 1 + 3,
            ("A", "Z") => score += 2 + 6,
            ("B", "X") => score += 1 + 0,
            ("B", "Y") => score += 2 + 3,
            ("B", "Z") => score += 3 + 6,
            ("C", "X") => score += 2 + 0,
            ("C", "Y") => score += 3 + 3,
            ("C", "Z") => score += 1 + 6,
            _ => (),
        }
    }

    println!("{}", score);
}
