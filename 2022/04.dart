// https://adventofcode.com/2022/day/4
// Solved in Python then reimplemented in Dart

import 'dart:io';
import 'dart:math';

void main() {
  final List<String> input = File('./04data.txt').readAsLinesSync();
  int fullyContained = 0;
  int overlap = 0;

  input.forEach((line) {
    final List<int> bounds = line
        .trim()
        .split(RegExp(',|-'))
        .map((e) => int.parse(e))
        .toList();

    if ((bounds[0] >= bounds [2] && bounds[1] <= bounds[3]) ||
        (bounds[2] >= bounds [0] && bounds[3] <= bounds[1])) {
      fullyContained++;
    }
    if (max(bounds[0], bounds[2]) <= min(bounds[1], bounds[3])) {
      overlap++;
    }
  });

  print(fullyContained);
  print(overlap);
}
