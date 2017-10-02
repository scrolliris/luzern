# Lozärn

`/ˌluːˈsɜːrn/`

[![build status](https://gitlab.com/lupine-software/luzern/badges/master/build.svg)](
https://gitlab.com/lupine-software/luzern/commits/master)

```txt
   _
\_|_)             + +
  |     __   __   __,   ,_    _  _
 _|    /  \_/ / _/  |  /  |  / |/ |
(/\___/\__/  /_/ \_/|_/   |_/  |  |_/
              /|
              \|

Luzärn; scrolLiris's Upstream Zig zAg cuRved chaNgelog
```

This is changelog website for the [Scrolliris](
https://about.scrolliris.com/).


## Repository

[https://gitlab.com/lupine-software/luzern](
https://gitlab.com/lupine-software/luzern)


## Requirements

* Asciidoc


## Setup

```zsh
% python -V
3.5.4
% python -m venv venv
% source ./venv/bin/activate
(venv) % pip install --upgrade pip setuptools
(venv) % pip install Lektor -c constraints.txt
```

## Serve

```zsh
(venv) % cd site
(venv) % lektor server
```


## Build

```zsh
(venv) % cd site
(venv) % lektor build --output-path ../public
```


## License

Copyright (c) 2017 Lupine Software LLC

### Software (Program)

This is free software:  
You can redistribute it and/or modify it under the terms of
the [BSD 3-Clause License](
https://opensource.org/licenses/BSD-3-Clause))

### Articles and Images (Content)

The is distributed as **GNU Free Documentation
License**. (version 1.3)

Permission is granted to copy, distribute and/or modify this document
under the terms of the GNU Free Documentation License, Version 1.3
or any later version published by the Free Software Foundation;
with no Invariant Sections, no Front-Cover Texts, and no Back-Cover Texts.
A copy of the license is included in the section entitled "GNU
Free Documentation License".

See [LICENSE](LICENSE). (`GFDL-1.3`)
