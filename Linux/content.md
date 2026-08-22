File Systems
A file system is a method that is used by an operating system to store, retrieve, organize, and manage files and directories on mass storage devices. A file system maintains information, such as the date of creation and modification of individual files, their file size, file type, and permissions. It also provides a structured form for data storage. A file system by itself does not interpret the data contained in files because this task is handled by specific applications. File systems vary depending on several parameters, such as the purpose of the file systems, the information they store about individual files, the way they store data, and data security.


File System Labels
File system labels are assigned to file systems for easy identification. The labels may be up to 16 characters long and can be displayed or changed using the e2label command.

The syntax for setting file system labels is e2label /dev/{device name}{partition number} {label name}. They can also be set using the tune2fs -L {volume label} {device} command.


File System Types
Linux supports many common file system types. Some are described in the following table.

File System Type 

Description 

ext2 

This used to be the native Linux file system of some of the previous releases. It is still supported in the current releases of Linux.

ext3 

This is an improved version of ext2. In case of an abrupt system shutdown, ext3 is faster in recovering data and better ensures data integrity. You can easily upgrade your file system from ext2 to ext3. 

ext4 

The newest default file system for Linux distributions. It is backwards- compatible with the ext2 and ext3 file systems. Among ext4’s improvements over ext3 are journaling, support of volumes of up to one exbibyte (EiB), and files up to 16 TiB in size. Ext4 is the default filesystem for CentOS/RHEL 7 and Ubuntu installations. 

XFS 

This is a 64-bit, high-performance journaling file system that provides fast recovery and can handle large files efficiently. XFS is the default file system for CentOS/RHEL 7 installations. 

ReiserFS

This can handle small files efficiently. It handles files smaller than 1K and is faster than ext2 and ext3. If appropriately configured, it can store more data than ext2. 

vfat

This is a 32-bit file system and supports long file names. It is compatible with the FAT file system of Microsoft Windows XP and Microsoft Windows NT.

JFS

This is a 64-bit journaling file system that is fast and reliable. It is better equipped to handle power failures and system crashes. 

swap

This is not a true file system, but rather is a portion of the hard disk that is used in situations when Linux runs out of physical memory and needs more of it. Linux pushes some of the unused files from RAM to “swap” to free up memory. 

ISO 9660

This is a file system standard defined by the International Organization for Standardization (ISO), and is also called a CDFS (Compact Disc File System). Linux allows you to access DVDs and CDs that use this file system. 

btrfs (Better FS) 

This is a modern copy on write (CoW) file system for Linux aimed at implementing advanced features while also focusing on fault tolerance, repair, and easy administration. btrfs is licensed under the GPL. 


Access to Other File Systems
Linux allows you to access other file systems and mount them when required. However, you cannot install Linux on these file systems.

File System 

Description 

FAT 

The FAT (File Allocation Table) file system is compatible with different operating systems, including all versions of Windows, MS-DOS, and UNIX. It is primarily used for formatting floppy disks.

NTFS

NTFS (New Technology File System) is the recommended file system for Windows-based computers. NTFS provides many enhanced features over FAT or vfat, including file- and folder-level security, file encryption, disk compression, and scalability to very large drives and files. 


Partitions
A partition is a section of the hard disk that logically acts as a separate disk. Partitions enable you to convert a large hard disk to smaller manageable chunks, leading to better organization of information. A partition must be formatted and assigned a filesystem before data can be stored on it. Partitions are identified using a partition table, which is stored in the boot record. The partition table can contain entries for a maximum of four primary partitions. The size of each partition can vary but cannot exceed the total free space of the hard disk.


Hard Disk Size Specification
Before proceeding with the installation process, you need to plan the hard disk layout based on your requirements. Each partition has a recommended size specification. The following table lists the recommended size specification for partitions.

Partition 

Recommended Size 

/ 

Minimum 1 GB. 

/boot

100 MB. 

swap 

Double the RAM size. 

/var

Minimum 250 MB. If the possibility of the installation of many applications exists in the future, allocate the appropriate size. 

/home

Varies based on the number of users. 


Disk Partitioning
Most operating systems, including Linux, use disk partitions. Data of different types can be stored in separate locations on the hard disk. The partition size can be specified by a user. However, the filesystem size must be considered before specifying the partition size. Disk partitioning enables the user to separate system files from user accessible ones. Corrupted partitions do not affect the other partitions, and they can be recovered separately.

Partition Type 

Description 

Primary 

A disk partition that can contain one filesystem or logical drive and is sometimes referred to as volumes. A maximum of four primary partitions are allowed. The swap filesystem and the boot partition are normally created in a primary partition. 

Extended 

An extended partition can contain several filesystems, which are referred to as logical disks or logical drives. There can be only one extended partition, which can be further subdivided. This partition type does not contain any data and has a separate partition table. 

Logical 

A part of a physical disk drive that has been partitioned and allocated as an independent unit and functions as a separate drive. A logical partition is created within an extended partition. There is no restriction on the number of logical partitions, but it is advisable to limit it to 12 logical partitions per disk drive.


The fdisk Utility
fdisk is a menu-driven utility program that is used for creating, modifying, or deleting partitions on a disk drive. Using fdisk, a new partition table can be created, or existing entries in the partition table can be modified. The fdisk utility understands the DOS and Linux type partition tables. Depending on the partition table created, the DOS FDISK or the Linux fdisk program is invoked. The fdisk utility also allows you to specify the size of partitions.

The syntax of the fdisk utility is fdisk [options] {device name}.

The fdisk utility supports a number of command line options.

Option

Enables You To 

-b sector size 

Specify the number of disk sectors. 

-H heads 

Specify the number of disk heads. 

-S sectors 

Specify the number of sectors per track. 

-s partition 

Print the partition size in blocks. 

-v 

List the fdisk version. 

-l 

List partition tables for devices. 


fdisk Utility Options
The fdisk utility provides various options for partitioning disks according to the requirements of users. Some of the fdisk options are described in the following table.

Option

Enables You To 

n 

Create a new partition. The sub-options allow you specify the partition type and partition size. 

d 

Remove a partition. 

p 

List the existing partitions. 

w 

Write the changes to the disk and exit the utility. 

q 

Cancel the changes made and exit the utility.


The fstab File
The fstab file is a configuration file that stores information about storage devices and partitions and where and how the partitions should be mounted.

The fstab file is located in the /etc directory. It can be edited only by a root user. The fstab file consists of a number of lines—one for each filesystem. Each line in an fstab file has six fields that are separated by spaces.

Field 

Description 

Device or partition name 

Specifies the name of the device or filesystem that has to be mounted. 

Default mount point 

Indicates where the filesystem has to be mounted.

Filesystem type 

Specifies the type of filesystem used by the device or partition. 

Mount options 

Specifies a set of comma-separated options that will be activated when the filesystem is mounted. 

Dump options 

Indicates if the dump utility should back up the filesystem. Usually, zero is specified as the dump option to indicate that dump can ignore the filesystem. 

fsck options 

Specifies the order in which the fsck utility should check filesystems. 


The mkfs Command
The mkfs command is used to build a Linux filesystem on a device, which is usually a hard disk partition. 

The syntax of the mkfs command is mkfs [filesystem type] [options] {device}.

The following table lists some options of the mkfs command and their description.

Option

Allows You To 

-v 

Produce verbose output, where the output message will keep changing constantly as the program is processing. 

-V 

Produce verbose output, including all filesystem-specific commands that are executed. 

-t {fstype} 

Specify the type of filesystem to be built. 

fs-options 

Pass filesystem-specific options to the filesystem builder. 

-c 

Check the device for bad blocks before building the filesystem. 

-l {file name} 

Read the list of bad blocks from a specified file. 


Building New Linux Filesystems Using the mkfs Commands
The mkfs commands are used to build a new Linux filesystem. The different mkfs commands are given in the following table.

If You Need To Build 

Use This mkfs Command 

An ext2 filesystem 

mkfs.ext2 /dev/hdaPartition number 

An ext3 filesystem 

mkfs.ext3 /dev/hdaPartition number 

An ext4 filesystem 

mkfs.ext4 /dev/hdaPartition number 

An XFS filesystem 

mkfs.xfs /dev/hdaPartition number 

A reiserfs filesystem 

mkfs.reiserfs /dev/hdaPartition number

A btrfs filesystem 

mkfs.btrfs /dev/hdaPartition number 

A vfat filesystem 

mkfs.vfat /dev/hdaPartition number 

A JFS filesystem 

mkfs.jfs /dev/hdaPartition number 


The mke2fs Command
The mke2fs utility is used to create ext2, ext3, and ext4 filesystems, and it has various options. This command is a more specific version of the mkfs command described previously that may be used to create ext2, ext3, and ext4 filesystems only. 

The syntax of the mke2fs utility is mke2fs[options] {device}.

Some of the options for mke2fs are listed in the following table.

Option

Enables You To 

-t {filesystem type} 

Specify the filesystem type to create (i.e., ext2, ext3, ext4, etc.). 

-b {block size} 

Specify the size of the block in bytes.

-c 

Check the device for errors in the blocks, before creating the filesystem. 

-f 

Specify the fragment size in bytes. 

-j 

Create a journaled ext3 filesystem. 

-M 

Set the directory that was last accessed for the filesystem to be mounted. 

-V 

Print the version number of the mke2fs utility. 

Note: The command mke2fs -t ext4 /dev/sdaPartition number will allow you to build an ext4 filesystem. 

WARNING: Running this command will format your disk, deleting all contents!

