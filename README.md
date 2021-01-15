# email-validator-cschallenge

Email validation program set as a challenge for my GCSE Computer Science course

This was written in Python for the sake of simplicity, although I could have probably made the code a lot prettier in a language like Java or Javascript.

I only gave myself 45 minutes to write this, most of which was spent debugging a bug in my RegEx, which turned out to be a missing `+` before the end of string key. 🙄
If I had have given myself longer to work on this I probably could have made it more efficient, which is why I put it on Github.

#### TODO:
On the off-chance that I do come back to this project, I will likely want to work on the following:
- [ ] Package as a usable Unix command
- [ ] Write an install script
- [ ] Options to output data to JSON (or other mediums)

## Prerequisites
* Python >=3.6

## How it works
The program essentially compares a string of an email address to a Regular Expression, or in the case of verbose mode (default) a series of Regular Expressions. This allows quick and efficient validation of email address strings without having to have half a million if statements and for loop iterations.

For the reading of lists, the script opens a text file using Python's built-in `open(file, [...])` command, where the data was then read and split into an array of strings by `\n`. These are then stripped of whitespace and filtered for empty strings, before being put through a `for x in y` loop, which runs the function to validate email addresses for each entry in the list.

## How to use
To use the program, you must first have Python 3.6 (or higher) installed.

### Download
To download via git, run from your terminal:
```bash
git clone https://github.com/OliverCordingl1/email-validator-cschallenge emailvalidator; cd emailvalidator
```

### Usage
To use, ensure that you are in the same directory as the program, and run:
```bash
python main.py --help
```

From there, you should be able to see all possible commands that can be used.

### Compatability
I use a Unix-based machine, so I am unable to test for Windows. In theory, it *should* work, however as the command interface is completely different to that of a Unix system like macOS or Linux, I do not know the correct syntax to use in CMD or Powershell