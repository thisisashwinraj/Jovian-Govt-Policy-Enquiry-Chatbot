# Jovian Bot - ChatBot for E-Governance

Jovian is a [DialogFlow](https://cloud.google.com/dialogflow) powered conversational chatbot developed to deliver information regarding latest Government schemes and affiliated policies for public services. The NLP based conversational platform can be used to interact with the public, provide assistance with tasks, analyse sentiments and collect and analyze data to offer appropriate services

This project was started in April 2022 as a combined initiative by [Ashwin](https://github.com/thisisashwinraj), & [Gayathri](https://github.com/rameshgayathri), and has been licensed under the [Eclipse Public License 2.0](https://github.com/thisisashwinraj/JovianBot-Policy-Chatbot/blob/main/LICENSE) . All PR's are maintained by Ashwin. Try interacting with Jovian deployed over Telegram [here](http://t.me/jovian_bot).

# SubDirectories and Deployment Platforms

### Files and Folders
**[Intents:](https://github.com/thisisashwinraj/JovianBot-ChatBot-For-Social-Good)** This folder contains over 100+ intents that are used to categorize user intentions, for each conversation turns.
<br>**[Entities:](https://github.com/thisisashwinraj/JovianBot-Policy-Chatbot/tree/main/entities)** This subdirectory contains entities that are used to identify & extract specific data from end-user expressions.
<br>**[agent.json](https://github.com/thisisashwinraj/JovianBot-Policy-Chatbot/blob/main/agent.json)** & **[package.json](https://github.com/thisisashwinraj/JovianBot-Policy-Chatbot/blob/main/package.json)** are inline editor file, & are not overwritten when importing/restoring the dialogflow agent

### Deployment Platforms

Direct end-user interactions are handled by [DialogFlow](https://dialogflow.cloud.google.com/) in a platform-specific way. Currently, Jovian is integrated only with text based platforms like Telegram and Messenger. These integrations are fully supported by DialogFlow and are configured with the DialogFlow Console. DialogFlow phone Gateway and a variety of other partner [built-in telephony integrations](https://cloud.google.com/dialogflow/cx/docs/concept/integration) are currently under alpha/beta testing and are scheduled to be made available in the upcoming versions

# Usage, Development and Privacy Policy

To invoke this bot, the user can simply start with a greeting or a query. This agent is set to match with user's language settings. The [default welcome intents](https://github.com/thisisashwinraj/JovianBot-ChatBot-For-Social-Good/blob/main/intents/Default%20Welcome%20Intent.json) usually includes a short description of the services that Jovian can deliver. Quick replies, and card responses are available for the Telegram deployment of the bot for user convenience. [Dialogflow API](https://cloud.google.com/dialogflow/es/docs/reference/rest/v2-overview) requests and responses are logged to [Cloud Logging](https://cloud.google.com/logging). As per the privacy policy, the users data is totally secure and no maintainer has any access over the messages that the user may send to the action or the responses that it sends back

![](https://github.com/thisisashwinraj/JovianBot-Policy-Chatbot/blob/main/flutterbot/assets/jovianBotDemo.gif)

[Interaction logs](https://cloud.google.com/dialogflow/es/docs/interaction-logging) capture conversation messages from both end-users, and the agent. This user information may reside within the agent's logs stored by Dialogflow for upto 400 days. Interactions that had issues with intent matching show a warning icon in yellow and the interactions that had webhook errors show a warning icon in red. Usage data such as information regarding the number of users using the bot, the geographical regions they are located in, and basic data including users’ language preference, device type, and length, & frequency of use can be accessed to make bot better

The Privacy Policy for this chatbot can be found [here](https://drive.google.com/file/d/15lGNlJJCo90k0x6s2jnaozdx_fpK8lv8/view?usp=sharing). Jovian does not require the users to sign up into a new account (some third-parties may require signingup). No cloud functions provided by Firebase are used for developing this bot

# Contribution and Guidelines

To start contributing to the project, clone the repository into your local system subdirectory using the below git code:
```
https://github.com/thisisashwinraj/JovianBot-Policy-Chatbot.git
```
Before cloning the repository, make sure to navigate to the working subdirectory of your command line interface and ensure that no folder with same name exists. Other ways to clone the repository includes using a password protected SSH key, or by using [Git CLI](https://cli.github.com/). The changes may additionally be performed by opening this repo using [GitHub Desktop](https://desktop.github.com/)

### Edit the Source Code and Make Desired Changes

Goto the [DialogflowConsole](https://www.google.com/url?sa=t&rct=j&q=&esrc=s&source=web&cd=&cad=rja&uact=8&ved=2ahUKEwj-nLqpgOf5AhWuR2wGHSJcBD8QFnoECAIQAQ&url=https%3A%2F%2Fdialogflow.cloud.google.com%2F&usg=AOvVaw2AsLbzcr82t1GsECYjUNf0) and select custom intent option. Import the code into Dialogflow. Make the appropriate changes, test the dialogflow agent on the simulator, download the ZIP file and make a pull request on this repository.

### Submitting a Pull Request
Before opening a Pull Request, it is recommended to have a look at the full contributing page to make sure your code complies with all the pull request guidelines. Please ensure that you satisfy the [~/checklist](https://github.com/thisisashwinraj/JovianBot-ChatBot-For-Social-Good/blob/main/.github/PULL_REQUEST_TEMPLATE/pull_request_template.md) before submitting your PR.

Navigate to this subdirectory & check status of all files that were altered (red) by running the below code in Git Bash:
```
git status
```
Stage all your files that are to be pushed into your pull request. This can be done in two ways - stage all or some files:
```
git add .            // adds every single file that shows up red when running git status
```
```
git add <filename>   // type in the particular file that you would like to add to the PR
```

Commit all the changes that you've made and describe in brief the changes that you have made using this command:
```
git commit -m "<commit_message>"
```
Push all of your updated work into this GitHub repo in the form of a Pull Request by running the following command:
```
git push origin main
```
All pull requests are reviewed on a monthly rolling basis. Your understanding is appreciate during this review process.

# License and Project Status
Jovian Bot and all of its resources are distributed under [Eclipse Public License 2.0](https://github.com/thisisashwinraj/JovianBot-ChatBot-For-Social-Good/blob/main/LICENSE). The bot is integrated with [Telegram](http://t.me/jovian_bot) and Messenger. The latest released stable version of Jovian Bot is v1.0.0, and is available in English Language. All new releases are logged in the [/Versions](https://github.com/thisisashwinraj/JovianBot-ChatBot-For-Social-Good/tree/main/versions). The agent is currently in beta phase, and more updates will be released in future

Upcoming versions will include support for more policies, new platform integrations, & better user-intents matchings.
