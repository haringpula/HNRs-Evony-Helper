<div id="top"></div>
<!--
*** Thanks for checking out the Best-README-Template. If you have a suggestion
*** that would make this better, please fork the repo and create a pull request
*** or simply open an issue with the tag "enhancement".
*** Don't forget to give the project a star!
*** Thanks again! Now go create something AMAZING! :D
-->

<!-- PROJECT SHIELDS -->
<!--
*** I'm using markdown "reference style" links for readability.
*** Reference links are enclosed in brackets [ ] instead of parentheses ( ).
*** See the bottom of this document for the declaration of the reference variables
*** for contributors-url, forks-url, etc. This is an optional, concise syntax you may use.
*** https://www.markdownguide.org/basic-syntax/#reference-style-links
-->
[![Contributors][contributors-shield]][contributors-url]
[![Forks][forks-shield]][forks-url]
[![Stargazers][stars-shield]][stars-url]
[![Issues][issues-shield]][issues-url]
[![MIT License][license-shield]][license-url]
[![LinkedIn][linkedin-shield]][linkedin-url]

<!-- PROJECT LOGO -->
<br />
<div align="center">
  <a href="https://github.com/haringpula/HNRs-Evony-Helper">
    <img src="https://cdn.discordapp.com/attachments/968595427228286976/972125616730144778/honor2_031019-1.jpg" alt="Logo" width="80" height="80">
  </a>

<h3 align="center">HNRs Evony Discord Bot</h3>

  <p align="center">
    Discord Bot for HNR's Evony TKR Server
    <br />
    <a href="https://github.com/haringpula/HNRs-Evony-Helper"><strong>Explore the docs »</strong></a>
    <br />
    <br />
    <a href="https://github.com/haringpula/HNRs-Evony-Helper">View Demo</a>
    ·
    <a href="https://github.com/haringpula/HNRs-Evony-Helper/issues">Report Bug</a>
    ·
    <a href="https://github.com/haringpula/HNRs-Evony-Helper/issues">Request Feature</a>
  </p>
</div>

<!-- TABLE OF CONTENTS -->
<details>
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
      <ul>
        <li><a href="#built-with">Built With</a></li>
      </ul>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#prerequisites">Prerequisites</a></li>
        <li><a href="#installation">Installation</a></li>
      </ul>
    </li>
    <li><a href="#usage">Usage</a></li>
    <li><a href="#roadmap">Roadmap</a></li>
    <li><a href="#contributing">Contributing</a></li>
    <li><a href="#license">License</a></li>
    <li><a href="#contact">Contact</a></li>
    <li><a href="#acknowledgments">Acknowledgments</a></li>
  </ol>
</details>

<!-- ABOUT THE PROJECT -->
## About The Project

[![Product Name Screen Shot][product-screenshot]](https://example.com)

Discord Bot for HNR's Evony The Kings Return Server. Created to aid HNR alliance. Can compute troop costs and power increase, and handy commands to show current server time/day. Made with discord.py and hosted on Repl.it by author [King Red Sanchez](king.red@gmail.com).

<p align="right">(<a href="#top">back to top</a>)</p>

### Built With

* [Python](https://www.python.org/)
* [Repl.it](https://replit.com/)
* [discord.py](https://discordpy.readthedocs.io/en/stable/)
* [Flask](https://flask.palletsprojects.com/en/2.1.x/)

<p align="right">(<a href="#top">back to top</a>)</p>

<!-- GETTING STARTED -->
## Getting Started

To get a copy up and running follow these simple steps.

### Prerequisites

This Repl implements *discord.py* with `@bot.commands`, and you can install this dependency with

* pip

  ```sh
  py -3 -m pip install -U discord.py  
  ```

### Installation

1. Get your bot's **TOKEN** at [the Discord Developer Portal](https://discord.com/developers/applications)

2. Fork the repl [here](https://replit.com/@King-RedRed/HNRs-Evony-Helper)

3. Enter your **TOKEN** in *Secrets (Environment Variables)* tab, or with a `.env` file with

   ```
   TOKEN = 'ENTER YOUR TOKEN';
   ```

<p align="right">(<a href="#top">back to top</a>)</p>

<!-- USAGE EXAMPLES -->
## Usage

* `$time` will display current server time

* `$calc TroopType TroopTier Troop Amount` will display the needed resources to complete that amount

  ```
  $calc r 14 1000000
  
  Input
  Troop Type = R
  Troop Tier = 14
  Troop Amount = 1000000
  
  Output
  Food = 4500000000
  Wood = 13500000000
  Stone = 4500000000
  Iron = 0
  Gold = 200000000
  Power Increase: 122000000
  ```

_For more examples, please refer to the [Documentation](https://github.com/haringpula/HNRs-Evony-Helper)_

<p align="right">(<a href="#top">back to top</a>)</p>

<!-- ROADMAP -->
## Roadmap

* [x] Evony Troop Calculator
* [ ] Evony Terminology Database
* [ ] Evony Server Time/Day commands
  * [x] Time/Day support
  * [ ] Event Reminder

See the [open issues](https://github.com/haringpula/HNRs-Evony-Helper/issues) for a full list of proposed features (and known issues).

<p align="right">(<a href="#top">back to top</a>)</p>

<!-- CONTRIBUTING -->
## Contributing

Contributions are what make the open source community such an amazing place to learn, inspire, and create. Any contributions you make are **greatly appreciated**.

If you have a suggestion that would make this better, please fork the repo and create a pull request. You can also simply open an issue with the tag "enhancement".
Don't forget to give the project a star! Thanks again!

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

<p align="right">(<a href="#top">back to top</a>)</p>

<!-- LICENSE -->
## License

Distributed under the MIT License. See `LICENSE.txt` for more information.

<p align="right">(<a href="#top">back to top</a>)</p>

<!-- CONTACT -->
## Contact

Your Name - [@haringpula](https://github.com/haringpula) - king.red@gmail.com

Project Link: [https://github.com/haringpula/HNRs-Evony-Helper](https://github.com/haringpula/HNRs-Evony-Helper)

<p align="right">(<a href="#top">back to top</a>)</p>

<!-- ACKNOWLEDGMENTS -->
## Acknowledgments

* [othneildrew](https://github.com/othneildrew/Best-README-Template)
* The awesome people of HNR alliance in Evony The Kings Return

<p align="right">(<a href="#top">back to top</a>)</p>

<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->
[contributors-shield]: https://img.shields.io/github/contributors/haringpula/HNRs-Evony-Helper.svg?style=for-the-badge
[contributors-url]: https://github.com/haringpula/HNRs-Evony-Helper/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/haringpula/HNRs-Evony-Helper.svg?style=for-the-badge
[forks-url]: https://github.com/haringpula/HNRs-Evony-Helper/network/members
[stars-shield]: https://img.shields.io/github/stars/haringpula/HNRs-Evony-Helper.svg?style=for-the-badge
[stars-url]: https://github.com/haringpula/HNRs-Evony-Helper/stargazers
[issues-shield]: https://img.shields.io/github/issues/haringpula/HNRs-Evony-Helper.svg?style=for-the-badge
[issues-url]: https://github.com/haringpula/HNRs-Evony-Helper/issues
[license-shield]: https://img.shields.io/github/license/haringpula/HNRs-Evony-Helper.svg?style=for-the-badge
[license-url]: https://github.com/haringpula/HNRs-Evony-Helper/blob/master/LICENSE.txt
[linkedin-shield]: https://img.shields.io/badge/-LinkedIn-black.svg?style=for-the-badge&logo=linkedin&colorB=555
[linkedin-url]: https://linkedin.com/in/king-red-sanchez-3507ab219/
[product-screenshot]: https://cdn.discordapp.com/attachments/977545429342371920/977549159047516201/unknown.png
