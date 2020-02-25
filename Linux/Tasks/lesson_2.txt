student@Ubuntu-MySQL-VirtualBox:~/lesson_2$ mkdir first
student@Ubuntu-MySQL-VirtualBox:~/lesson_2$ mkdir second
student@Ubuntu-MySQL-VirtualBox:~/lesson_2$ tree
.
├── first
└── second

2 directories, 0 files
student@Ubuntu-MySQL-VirtualBox:~/lesson_2$ cd first/
student@Ubuntu-MySQL-VirtualBox:~/lesson_2/first$ > first.py
student@Ubuntu-MySQL-VirtualBox:~/lesson_2/first$ echo "print(1)" > first.py
student@Ubuntu-MySQL-VirtualBox:~/lesson_2/first$ cat first.py 
print(1)
student@Ubuntu-MySQL-VirtualBox:~/lesson_2/first$ cd ..
student@Ubuntu-MySQL-VirtualBox:~/lesson_2$ cd second/
student@Ubuntu-MySQL-VirtualBox:~/lesson_2/second$ > second.py
student@Ubuntu-MySQL-VirtualBox:~/lesson_2/second$ echo "print(2)" > second.py
student@Ubuntu-MySQL-VirtualBox:~/lesson_2/second$ cat second.py 
print(2)
student@Ubuntu-MySQL-VirtualBox:~/lesson_2/second$ cd ..
student@Ubuntu-MySQL-VirtualBox:~/lesson_2$ tree
.
├── first
│   └── first.py
└── second
    └── second.py

2 directories, 2 files
student@Ubuntu-MySQL-VirtualBox:~/lesson_2$ cd second/
student@Ubuntu-MySQL-VirtualBox:~/lesson_2/second$ mv second.py ../first/
student@Ubuntu-MySQL-VirtualBox:~/lesson_2/second$ cd ..
student@Ubuntu-MySQL-VirtualBox:~/lesson_2$ tree
.
├── first
│   ├── first.py
│   └── second.py
└── second

2 directories, 2 files
student@Ubuntu-MySQL-VirtualBox:~/lesson_2$ rm -r second/
student@Ubuntu-MySQL-VirtualBox:~/lesson_2$ tree
.
└── first
    ├── first.py
    └── second.py

1 directory, 2 files
student@Ubuntu-MySQL-VirtualBox:~/lesson_2$ mv first/ first_second
student@Ubuntu-MySQL-VirtualBox:~/lesson_2$ tree
.
└── first_second
    ├── first.py
    └── second.py

1 directory, 2 files
student@Ubuntu-MySQL-VirtualBox:~/lesson_2$ rm -r first_second/
student@Ubuntu-MySQL-VirtualBox:~/lesson_2$ tree
.

0 directories, 0 files



