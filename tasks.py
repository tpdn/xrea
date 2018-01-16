from invoke import task


@task
def clean(ctx):
    ctx.run('rm -rf xrea.egg-info')
    ctx.run('rm -rf */__pycache__')
    ctx.run('rm -rf */*/__pycache__')
    ctx.run('rm -rf dist')
    ctx.run('rm -rf build')


@task
def build(ctx):
    ctx.run('python setup.py sdist')
    ctx.run('python setup.py bdist_wheel')


@task
def upload_testpypi(ctx):
    ctx.run('twine upload --repository testpypi dist/*')


@task
def upload(ctx):
    ctx.run('twine upload dist/*')


@task
def format_source(ctx):
    ctx.run('pyformat -i -r -a xrea/*.py tasks.py setup.py')
