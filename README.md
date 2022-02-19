# **fileNamer build_0.0.2**

https://github.com/ljcbc/fileNamer

## DESCRIPTION:

a simple python script that generates a filename in **YYYY-MM-DD-XXBPM-KEYWORD** format that is sent to your clipboard.

![](https://media.giphy.com/media/k5TVqhx76GhfTifBjL/giphy.gif)

## REQUIREMENTS:

PYTHON3\
https://www.python.org/downloads/


PYPERCLIP
```
pip install pyperclip
```

PIP (to install modules)
```
curl https://bootstrap.pypa.io/get-pip.py | python3
```


## INSTALLATION:

1 - Make sure you have REQUIREMENTS installed.

2 - Place fileNamer folder in a directory that is out of the way + that will not be changed in the future.

3 - Edit the contents of the 'filenamer.command' file such that the file path points to the 'fileNamer.py' file in this folder.

4 - Test to see if the 'filenames.command' script runs (double click on it).

[!] if the file does not execute, enter the following command in Terminal"
```shell 
sudo chmod 775 {filenamer.command filepath}
```

[!] if the file runs but fileNamer does not run, make sure that you did step 3.

5 - Open Automator App, file >> new >> quick action >> add 'Run AppleScript'.

6 - Delete the apple script contents ( from 'on run'.. to 'end run'. Replace them with:

```AppleScript
on run {input, parameters}
	
	tell application "Terminal"
		activate
		do script "/Users/choi/Desktop/Projects/Other/CS/VSCode_Projects/fileNamer/filenamer.command;exit"
	end tell
	return input
end run
```

7 - Replace the existing filepath in the AppleScript with your own filepath to the 'filenamer.command'. Make sure not to remove the ';exit'.

8 - Save quick action.

9 - System Preferences >> Keyboard >> Shortcuts >> Services >> General >> add fileNamer keyboard shortcut. I use *CTRL + CMD + Z*.


## NOTES:

You may need to grant the application permission to run on the first time it is launched.

If you receive a weird AppleScript / Automator error similar to '**Expected “"” but found unknown token.**', make sure to use underscores instead of spaces in your folder names in this path, AppleScript seems to handle spaces poorly.
