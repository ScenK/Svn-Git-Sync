# SVN-Git automatated sync script

## requirements
  - Python
  - Fabric
  - Subversion
  - Git

## installation (Linux Ubuntu)

```bash
  sudo apt-get install python-pip

  pip install fabric
```

## one command line trigger

```bash
    fab sync
```

## logic structure
  - Copy & Commit instead of gitlab bare sync make it easier to deal with confilcts
  - SVN update -> Git update -> Sync files -> Git commit -> Git push

```bash
~/
├── svn-source-folder/
├── git-source-folder/
└── fabfile.py
```