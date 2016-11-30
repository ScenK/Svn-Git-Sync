from fabric.api import local, task, execute

git_path = "/path/to/git_source"
svn_path = "/path/to/svn_source"

@task
def sync():
    execute(svn_up)
    execute(git_up)
    execute(transfer)
    execute(git_commit)

@task
def svn_up():
    local("svn up %s ." % svn_path)

@task
def git_up():
    local("git -C %s pull --rebase" % git_path)

@task
def transfer():
    ignore = ".svn,.git,.DS_Store"
    local("rsync -arv --exclude={%s} %s/. %s/." % (ignore, svn_path, git_path))
    # mv files from svn folder to git folder
    execute(clean_up_deleted_files)

@task
def clean_up_deleted_files():
    result = None


    try:
        result = local("diff -r -x '.git' -x '.gitignore' -x '.DS_Store' %s %s | grep %s" % (svn_path, git_path, git_path), capture=True)
    except:
        pass

    if result:
        for i in result.split('\n'):
            file_path = '/'.join(i[8:].split(': '))
            local("rm %s" % file_path)

@task
def git_commit():
    local("git -C %s add -A" % git_path)
    local("git -C %s commit -m 'Auto Sync from svn source to Gitlab'" % git_path)
    local("git -C %s push" % git_path)
