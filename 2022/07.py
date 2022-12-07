# https://adventofcode.com/2022/day/7

def insert(contents, subtree, subpath):
    if len(subpath) != 1:
        # Call this function recursively, each time passing:
        # - the contents to be placed at the path, when it's eventually reached
        # - a subtree that's one level further down the path
        # - a subpath truncated from the left
        insert(contents, subtree[pathindex(subtree, subpath[0])][1], subpath[1:])
    else:
        # Now at end of the path, add the contents to the relevant dir
        subtree[pathindex(subtree, subpath[0])][1].extend(contents)

def pathindex(subtree, subdir):
    for index, dir in enumerate(subtree):
        if dir[0] == subdir:
            return index

def traverse(contents):
    smalldirsum = 0
    dirsize = 0
    dirsizes = set()

    # Explore contents of this dir one by one, summing sizes of files and exploring subdirs
    for item in contents:
        if type(item[1]) is int: # file
            dirsize += item[1]
        else: # dir
            # Call this function recursively, passing each subdir's contents and obtaining:
            # - sum of sizes of all <=100000 dirs within it
            # - size of the subdir
            # - set of all dir sizes in the subtree
            (subtreesmalldirsum, subdirsize, subdirsizes) = traverse(item[1])
            smalldirsum += subtreesmalldirsum
            dirsize += subdirsize
            dirsizes.update(subdirsizes)

    # Now this dir has been traversed:
    # - add its size to the set of all dir sizes for part 2
    dirsizes.update({dirsize})
    # - if it's small enough, add its size to sum for part 1
    if dirsize <= 100000:
        smalldirsum += dirsize
    # Return the above and the size of this dir to be added to size of its parent
    return smalldirsum, dirsize, dirsizes


with open('./07data.txt') as datafile:
    input = [line.strip() for line in datafile.readlines()]

path = ['/']        # path to present working directory, as a stack
contents = []       # contents of present working directory
tree = [('/', [])]  # list of nested tuples containing the whole filesystem

# Parse the input and create the tree
for line in input:
    if line == '$ cd /' or line == '$ ls':
        continue
    elif line[0:4] == '$ cd':
        # Insert items accumulated from last dir listing
        insert(contents, tree, path)
        contents = []
        # Then change dir
        if line[5:] == '..':
            path.pop()
        else:
            path.append(line[5:])
    elif line[0:3] == 'dir':
        # Prepare tuple of form ('name', [])
        # [] will eventually hold the dir's contents
        contents.append((line[4:], []))
    else: # file
        # Prepare tuple of form ('name', size)
        file = line.split()
        contents.append((file[1], int(file[0])))
# Catch last dir listing in file
insert(contents, tree, path)

# Traverse the tree to obtain totals
(smalldirsum, rootsize, dirsizes) = traverse(tree)

# Part 1
print(smalldirsum)

# Part 2: Filter set of dir sizes to those big enough, then find smallest
print(sorted(list(filter(lambda x: x > rootsize - 40000000, dirsizes)))[0])