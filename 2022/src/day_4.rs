pub fn day_4() {
    part_1();
    part_2();
}

fn part_1() {
    let lines = crate::utils::read_lines("./input-4");
    let mut count = 0;
    for line in lines {
        let mut tokens = line.split(",");
        let range_a = parse_range(tokens.next().unwrap());
        let range_b = parse_range(tokens.next().unwrap());

        if (range_a.0 >= range_b.0 && range_a.1 <= range_b.1)
            || (range_b.0 >= range_a.0 && range_b.1 <= range_a.1)
        {
            count += 1;
        }
    }
    println!("{}", count);
}

fn part_2() {
    let lines = crate::utils::read_lines("./input-4");
    let mut count = 0;
    for line in lines {
        let mut tokens = line.split(",");
        let range_a = parse_range(tokens.next().unwrap());
        let range_b = parse_range(tokens.next().unwrap());

        if range_a.0 <= range_b.1 && range_a.1 >= range_b.0 {
            count += 1;
        }
    }
    println!("{}", count);
}

fn parse_range(range_s: &str) -> (i32, i32) {
    let mut tokens = range_s.split("-");
    return (
        tokens.next().unwrap().parse::<i32>().unwrap(),
        tokens.next().unwrap().parse::<i32>().unwrap(),
    );
}
