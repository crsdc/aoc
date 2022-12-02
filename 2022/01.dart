// https://adventofcode.com/2022/day/1
// Solved in Python then reimplemented in Dart

import 'dart:io';
import 'dart:math';

void main() {
  final List<String> input = File('01data.txt').readAsLinesSync();

  List<int> elves = [];
  int elfIndex = 0;

  input.forEach((line) {
    if (line.isEmpty) {
      elfIndex++;
    } else {
      if (elves.length == elfIndex) {
        elves.add(int.parse(line));
      } else {
        elves[elfIndex] += int.parse(line);
      }
    }
  });

  // Part 1
  print(elves.reduce(max));

  // Part 2
  elves.sort();
  print(
    elves.reversed.take(3).reduce(
      (total, next) => total + next
    )
  );
}
