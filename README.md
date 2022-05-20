# Jovian-Bot

Jovian is a Dialogflow powered conversational chatbot developed to deliver information regarding government schemes and affiliated policies for public services. The NLP based conversational platform can be used to interact with the public, provide assistance with tasks, analyse sentiments, & collect & analyze data to offer appropriate services.

The project was starteded in May 2022 as a combined initiative by Ashwin and Gayathri and has been licensed under the Eclipse Public License 2.0 . All pull requests are maintained by Ashwin. Try interacting with Jovian deployed over Telegram here.

# SubDirectories and Deployment Platforms

### Files and Folders
- **Intents:** This folder contains over 100 intents that are used to categorize end-user intentions for each conversation turn.
- **Entities:** This subdirectory contains entities that are used to identify and extract specific data from end-user expressions.
- **agent.json** and **package.json** are inline editor file, & are not overwritten when importing/restoring the dialogflow agent.

### Deployment Platforms

Direct end-user interactions are handled by Dialogflow in a platform-specific way. Currently, Jovian is integrated only with text based platforms like Telegram and Facebook  Messenger. These integrations are fully supported by Dialogflow and are configured with the Dialogflow Console. Dialogflow phone Gateway and partner built-in telephony integrations are  currently under testing and is scheduled to be available in the upcoming version.

# Usage, Development and Privacy Policy

To invoke the bot, the  user can simply start with a greeting or a query. The action is set to match the user's language settings. The default welcome intent usually includes a short description of the services that Jovian can deliver. Quick replies and card responses are available for the Telegram deployment of the bot for user convenience. Dialogflow API requests and responses are logged to Cloud Logging. As per the privacy policy, the user data is totally secure and no maintainer has any access over the messages the user may send to the action or the responses that it sends back. The action also does not require the user to provide any account linking or login information.

Interaction logs capture conversation messages from both end-users and the agent. User information may reside within the agent's logs stored by Dialogflow for upto 400 days. Interactions that had issues with intent matching show a warning icon in yellow and the interactions that had webhook errors show a warning icon in red. Usage data such as information regarding how many users are using the bot, which geographical regions they are located in, and basic data including users’ language, device type, and length and frequency of use can be accessed and used to make the action better and add features. 

The privacy policy for the chatbot can be found here. Jovian does not require the users to sign up for new accounts (integrating third -parties may require signing up to their platform). No cloud functions provided by firebase are used for developing the action.

# Contribution and Guidelines

To start contributing to the project, clone the repository into your local system subdirectory using the below git code:
```

```
Before cloning the repository, make sure to navigate to the working subdirectory of your command line interface and ensure that no folder with same name exists. Other ways to clone the repository includes using a password protected SSH key or by using Git CLI. The changes may additionally be performed by opening this repo using GitHub Desktop

### Edit the Source Code and Make Desired Changes

Go to the Dialogflow Console and select custom intent. Import the code into DialogFlow. Make the appropriate changes, test the bot agent on the simulator, download the ZIP file and make a pull request on this repository.

### Submitting a Pull Request
Before opening a Pull Request, it is recommended to have a look at the full contributing page to make sure your code complies with all the pull request guidelines. Please ensure that you satisfy the [~/checklist]() before submitting your PR.

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

Commit all the changes that you've made & describe in brief the changes that you have made, using this command:
```
git commit -m "<commit_message>"
```
Push all of your updated work into this GitHub repo in the form of a Pull Request by running the following command:
```
git push origin main
```
All pull requests are reviewed on a monthly rolling basis. Your understanding is appreciate during this review process.

# License and Project Status
Jovian Bot and all of its resources are distributed under [Eclipse Public License 2.0](). The bot is integrated over Telegram and Messenger. The latest released stable version of Jovian Bot is v1.0.0, and is available in English Language. All new releases are logged in the [~/Stable Versions]()

Upcoming updates will include more features, optimized recommendations using tf/idf, and faster result predictions

Upcoming versions will include support for more policies, new platform integrations & better user-intent matchings
