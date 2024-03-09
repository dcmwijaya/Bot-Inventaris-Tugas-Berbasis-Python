[![Open Source Love](https://badges.frapsoft.com/os/v1/open-source.svg?style=flat)](https://github.com/ellerbrock/open-source-badges/)
[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg?logo=github&color=%23F7DF1E)](https://github.com/devancakra/Bot-Inventaris-Tugas-Berbasis-Python)
[![ISSN](https://img.shields.io/badge/ISSN-2686%E2%80%936099-blue.svg?logo=google-scholar&color=98FB98)](http://www.ejournal.upnjatim.ac.id/index.php/scan/article/view/2352)
![GitHub Star](https://img.shields.io/github/stars/devancakra/Bot-Inventaris-Tugas-Berbasis-Python.svg?color=FF69B4)
![GitHub Contributor](https://img.shields.io/github/contributors/devancakra/Bot-Inventaris-Tugas-Berbasis-Python.svg?color=FF8C00)
![GitHub last commit](https://img.shields.io/github/last-commit/devancakra/Bot-Inventaris-Tugas-Berbasis-Python)
![Python](https://img.shields.io/badge/-Python-blue.svg?style=flat&logo=python&logoColor=white)

# Bot-Telegram-Python-Inventaris-Tugas
<strong>2nd Final Project in API Programming</strong><br>

This project is closely related to telegram bots, which themselves have an important role in teaching and learning activities in a classroom. This bot can perform task inventory periodically. This bot is built with the help of a platform called ``` pythonanywhere ```. In this project, the program creator uses ``` python version 3.6 ``` because it is known to have advantages in syntax. The purpose of this project is to help lecturers or teachers in taking inventory of their students' assignments and anticipate errors that might occur, namely forgetting to recap, this is due to the busy messaging activities in a class social media group, in this case telegram.

<br>

## Project Requirements
| Part | Description |
| --- | --- |
| Features | Reply Keyboard, Inline Keyboard, Error Handling, Inventory, User Log Activity |
| Platform | Pythonanywhere |
| Library | telebot, datetime |
| Code | Python 3.6 |

<br>

## Bot Capabilities
1. There are menu options that can be accessed by clicking or typing.
   
2. It can also detect incoming files or documents and notify the sender directly.
   
3. Another ability of this bot is that it can provide notification to the bot owner that someone has accessed a certain menu, so that the bot owner can monitor the movements that occur directly.
   
4. This bot can address both group users and non-group users.
   
5. There is problem control in the system, if the message does not match the command it will be redirected to the ``` /help ``` command.

<br>

## Get Started
1. Download this repository and extract it.
   
2. Register for a ``` pythonanywhere account ``` :<br>

   ```bash
   https://www.pythonanywhere.com/registration/register/beginner/
   ```
3. Login to ``` pythonanywhere account ```.
   
4. Create a new directory on the ``` pythonanywhere platform ``` by clicking on ``` Files ``` at the top -> Type in the ``` Directories ``` section: ``` KelasApi ``` -> Click ``` New directory ```.

5. Then upload ``` Bot-InventarisTugas.py ``` by clicking the ``` Upload a file ``` button.

6. Return to the previous page, which is at ``` /home/[pythonanywhere username] ``` -> Click on ``` Open Bash console here ```.
  
7. Then type this in the console in rotation:

   ```bash
   mkvirtualenv myvirtualenv --python=/usr/bin/python3
   ```
   <img width="810" src="https://github.com/devancakra/Bot-Inventaris-Tugas-Berbasis-Python/assets/54527592/da359630-98c8-4742-a1d8-7a2f9beb282a">
   <br><br>

   ```bash
   pip install pytelegrambotapi
   ```
   <img width="810" src="https://github.com/devancakra/Bot-Inventaris-Tugas-Berbasis-Python/assets/54527592/c452c0b8-38f6-4ca0-987d-01e28ef0c3be">
   <br><br>

   ```bash
   pip install datetime
   ```
   <img width="810" src="https://github.com/devancakra/Bot-Inventaris-Tugas-Berbasis-Python/assets/54527592/e1ce9401-ac0d-4fff-8f93-8dbb89a893a9">
   <br><br>

   ```bash
   cd KelasApi
   ```
   <img width="810" src="https://github.com/devancakra/Bot-Inventaris-Tugas-Berbasis-Python/assets/54527592/ba30f775-d385-4433-b8c5-a74b2086fc60">
   <br><br>

   ```bash
   python3 Bot-InventarisTugas.py
   ```
   <img width="810" src="https://github.com/devancakra/Bot-Inventaris-Tugas-Berbasis-Python/assets/54527592/8391e6f8-de4b-4315-942a-4570385cc763">
   <br>

8. Enjoy [Done].

<br>

## Reminder
• Pay attention to writing good and correct syntax because python is case sensitive.

• Make sure your PC/Laptop is connected to the internet.

<br>

## Highlights
<table>
<tr>
<th colspan="4">Telegram Bot</th>
</tr>
<tr>
<td width="280"><img src="https://github.com/devancakra/Bot-Inventaris-Tugas-Berbasis-Python/assets/54527592/08217f59-1fc8-4721-a67c-4d604c4286e4" alt="TGbot-1"></td>
<td width="280"><img src="https://github.com/devancakra/Bot-Inventaris-Tugas-Berbasis-Python/assets/54527592/9d5e906a-63a8-4913-97a3-1b86aabb9d0c" alt="TGbot-2"></td>
<td width="280"><img src="https://github.com/devancakra/Bot-Inventaris-Tugas-Berbasis-Python/assets/54527592/9b684607-ca9f-4764-bf34-7ccd056fda0d" alt="TGbot-3"></td>
</tr>
<tr>
<td width="280"><img src="https://github.com/devancakra/Bot-Inventaris-Tugas-Berbasis-Python/assets/54527592/cde5ec27-79ed-412e-9b4b-33d3062bc50b" alt="TGbot-4"></td>
<td width="280"><img src="https://github.com/devancakra/Bot-Inventaris-Tugas-Berbasis-Python/assets/54527592/44b7d8f9-f3a2-42dc-a1b5-23ff54899062" alt="TGbot-5"></td>
<td width="280"><img src="https://github.com/devancakra/Bot-Inventaris-Tugas-Berbasis-Python/assets/54527592/ad0936cf-e162-42c0-a6d1-9a9ae192fbd4" alt="TGbot-6"></td>
</tr>
</table>

<br>

## Demonstration of Application
Via Telegram: <a href="http://t.me/inventaristugas_bot">@inventaristugas_bot</a>

<br>

## Appreciation
If you find this work useful, please support it as a token of appreciation to the author by clicking the ``` ⭐Star ``` button.

<br>

## Disclaimer
This application has been created by including third-party sources. Third parties here are service providers, whose services are in the form of libraries, frameworks, and others. I thank you very much for the service. It has proven to be very helpful and implementable.

<br>

## LICENSE
MIT License - Copyright © 2020 - Devan Cakra Mudra Wijaya

Permission is hereby granted without charge to any person obtaining a copy of this software and the software-related documentation files to deal in them without restriction, including without limitation the right to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons receiving the Software to be furnished therewith on the following terms:

The above copyright notice and this permission notice must accompany all copies or substantial portions of the Software.

IN ANY EVENT, THE AUTHOR OR COPYRIGHT HOLDER HEREIN RETAINS FULL OWNERSHIP RIGHTS. THE SOFTWARE IS PROVIDED AS IS, WITHOUT WARRANTY OF ANY KIND, EITHER EXPRESS OR IMPLIED, THEREFORE IF ANY DAMAGE, LOSS, OR OTHERWISE ARISES FROM THE USE OR OTHER DEALINGS IN THE SOFTWARE, THE AUTHOR OR COPYRIGHT HOLDER SHALL NOT BE LIABLE, AS THE USE OF THE SOFTWARE IS NOT COMPELLED AT ALL, SO THE RISK IS YOUR OWN.
