# Used help from Github user willsmith28

import functools
import operator
from collections.abc import Iterator
from typing import TextIO

class File:
    def __init__(self, name: str, size: int) -> None:
        self.name = name
        self.size = size


class Directory:
    def __init__(self, name) -> None:
        self.name = name
        self.files: dict[str, File] = {}
        self.directories: dict[str, Directory] = {}

    @functools.cached_property
    def size(self) -> int:
        file_sizes = sum(file.size for file in self.files.values())
        return file_sizes + sum(
            directory.size for directory in self.directories.values()
        )


class FileSystem:
    def __init__(self) -> None:
        self.root = Directory("")

    def add(self, path: str, item: File):
        root, *path = path.split("/")
        assert root == ""
        current = self.root
        for name in path:
            if name == "":
                continue
            elif name in current.directories:
                current = current.directories[name]
            else:
                current.directories[name] = Directory(name)
                current = current.directories[name]

        current.files[item.name] = item

    def iter_directories(self, current: Directory | None = None) -> Iterator[Directory]:
        if current is None:
            current = self.root

        yield current

        for sub_dir in current.directories.values():
            yield from self.iter_directories(sub_dir)

def build_file_system(command_logs: TextIO):
    fs = FileSystem()
    it = iter(command_logs)
    command = next(it).strip()
    assert command == "$ cd /"
    current_dir: list[str] = []
    try:
        while True:
            command = next(it).strip()
            if command.startswith("$ cd "):
                # changing dirs
                dest_dir = command.split()[-1]
                if dest_dir == "..":
                    current_dir.pop()
                else:
                    current_dir.append(dest_dir)
            elif command == "$ ls":
                # consume results
                current_dir_str = f"/{'/'.join(current_dir)}"
                while not (log := next(it).strip()).startswith("$"):
                    if log.startswith("dir"):
                        continue
                    else:
                        size, file_name = log.split()
                        fs.add(current_dir_str, File(file_name, int(size)))

                if log.startswith("$ cd "):
                    # changing dirs
                    dest_dir = log.split()[-1]
                    if dest_dir == "..":
                        current_dir.pop()
                    else:
                        current_dir.append(dest_dir)
    except StopIteration:
        return fs



def part_one():
    with open("input.txt", "r") as f:
        fs = build_file_system(f)

    return sum(dir.size for dir in fs.iter_directories() if dir.size <= 100000)

def part_two():
    with open("input.txt", "r") as f:
        fs = build_file_system(f)

    total_space = 70000000
    target_unused_space = 30000000
    directories = sorted(fs.iter_directories(), key=operator.attrgetter("size"))
    root = directories[-1]
    current_unused_space = total_space - root.size
    for dir in directories:
        if current_unused_space + dir.size >= target_unused_space:
            return dir.size

print(part_one())
print(part_two())