# Lozärn

`/ˌluːˈsɜːrn/`

[![pipeline status][ci-build]][commit] [![coverage report][ci-cov]][commit]


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

This project is distributed as various licenses by parts.

```txt
Lozärn
Copyright (c) 2017 Lupine Software LLC
```

### Software (Program)

`BSD-3-Clause`

The programs in this project are distributed as
BSD 3-Clause License.

```
THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS" AND
ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO,
THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE
ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE
LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY,
OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF
SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR
BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY,
WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR
OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED
OF THE POSSIBILITY OF SUCH DAMAGE.
```

Check the [BSD 3-Clause](https://opensource.org/licenses/BSD-3-Clause) License.

### Documentation and Resource (image)

`GFDL-1.3`

The translation files (`*.po` and `*.pot`) are distributed as
GNU Free Documentation License. (version 1.3)

```txt
Permission is granted to copy, distribute and/or modify this document
under the terms of the GNU Free Documentation License, Version 1.3
or any later version published by the Free Software Foundation;
with no Invariant Sections, no Front-Cover Texts, and no Back-Cover Texts.
A copy of the license is included in the section entitled "GNU
Free Documentation License".
```

See [LICENSE](LICENSE).


[ci-build]: https://gitlab.com/lupine-software/luzern/badges/master/build.svg
[ci-cov]: https://gitlab.com/lupine-software/luzern/badges/master/coverage.svg
[commit]: https://gitlab.com/lupine-software/luzern/commits/master
