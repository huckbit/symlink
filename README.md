# SYMLINK
Symlink script for python2x: Create and remove symlink quickly in the current directory.

Use this script to link the document root for your apache virtual host quickly. You need just to have the files `symlink.py` inside the directory where you want to create the symlink. The default dir name is `public_html` modify this variable setting if you need to link another folder.

### How to use it

From the project folder launch the command:

```shell
python symlink.py
```

and follow the instruction.

It's possible to launch the script also with:
```shell
./symlink.py
# make sure you have the permission to execute the file.
```


![symlink](https://gitlab.com/huckbit/blog-images/raw/master/symlink.gif)
