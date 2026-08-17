# ElViz

[![PyPI version](https://img.shields.io/pypi/v/ElViz.svg)](https://pypi.org/project/ElViz/)
[![PyPI downloads](https://static.pepy.tech/badge/ElViz/month)](https://pepy.tech/projects/ElViz)

E-CAD (electrical CAD) projects with python.

Describe your devices with python classes and symbols in svg format or import them from the devices repository.
Import and instantiate the device classes in the circuit definition file and connect them using the connection decorator.
Create page definition files by importing and positioning the device instances from the circuit definition using the wire class to visualize connections. Use the CLI  to preview and render your pages. The border and title-block of the pages are defined in separate files and applied to the pages by the CLI or idevidualy by the page definitions. 

Use inbuilt templates or simply create and empty project with definitions for common pages like tile, contents and terminal blocks to create your own. Use the simple copy mechanism provided py the the CLI or advanced tools like [cookiecutter](https://github.com/cookiecutter/cookiecutter) too apply templates to new projects. The resulting project is fully compatible with standard software version control like [git](https://git-scm.com/). 

* [GitHub](https://github.com/PBK-DEV/ElViz/) | [PyPI](https://pypi.org/project/ElViz/) | [Documentation](https://PBK-DEV.github.io/ElViz/)
* Created by [Paul B. Kochta](https://elviz.kochta.eu) | GitHub [@PBK-DEV](https://github.com/PBK-DEV) | PyPI [@PaulBK](https://pypi.org/user/PaulBK/)
* [EUROPEAN UNION PUBLIC LICENCE v. 1.2](https://eupl.eu/)

## Features

- [ ] describe your E-CAD project with python code by importing the elviz package
    - [ ] classes that model project, circuit, devices and documentation pages (elek. drawing)
    - [ ] project structure similar to python projects
    - [ ] use standard dev tools (pip, uv, .env, git ...) for project management
    - [ ] combine with any python package to add/customize functionality
- [ ] rendering to SVG for full visual flexibility
- [ ] CLI tool for project management
    - [ ] init new projects
    - [ ] update repository of devices 
    - [ ] visualize the circuit
    - [ ] live visualization of pages
    - [ ] render the documentation to pdf, dxf or svg
    - [ ] embed external documentation like mechanical drawings, data-sheets ...
- [ ] GitHub based repository of electric, pneumatic and hydraulic device-definitions to us in your projects
- [ ] [FreeCAD](https://freecad.org) AddOn as GUI and for integrating mechanical and electrical CAD
- [ ] import device symbols from [QElectrotech](https://qelectrotech.org/)
- [ ] import [EPlan](https://www.eplan.com)-Makros
- [ ] simulate circuits and ty in the automation software components for accurate testing

## Installation

```bash
uv add ElViz
```

## Usage

```python
import elviz
```

## Documentation

Documentation is available on
[GitHub Pages](https://PBK-DEV.github.io/ElViz/).

## Contributing

See [CONTRIBUTING.md](CONTRIBUTING.md) for development setup, testing, and
documentation instructions.

## Author

elviz was created in 2026 by Paul B. Kochta.

Built with [Cookiecutter](https://github.com/cookiecutter/cookiecutter) and the [audreyfeldroy/cookiecutter-pypackage](https://github.com/audreyfeldroy/cookiecutter-pypackage) project template.
