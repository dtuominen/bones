from fabric.api import local, lcd

# This function will run the test suite, commit your branch change,
# and merge your branch with master
def prepare_deployment(branch_name=None):
    local('python manage.py test basicapp')
    local('git add -p && git commit')
    if branch_name is not None:
        local('git checkout master && git merge' + branchname)


def deploy():
    """
    simple deployment script
    cds into base directory of the production files and git pulls
    cds into myproject/ directory because that's where manage.py is located
    runs tests and migrations
    """
    with lcd('/home/dylan/production/my-project'):
        local('git pull /home/dylan/proj/my-project/')
    with lcd('/home/dylan/production/my-project/myproject'):
        local('python manage.py migrate basicapp')
        local('python manage.py test basicapp')
        #local ('/command/to/restart/server')

    
