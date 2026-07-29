# Linux Learning Notes: Commands, Navigation, Permissions, and Ownership

This document summarizes the Linux concepts covered so far in a beginner-friendly format for GitHub reference.

## Core commands

- `pwd` prints the current working directory path.
- `ls` lists files and directories in the current location.
- `whoami` prints the current username.
- `uname -a` shows system and kernel information, not a list of users.

## Navigation basics

- `cd` changes the current directory.
- `cd ..` moves to the parent directory.
- `cd /` moves to the root directory.
- Running `cd` by itself usually takes the user to the home directory.

### Example

If the current path is `/var/lib`, then:

```bash
cd ..
```

moves to:

```bash
/var
```

## Listing files in detail

- `ls` shows visible files and directories.
- `ls -a` also shows hidden files.
- `ls -l` shows detailed information such as permissions, owner, group, size, and modification time.
- `ls -la` combines detailed view with hidden files.

A typical `ls -l` output includes:

- Permission string
- Link count
- Owner
- Group
- File size
- Timestamp
- File name

## Permission basics

Linux permissions are expressed with `r`, `w`, and `x`, and they apply separately to the owner, group, and others.

- `r` = read.
- `w` = write.
- `x` = execute.

A permission string like `-rwxr-xr--` can be read as:

- `-` = regular file.
- `rwx` = owner can read, write, and execute.
- `r-x` = group can read and execute.
- `r--` = others can only read.

### Common examples

| Symbolic | Numeric | Meaning |
|---------|---------|---------|
| `-rw-r--r--` | `644` | Owner can read/write; group and others can read only. |
| `-rwxr-x---` | `750` | Owner has full access; group can read/execute; others have no access. |
| `-rwx------` | `700` | Only the owner has full access. |

## Numeric permissions

Numeric permissions are based on these values:

- Read = 4
- Write = 2
- Execute = 1

Examples:

- `7` = 4 + 2 + 1 = `rwx`
- `5` = 4 + 1 = `r-x`
- `4` = `r--`
- `0` = `---`

So `750` means:

- Owner = `7` = `rwx`
- Group = `5` = `r-x`
- Others = `0` = `---`

## chmod

The `chmod` command changes file or directory permissions.

Examples:

```bash
chmod 700 deploy.sh
chmod 750 deploy.sh
chmod 644 notes.txt
```

Typical use cases:

- `700` for a private script that only the owner should edit and run.
- `750` when the owner needs full control, the group needs read/execute, and others should have no access.
- `644` for normal files that the owner edits while others can read.

## Ownership and groups

Every file has both an owner user and an owner group.

In `ls -l` output, the columns after the link count typically show:

- Owner
- Group

If a file shows this:

```text
-rw-rw-r-- 1 root mygroup 0 Jul 29 23:40 test.sh
```

then:

- `root` is the file owner.
- `mygroup` is the owning group.
- Owner permissions are `rw-`.
- Group permissions are `rw-`.
- Others have `r--`.

## chown and chgrp

- `chown user file` changes the owner of a file.
- `chown user:group file` changes both owner and group.
- `chgrp group file` changes only the group.

Examples:

```bash
sudo chown root demo.txt
sudo chown root:developers demo.txt
sudo chgrp developers demo.txt
```

Usually, changing ownership to another user requires elevated privileges such as `sudo`.

## Practical interpretation

When a user creates a file, the owner is usually that user, and the group is often the user's primary group, which may have the same name as the username.

After running:

```bash
sudo chown root demo.txt
```

the owner changes to `root`, while the group usually remains unchanged unless it is explicitly modified.

## Useful commands to practice next

```bash
pwd
ls
ls -a
ls -l
ls -la
whoami
uname -a
id
groups
chmod 700 file.sh
chmod 750 file.sh
chmod 644 notes.txt
chown root file.sh
chgrp developers file.sh
```

## Suggested learning path

A practical Linux roadmap typically progresses from basic commands to permissions, users, package management, processes, networking, scripting, storage, security, and automation.
