# Piclodio3

This repository was cloned from https://github.com/Sispheor/piclodio3/.
The original project was written in Python2(django) and Angular 2. I've partial rewritten it in Python3 and Angular 7.

Piclodio is a web radio player and a also an alarm clock that can be installed on Raspberry Pi.
You can add url stream to complete the collection. Scheduling alarm clock is easy and can be periodic.
A local backup MP3 file is used in case of losing internet connection or if the web radio is not anymore available to be sure you'll be awaken.

![piclodio_home](https://github.com/strmark/piclodio3/blob/master/images/piclodio_presentation.png)

## Installation

### Manual install
The project is split in two parts:
- [Backend](back/README.md)
- [Frontend](front/README.md)

Installation procedures have been tested on a Raspberry Pi(raspian) and on debian but the project should works on any Linux system that can handle Django and Angular 7.

## License

Copyright (c) 2019. All rights reserved.

Piclodio is covered by the MIT license, a permissive free software license that lets you do anything you want with the source code, as long as you provide back attribution and "don't hold you liable". For the full license text see the [LICENSE.md](LICENSE.md) file.
