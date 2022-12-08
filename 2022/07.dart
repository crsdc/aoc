// https://adventofcode.com/2022/day/7
// Solved in Python with recursive functions and nested lists
// Reimplemented in Dart with classes

import 'dart:io' as io;

class File {
  String name;
  String path;
  int? size;

  File({required this.name, required this.path, int? this.size});

  String toString() {
    return '$name, $path, $size';
  }
}

class Folder extends File {
  late List children;

  Folder({required name, required path}) : super(name: name, path: path);
}



void main() {
  final List<String> input = io.File('./testdata.txt').readAsLinesSync();

  List filesystem = [];
  String path = '';

  input.forEach((line) {
    if (line == '\$ ls') {
      return;
    } else if (line.substring(0, 7) == '\$ cd ..') {
      path // lose the last string up to slash
    } else if (line.substring(0, 4) == '\$ cd') {
      path += line.substring(5);
    } else if (line.substring(0, 3) == 'dir') {
      filesystem.add(Folder(name: line.substring(4), path: path));
    } else {
      List file = line.split(' ');
      filesystem.add(File(name: file[1], path: path, size: int.parse(file[0])));
    }
  });

  filesystem.forEach((file) {
    print(file.toString());
  });

}
