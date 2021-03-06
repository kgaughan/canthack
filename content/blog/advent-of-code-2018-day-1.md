Title: Advent of Code 2018, Day 1
Date: 2018-12-26 23:14
Category: Advent of Code
Status: published

## Part 1

Very simple. Just a matter of summing up the lines.

Given this is the first time I'm writing non-trivial Rust, I ran into a small issue. Initially, my main function used the default return type of `()`, so when I compiled my code, I got this:

```text
warning: unused import: `std::io`
 --> src/main.rs:1:5
  |
1 | use std::io;
  |     ^^^^^^^
  |
  = note: #[warn(unused_imports)] on by default

error[E0277]: the `?` operator can only be used in a function that returns `Result` or `Option` (or another type that implements `std::ops::Try`)
 --> src/main.rs:7:13
  |
7 |     let f = File::open("input.txt")?;
  |             ^^^^^^^^^^^^^^^^^^^^^^^^ cannot use the `?` operator in a function that returns `()`
  |
  = help: the trait `std::ops::Try` is not implemented for `()`
  = note: required by `std::ops::Try::from_error`

error[E0277]: the `?` operator can only be used in a function that returns `Result` or `Option` (or another type that implements `std::ops::Try`)
  --> src/main.rs:12:18
   |
12 |         total += line?.parse::<i32>().unwrap()
   |                  ^^^^^ cannot use the `?` operator in a function that returns `()`
   |
   = help: the trait `std::ops::Try` is not implemented for `()`
   = note: required by `std::ops::Try::from_error`

error: aborting due to 2 previous errors

For more information about this error, try `rustc --explain E0277`.
error: Could not compile `day01`.
```

This was fixed by changing the return type to be `io::Result<()>`. I can't say that using this particular type was 100% obvious, and had to read the docs to find out. That I attribute more to my lack of experience in the langauge than any issue with the error message or language.

## Part 2

For this one, we want to the first value that gets repeated. The easiest way is to use as [HashSet](https://doc.rust-lang.org/std/collections/struct.HashSet.html) to keep track of the frequencies we hit. We start with 0, so that ought to be in there at the beginning.

Straightforward enough on the face of it, but I misread the question and the implication that the collection would have to be read over multiple times, and attempted to find the duplicate frequency while finding the final frequency.

To fix that, I created a [Vec](https://doc.rust-lang.org/std/vec/struct.Vec.html), which I collected the values into, and then wrote a second loop that iterated over the collected values repeatedly to find the first repetition.

## Solutions

For the source code, see [here](https://github.com/kgaughan/adventofcode2018/tree/master/day01).
