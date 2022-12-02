// https://adventofcode.com/2022/day/2
// Solved in Python then reimplemented in Dart to practise OOP

import 'dart:io';

enum Move {rock, paper, scissors}
enum Outcome {win, draw, lose}

class Round {
  late final Move _opponentMove, _playerMove;
  late final Outcome _outcome;
  late final int score;

  static const opponentMap = {
    'A': Move.rock,
    'B': Move.paper,
    'C': Move.scissors,
  };

  static const playerMap = {
    'X': Move.rock,
    'Y': Move.paper,
    'Z': Move.scissors,
  };

  static const outcomeMap = {
    'X': Outcome.lose,
    'Y': Outcome.draw,
    'Z': Outcome.win,
  };

  static const pairwise = {
    // key beats value
    Move.rock: Move.scissors,
    Move.paper: Move.rock,
    Move.scissors: Move.paper,
  };

  static const moveScore = {
    Move.rock: 1,
    Move.paper: 2,
    Move.scissors: 3,
  };

  static const outcomeScore = {
    Outcome.win: 6,
    Outcome.draw: 3,
    Outcome.lose: 0,
  };

  setOutcome() {
    if (_playerMove == _opponentMove) {
      _outcome = Outcome.draw;
    } else if (pairwise[_playerMove] == _opponentMove) {
      _outcome = Outcome.win;
    } else {
      _outcome = Outcome.lose;
    }
  }

  setPlayerMove() {
    if (_outcome == Outcome.lose) {
      _playerMove = pairwise[_opponentMove]!;
    } else if (_outcome == Outcome.draw) {
      _playerMove = _opponentMove;
    } else { // win
      _playerMove = pairwise.keys.firstWhere((elem) => pairwise[elem] == _opponentMove);
    }
  }

  Round(String opponentMove, {String? playerMove, String? outcome}) {
    _opponentMove = opponentMap[opponentMove]!;
    if (outcome == null) {
      _playerMove = playerMap[playerMove]!;
      setOutcome();
    }
    if (playerMove == null) {
      _outcome = outcomeMap[outcome]!;
      setPlayerMove();
    }
    score = moveScore[_playerMove]! + outcomeScore[_outcome]!;
  }
}

void main() {
  final List<String> input = File('./02data.txt').readAsLinesSync();

  // Part 1
  int score = 0;
  input.forEach((line) {
    Round round = Round(line[0], playerMove: line[2]);
    score += round.score;
  });
  print(score);

  // Part 2
  score = 0;
  input.forEach((line) {
    Round round = Round(line[0], outcome: line[2]);
    score += round.score;
  });
  print(score);
}
