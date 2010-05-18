from setuptools import setup, find_packages

setup(name = "FPyS2",
      version = "0.5.2",
      description = "Amazon FPS Library (version 2008-09-17)",
      author = "Wade Simmons",
      author_email = "wade@wades.im",
      url = "http://github.com/wadey/fpys2",
      packages = ["fpys2"],
      test_suite = "fpys2.tests",
      install_requires = ["wsgi_intercept",
                          ],
      entry_points = {},
      license = 'MIT License',
      long_description = """\
FPyS is a library for interacting with the Amazon Flexible Payment Service.

FPys communicates with the service via the available REST interface.  It handles the
details of request signing and response parsing for the application developer.

An Amazon web services account is required to begin working with FPyS in the development
environment.  An approved account is required to move software into production.

Development Trac: http://fpys.achievewith.us
Mailing List: http://groups.google.com/group/fpys/
""",
      classifiers = [
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python",
        "Topic :: Internet :: WWW/HTTP",
        "Topic :: Software Development :: Libraries :: Python Modules",
        ])
