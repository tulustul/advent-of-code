pub fn day_5() {
    part_1();
    part_2();
}

fn part_1() {
    let lines = crate::utils::read_lines("./input-5");

    let (mut stacks, operations) = split_to_stack_and_operations(lines);

    for oper in operations {
        move_crate_9000(&mut stacks, oper);
    }

    let top_of_stack = get_top_of_stacks(stacks);

    println!("{}", top_of_stack);
}

fn part_2() {
    let lines = crate::utils::read_lines("./input-5");

    let (mut stacks, operations) = split_to_stack_and_operations(lines);

    for oper in operations {
        move_crate_9001(&mut stacks, oper);
    }

    let top_of_stack = get_top_of_stacks(stacks);

    println!("{}", top_of_stack);
}

fn split_to_stack_and_operations(lines: Vec<String>) -> (Vec<Vec<char>>, Vec<String>) {
    for i in 0..lines.len() {
        if lines[i] == "" {
            return (parse_stacks(lines[..i].to_vec()), lines[i + 1..].to_vec());
        }
    }
    return (Vec::new(), Vec::new());
}

fn parse_stacks(lines: Vec<String>) -> Vec<Vec<char>> {
    let number_of_stacks = lines.last().unwrap().len() / 4;
    let mut stacks: Vec<Vec<char>> = Vec::new();

    for i in 0..=number_of_stacks {
        let mut stack = Vec::new();
        for line in lines.iter().rev().skip(1) {
            if let Some(value) = line.chars().nth(i * 4 + 1) {
                if value != ' ' {
                    stack.push(value);
                }
            }
        }
        stacks.push(stack);
    }

    return stacks;
}

fn move_crate_9000(stacks: &mut Vec<Vec<char>>, oper: String) {
    let tokens: Vec<&str> = oper.split(" ").collect();
    let quantity = tokens[1].parse::<usize>().unwrap();
    let from_stack = tokens[3].parse::<usize>().unwrap() - 1;
    let to_stack = tokens[5].parse::<usize>().unwrap() - 1;

    for _ in 0..quantity {
        let value = stacks[from_stack].pop();
        stacks[to_stack].push(value.unwrap())
    }
}

fn move_crate_9001(stacks: &mut Vec<Vec<char>>, oper: String) {
    let tokens: Vec<&str> = oper.split(" ").collect();
    let quantity = tokens[1].parse::<usize>().unwrap();
    let from_stack = tokens[3].parse::<usize>().unwrap() - 1;
    let to_stack = tokens[5].parse::<usize>().unwrap() - 1;

    let mut tmp: Vec<char> = Vec::new();
    for _ in 0..quantity {
        let value = stacks[from_stack].pop().unwrap();
        tmp.push(value);
    }
    tmp.reverse();
    stacks[to_stack].append(&mut tmp);
}

fn get_top_of_stacks(stacks: Vec<Vec<char>>) -> String {
    let top_of_stack: Vec<String> = stacks
        .iter()
        .map(|stack| stack.last().or(Some(&' ')).unwrap().to_string())
        .filter(|value| value != " ")
        .collect();
    return top_of_stack.join("");
}
