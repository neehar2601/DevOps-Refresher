# Linux Learning Notes: Commands, Navigation, Permissions, and Ownership

This document summarizes the Linux concepts covered so far in a beginner-friendly format for GitHub reference.

## Core commands

- `pwd` prints the current working directory path.[cite:23][cite:24]
- `ls` lists files and directories in the current location.[cite:23][cite:25]
- `whoami` prints the current username.[cite:21][cite:24]
- `uname -a` shows system and kernel information, not a list of users.[cite:18]

## Navigation basics

- `cd` changes the current directory.[cite:26][cite:32]
- `cd ..` moves to the parent directory.[cite:26][cite:27]
- `cd /` moves to the root directory.[cite:27][cite:35]
- Running `cd` by itself usually takes the user to the home directory.[cite:26][cite:34]

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

- `ls` shows visible files and directories.[cite:23][cite:25]
- `ls -a` also shows hidden files.[cite:35]
- `ls -l` shows detailed information such as permissions, owner, group, size, and modification time.[cite:36][cite:44]
- `ls -la` combines detailed view with hidden files.[cite:35][cite:44]

A typical `ls -l` output includes:

- Permission string
- Link count
- Owner
- Group
- File size
- Timestamp
- File name[cite:42][cite:43]

## Permission basics

Linux permissions are expressed with `r`, `w`, and `x`, and they apply separately to the owner, group, and others.[cite:52][cite:58]

- `r` = read.[cite:53][cite:55]
- `w` = write.[cite:53][cite:55]
- `x` = execute.[cite:53][cite:55]

A permission string like `-rwxr-xr--` can be read as:

- `-` = regular file.[cite:57][cite:62]
- `rwx` = owner can read, write, and execute.[cite:57][cite:62]
- `r-x` = group can read and execute.[cite:57][cite:62]
- `r--` = others can only read.[cite:57][cite:62]

### Common examples

| Symbolic | Numeric | Meaning |
|---------|---------|---------|
| `-rw-r--r--` | `644` | Owner can read/write; group and others can read only.[cite:75][cite:52] |
| `-rwxr-x---` | `750` | Owner has full access; group can read/execute; others have no access.[cite:89][cite:90] |
| `-rwx------` | `700` | Only the owner has full access.[cite:96][cite:100] |

## Numeric permissions

Numeric permissions are based on these values:[cite:48][cite:98]

- Read = 4
- Write = 2
- Execute = 1

Examples:[cite:48][cite:90]

- `7` = 4 + 2 + 1 = `rwx`
- `5` = 4 + 1 = `r-x`
- `4` = `r--`
- `0` = `---`

So `750` means:[cite:89][cite:92]

- Owner = `7` = `rwx`
- Group = `5` = `r-x`
- Others = `0` = `---`

## chmod

The `chmod` command changes file or directory permissions.[cite:46][cite:49]

Examples:[cite:46][cite:54]

```bash
chmod 700 deploy.sh
chmod 750 deploy.sh
chmod 644 notes.txt
```

Typical use cases:

- `700` for a private script that only the owner should edit and run.[cite:96][cite:100]
- `750` when the owner needs full control, the group needs read/execute, and others should have no access.[cite:92][cite:94]
- `644` for normal files that the owner edits while others can read.[cite:75][cite:95]

## Ownership and groups

Every file has both an owner user and an owner group.[cite:58][cite:134]

In `ls -l` output, the columns after the link count typically show:

- Owner
- Group[cite:134][cite:131]

If a file shows this:

```text
-rw-rw-r-- 1 root mygroup 0 Jul 29 23:40 test.sh
```

then:

- `root` is the file owner.[cite:124][cite:126]
- `mygroup` is the owning group.[cite:123][cite:134]
- Owner permissions are `rw-`.[cite:134][cite:52]
- Group permissions are `rw-`.[cite:134][cite:52]
- Others have `r--`.[cite:134][cite:52]

## chown and chgrp

- `chown user file` changes the owner of a file.[cite:124][cite:125]
- `chown user:group file` changes both owner and group.[cite:106][cite:116]
- `chgrp group file` changes only the group.[cite:106][cite:108]

Examples:[cite:106][cite:108]

```bash
sudo chown root demo.txt
sudo chown root:developers demo.txt
sudo chgrp developers demo.txt
```

Usually, changing ownership to another user requires elevated privileges such as `sudo`.[cite:126][cite:129]

## Practical interpretation

When a user creates a file, the owner is usually that user, and the group is often the user's primary group, which may have the same name as the username.[cite:123][cite:128]

After running:

```bash
sudo chown root demo.txt
```

the owner changes to `root`, while the group usually remains unchanged unless it is explicitly modified.[cite:124][cite:130]

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

A practical Linux roadmap typically progresses from basic commands to permissions, users, package management, processes, networking, scripting, storage, security, and automation.[cite:2][cite:9][cite:12]
