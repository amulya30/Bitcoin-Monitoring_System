<h1 align="center"> Bitcoin Monitoring System

<a href="https://www.python.org/"><img src="https://img.shields.io/badge/Python-inside-yellow?style=for-the-badge&logo=python" /></a> <a href="https://www.docker.com/"><img src="https://img.shields.io/badge/IoT-inside-green?style=for-the-badge&logo=buzzer" /></a>
</h1>

<h4 align="center"> ~ An experiment in development to monitor the fluctuating price of bitcoin without the user worrying about each and every single change in the price. </h4>

## :scroll: About

1. This repository contains an easy to use logic that brings the current bitcoin price to the user.
2. Then it notifies the user by beeping the buzzer if the price is not suitable to the user.
3. Also it alerts the user by sending a text message through telegram messaging service in case the user has missed the beep of the buzzer.

## :dart: Features

<ul type="square">
 <li>Uses ESP8266 Wi-Fi Module</li>
 <li>Uses Piezo electric buzzer</li>
 <li>Linux Compatible</li>
 <li>Allows setting a user specific threshold</li>
</ul>

## :blue_book: Working

<ol type="number">
 <li>Application allows the user to set a specific threshold price for the bitcoin.</li>
 <li>Next the application makes a request to the API endpoint from where it fetches the price.
 <li>Now it compares the fetched bitcoin price with that of the threshold price.</li>
 <li>On comparision if the price differs from that of the set threshold a notification is sent to the user to notify about the change.</li>
</ol>

## :clap: Want to contribute? You are most welcome :smiley:

- Contributions make the open source community such an amazing place to learn, inspire, and create. Any contributions you make are greatly appreciated. Please follow  the following steps whenever you wish to contribute:

   1. Fork the repository
   2. Create your Feature Branch 
        ``` git checkout -b feature/AmazingFeatureName ```
   3. Commit your Changes 
        ``` git commit -m 'Add some AmazingFeatureName' ```
   4. Push to the Branch 
         ``` git push origin feature/AmazingFeatureName ```
   5. Finally open a Pull Request by clicking <a href="https://github.com/amulya30/Text_Similarity_API/pulls">here</a>

- Or if you have any suggestions that would make this application better, you can just simply open an issue with the tag "enhancement" or "bug" by clicking <a href="https://github.com/amulya30/Text_Similarity_API/issues">here</a>

