# OverTheWire Bandit Wargame Writeup

**Author:** ayanagi  
**Date:** February 2025  
**Platform:** OverTheWire - Bandit  
**Difficulty:** Beginner to Intermediate

## Level 0 → Level 1

### Objective
Establish initial SSH connection to the Bandit server and retrieve the first password.

### Solution

Connect to the server using the provided credentials:
- Username: `bandit0`
- Host: `bandit.labs.overthewire.org`
- Port: `2220`
- Password: `bandit0`

```bash
ssh bandit0@bandit.labs.overthewire.org -p 2220
```

Upon successful authentication, list the contents of the home directory:

```bash
bandit0@bandit:~$ ls
readme
```

Read the file to obtain the password for the next level:

```bash
bandit0@bandit:~$ cat readme
```

**Password:** `ZjLjTmM6FvvyRnrb2rfNWOZOTa6ip5If`

---

## Level 1 → Level 2

### Objective
Read a file with a hyphenated filename (`-`).

### Solution

In Unix systems, filenames starting with `-` are interpreted as command options by many utilities. To handle this, use a relative path prefix:

```bash
bandit1@bandit:~$ cat ./-
```

**Password:** `263JGJPfgU6LtdEvgfWU1XP5yac29mFx`

---

## Level 2 → Level 3

### Objective
Read a file with spaces in the filename.

### Solution

Filenames containing spaces require proper escaping. Either escape each space with a backslash or enclose the entire filename in quotes:

```bash
bandit2@bandit:~$ cat ./--spaces\ in\ this\ filename--
```

**Password:** `MNk8KNH3Usiio41PRUEoDFPqfxLPlSmx`

---

## Level 3 → Level 4

### Objective
Locate a hidden file within a subdirectory.

### Solution

Hidden files in Unix systems begin with a dot (`.`). Navigate to the `inhere` directory and list all files including hidden ones:

```bash
bandit3@bandit:~$ ls -la inhere/
bandit3@bandit:~$ cat ~/inhere/...Hiding-From-You
```

**Password:** `2WmrDFRmJIq3IPxneAaMGhap0pFhF3NJ`

---

## Level 4 → Level 5

### Objective
Identify the only human-readable file among multiple files.

### Solution

Use the `find` command combined with `file` to identify file types, then filter for ASCII text:

```bash
bandit4@bandit:~/inhere$ find . -type f -exec file {} \; | grep -i text
./-file07: ASCII text
```

Read the identified file:

```bash
bandit4@bandit:~/inhere$ cat ./-file07
```

**Password:** `4oQYVPkxZOOEOO5pTW81FB8j8lxXGUQw`

---

## Level 5 → Level 6

### Objective
Find a file based on specific size and permission constraints.

### Solution

Search for a file that is:
- Exactly 1033 bytes in size
- Not executable
- Owned by the appropriate user

```bash
bandit5@bandit:~/inhere$ find . -type f -size 1033c ! -executable
./maybehere07/.file2
```

Read the target file:

```bash
bandit5@bandit:~/inhere$ cat maybehere07/.file2
```

**Password:** `HWasnPhtq9AVKe0dmk45nxy20cvUa6EG`

---

## Level 6 → Level 7

### Objective
Locate a file system-wide based on ownership and size criteria.

### Solution

Search from the root directory for a file owned by `bandit7`, belonging to group `bandit6`, with size of 33 bytes:

```bash
bandit6@bandit:~$ find / -user bandit7 -group bandit6 -size 33c 2>/dev/null
/var/lib/dpkg/info/bandit7.password
```

Read the discovered file:

```bash
bandit6@bandit:~$ cat /var/lib/dpkg/info/bandit7.password
```

**Password:** `morbNTDkSW6jIlUc0ymOdMaLnOlFVAaj`

---

## Level 7 → Level 8

### Objective
Extract a password from a large text file using pattern matching.

### Solution

The file `data.txt` contains numerous entries. Use `grep` to search for the keyword "millionth":

```bash
bandit7@bandit:~$ grep "millionth" data.txt
millionth	dfwvzFQi4mU0wfNbFOe9RoWskMLg7eEc
```

**Password:** `dfwvzFQi4mU0wfNbFOe9RoWskMLg7eEc`

---

## Level 8 → Level 9

### Objective
Find the only line of text that appears exactly once in a file.

### Solution

Use `sort` and `uniq` to identify unique lines:

```bash
bandit8@bandit:~$ sort data.txt | uniq -u
```

**Password:** `4CKMh1JI91bUIZZPXDqGanal4xvAg0JM`

---

## Level 9 → Level 10

### Objective
Extract strings from binary data and identify the password pattern.

### Solution

Use `strings` to extract readable text from binary files, then filter for lines containing multiple equals signs:

```bash
bandit9@bandit:~$ strings data.txt | grep "^=.*"
```

**Password:** `FGUW5ilLVJrxX9kMYMmlN4MgbpfMiqey`

---

## Level 10 → Level 11

### Objective
Decode Base64 encoded data.

### Solution

The file contains Base64 encoded text. Decode using the `base64` utility:

```bash
bandit10@bandit:~$ cat data.txt | base64 -d
```

**Password:** `dtR173fZKb0RRsDFSGsg2RWnpNVj3qRr`

---

## Level 11 → Level 12

### Objective
Decode ROT13 encrypted text.

### Solution

The file contains text encrypted with ROT13 cipher (Caesar cipher with 13-position shift). Use `tr` to translate characters:

```bash
bandit11@bandit:~$ cat data.txt | tr 'A-Za-z' 'N-ZA-Mn-za-m'
```

**Password:** `7x16WNeHIi5YkIhWsfFIqoognUTyj9Q4`

---

## Level 12 → Level 13

### Objective
Decompress a file with multiple layers of compression.

### Solution

The file is a hexdump that requires conversion and multiple decompression steps:

1. Create a working directory and copy the file:
```bash
bandit12@bandit:~$ mktemp -d
/tmp/tmp.omc7PVzmGX
bandit12@bandit:~$ cd /tmp/tmp.omc7PVzmGX
bandit12@bandit:/tmp/tmp.omc7PVzmGX$ xxd -r ~/data.txt > data.bin
```

2. Iteratively decompress using `file` to identify compression types:
```bash
bandit12@bandit:/tmp/tmp.omc7PVzmGX$ file data.bin
# gzip -> gunzip
# bzip2 -> bunzip2
# tar -> tar -xf
# Repeat until ASCII text is obtained
```

**Password:** `FO5dwFsc0cbaIiH0h8J2eUks2vdTDwAn`

---

## Level 13 → Level 14

### Objective
Use SSH private key authentication to access the next level.

### Solution

A private SSH key is provided. Set appropriate permissions and connect:

```bash
# On local machine
chmod 600 sshkey.private
ssh -i sshkey.private bandit14@bandit.labs.overthewire.org -p 2220
```

Once connected, retrieve the password:

```bash
bandit14@bandit:~$ cat /etc/bandit_pass/bandit14
```

**Password:** `MU4VWeTyJk8ROof1qqmcBPaLh7lDCPvS`

---

## Level 14 → Level 15

### Objective
Submit the current password to a network service to receive the next password.

### Solution

Use `netcat` to send the password to localhost on port 30000:

```bash
bandit14@bandit:~$ echo "MU4VWeTyJk8ROof1qqmcBPaLh7lDCPvS" | nc localhost 30000
Correct!
8xCjnmgoKbGLhHFAZlGE5Tmu4M2tKJQo
```

**Password:** `8xCjnmgoKbGLhHFAZlGE5Tmu4M2tKJQo`

---

## Level 15 → Level 16

### Objective
Submit password to an SSL encrypted service.

### Solution

Use `openssl s_client` to establish an SSL connection and submit the password:

```bash
bandit15@bandit:~$ echo "8xCjnmgoKbGLhHFAZlGE5Tmu4M2tKJQo" | openssl s_client -connect localhost:30001 -quiet 2>/dev/null
```

**Password:** `kSkvUpMQ7lBYyCM4GBPvCvT1BfWRy0Dx`

---

## Level 16 → Level 17

### Objective
Identify SSL-enabled port and retrieve private key.

### Solution

1. Scan for open ports in the specified range:
```bash
bandit16@bandit:~$ nmap -p 31000-32000 localhost
```

2. Test SSL ports to find the correct one:
```bash
bandit16@bandit:~$ echo "kSkvUpMQ7lBYyCM4GBPvCvT1BfWRy0Dx" | openssl s_client -connect localhost:31790 -quiet 2>/dev/null
```

3. Save the provided RSA private key to a file and use it to SSH as bandit17.

---

## Level 17 → Level 18

### Objective
Compare two files to find the only differing line.

### Solution

Sort both files and use `diff` to identify differences:

```bash
bandit17@bandit:~$ sort passwords.new > /tmp/new.txt
bandit17@bandit:~$ sort passwords.old > /tmp/old.txt
bandit17@bandit:~$ diff /tmp/new.txt /tmp/old.txt
```

**Password:** `x2gLTTjFwMOhQ8oWNbMN362QKxfRqGlO`

---

## Level 18 → Level 19

### Objective
Bypass restricted shell access to read a file.

### Solution

The `.bashrc` is configured to immediately exit. Execute commands directly via SSH:

```bash
ssh bandit18@bandit.labs.overthewire.org -p 2220 "cat readme"
```

**Password:** `cGWpMaKXVwDUNgPAVJbWYuGHVn9zl3j8`

---

## Level 19 → Level 20

### Objective
Exploit SetUID binary to escalate privileges.

### Solution

The `bandit20-do` binary has SetUID permissions, allowing execution as `bandit20`:

```bash
bandit19@bandit:~$ ./bandit20-do cat /etc/bandit_pass/bandit20
```

**Password:** `0qXahG8ZjOVMN9Ghs7iOWsCfZyXOUbYO`

---

## Level 20 → Level 21

### Objective
Use a network service to validate a password and receive the next one.

### Solution

1. Terminal 1: Set up a listener to provide the current password:
```bash
bandit20@bandit:~$ echo "0qXahG8ZjOVMN9Ghs7iOWsCfZyXOUbYO" | nc -l -p 1234 &
```

2. Terminal 2: Connect using the `suconnect` binary:
```bash
bandit20@bandit:~$ ./suconnect 1234
```

**Password:** `EeoULMCra2q0dSkYj561DX7s1CpBuOBt`

---

## Level 21 → Level 22

### Objective
Analyze cron jobs to predict password file location.

### Solution

Inspect the cron job for bandit22:

```bash
bandit21@bandit:~$ cat /usr/bin/cronjob_bandit22.sh
#!/bin/bash
chmod 644 /tmp/t7O6lds9S0RqQh9aMcz6ShpAoZKF7fgv
cat /etc/bandit_pass/bandit22 > /tmp/t7O6lds9S0RqQh9aMcz6ShpAoZKF7fgv
```

Read the target file:

```bash
bandit21@bandit:~$ cat /tmp/t7O6lds9S0RqQh9aMcz6ShpAoZKF7fgv
```

**Password:** `tRae0UfB9v0UzbCdn9cY0gQnds9GF58Q`

---

## Level 22 → Level 23

### Objective
Understand and exploit a cron job that uses dynamic filename generation.

### Solution

Analyze the script to understand the filename generation logic:

```bash
bandit22@bandit:~$ cat /usr/bin/cronjob_bandit23.sh
#!/bin/bash
myname=$(whoami)
mytarget=$(echo I am user $myname | md5sum | cut -d ' ' -f 1)
cat /etc/bandit_pass/$myname > /tmp/$mytarget
```

Replicate the hash generation for `bandit23`:

```bash
bandit22@bandit:~$ echo I am user bandit23 | md5sum
8ca319486bfbbc3663ea0fbe81326349  -
```

Read the generated file:

```bash
bandit22@bandit:~$ cat /tmp/8ca319486bfbbc3663ea0fbe81326349
```

**Password:** `0Zf11ioIjMVN551jX3CmStKLYqjk54Ga`

---

## Key Concepts Summary

| Level | Technique |
|-------|-----------|
| 0-1 | SSH basics |
| 1-2 | Handling special filenames (`-`) |
| 2-3 | Escaping spaces in filenames |
| 3-4 | Hidden files (dotfiles) |
| 4-5 | File type identification |
| 5-6 | Advanced find with size/permission filters |
| 6-7 | System-wide file search with ownership filters |
| 7-8 | Pattern matching with grep |
| 8-9 | Sorting and uniqueness detection |
| 9-10 | String extraction from binary data |
| 10-11 | Base64 decoding |
| 11-12 | ROT13/Caesar cipher decoding |
| 12-13 | Multi-layer compression (gzip, bzip2, tar) |
| 13-14 | SSH key authentication |
| 14-15 | Network services with netcat |
| 15-16 | SSL/TLS connections with OpenSSL |
| 16-17 | Port scanning and SSL validation |
| 17-18 | File comparison with diff |
| 18-19 | Restricted shell bypass |
| 19-20 | SetUID privilege escalation |
| 20-21 | Network listener and service interaction |
| 21-22 | Cron job analysis |
| 22-23 | Hash-based filename prediction |

---

## Tools Used

- SSH client
- Standard Unix utilities: `ls`, `cat`, `find`, `grep`, `sort`, `uniq`, `diff`
- File utilities: `file`, `strings`, `xxd`
- Compression tools: `gzip`, `bzip2`, `tar`
- Encoding utilities: `base64`, `tr` (for ROT13)
- Network tools: `nc` (netcat), `nmap`, `openssl s_client`
- Cryptographic tools: `md5sum`

---

*Note: This writeup is for educational purposes only. Passwords and solutions are provided for learning and verification purposes in the context of the OverTheWire wargame platform.*
```

---

Writeup ini sudah diformat dengan:
- Struktur heading yang jelas dan konsisten
- Code blocks untuk semua command
- Tabel ringkasan di akhir
- Tidak ada emoji atau ikon yang tidak profesional
- Penjelasan teknis yang singkat dan to the point
- Format yang siap di-copy paste ke GitHub (Markdown)

