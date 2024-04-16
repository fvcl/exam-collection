# FVCL Study Material Collection

![Commit Activity](https://img.shields.io/github/commit-activity/m/fvcl/exam-collection)
[![License](https://img.shields.io/badge/License-BSD-blue)](#license)
[![open issues - exam-collection](https://img.shields.io/github/issues/fvcl/exam-collection)](https://github.com/fvcl/exam-collection/issues)
[![closed issues - exam collection](https://img.shields.io/github/issues-closed/fvcl/exam-collection)](https://github.com/fvcl/exam-collection/issues)

[Live Site](https://exams.fvcl.ch)

This repo contains the source for the exam collection site of the computational linguistics student association (CL@ZH). The site provides a platform for users to share and distribute study resources and discuss them.


# Contributing
## Contribution Guidelines

Welcome and thank you for considering contributing to our project! We're thrilled to have you onboard. Here are a few guidelines that we'd like you to follow so that we can have a smooth and enjoyable collaboration process.

### Getting Started
- **Read the docs**: Before you contribute, please read through the documentation and the setup guide in our README. This will help you understand the project better and make your contribution more effective.
- **Check out the issues**: Take a look at the existing issues for tasks that need help or improvements. Feel free to ask for clarifications if something isn’t clear.

### Making Contributions
#### If you are a contributor from the Fachverein Software Development Team
- **Send a message to a project owner**: Currently these are Luc and Lucas, if unsure send a message to fachverein@cl.uzh.ch or ask whoever is webmaster
- **Create a branch**: After you're added to the project, you should be able to create branches and create pull requests in the repo


#### If you are an external contributor
- **Fork the repository**: Make sure to fork the repository and work from your copy.
- **Branching**: Create a new branch for each feature or fix, naming it something relevant to the task you're addressing.
- **Commit messages**: Keep your commit messages clear and informative, describing what has been done and why.

If you're feeling unsure about how to fork the repo and make changes, this article explains it relatively well: 

### Pull Requests
- **Open a pull request (PR)**: Once you’re ready to submit your changes, make a pull request to the main branch. Describe what your code does and link to any relevant issues.
- **Code review**: Wait for at least one code review. We might suggest some changes or improvements.
- **Integration**: Once approved, your PR will be merged into the main branch!

### Stay Involved
- **Feedback**: Don’t hesitate to leave feedback. We're always trying to improve and your opinions matter!
- **Ask questions**: Always feel free to ask questions if you’re unsure about something. We're here to help!

### Code of Conduct
- **Respectful communication**: Please be polite and respectful in your interactions with other community members. We strive to provide a welcoming environment for everyone.

Thank you for contributing to our project! We’re excited to see what you bring to the community.

## Setting up a development environment


### Prerequisites

Before you begin, ensure you have the following installed on your local machine:

- Python (3.11 or later)
- pip (Python package installer)
- Git (Version control system)

#### Environment Setup

Start by cloning the project repository to your local machine using git. 

   ```
   git clone git@github.com:fvcl/exam-collection.git
   cd exam-collection
   ```

It's recommended to use a virtual environment to manage dependencies and isolate project settings. You can create one
using `venv`:

   ```
   python -m venv venv
   ```

Activate the virtual environment:

- On Windows:
  ```
  .\venv\Scripts\activate
  ```
- On macOS and Linux:
  ```
  source venv/bin/activate
  ```

Install the project dependencies using the `requirements.txt` file located in the `exco` folder:

   ```
   pip install -r exco/requirements.txt
   ```

Test the installation by running the application locally:

   ```
   flask run
   ```


### Database Setup
When not running in the production environment (indicated by the environment variable `DEVELOPMENT_MODE` being set to false), the application uses SQLite as the database. The database file is located at `exco/db/exam-collection.db.

To interact with the database locally, you can use `cli.py` to create the tables, insert sample data, and query the database.
```shell
python exco/cli.py
```

## Contribution Guidelines

Welcome and thank you for considering contributing to our project! We're thrilled to have you onboard. Here are a few guidelines that we'd like you to follow so that we can have a smooth and enjoyable collaboration process.

### Getting Started
- **Read the docs**: Before you contribute, please read through the documentation and the setup guide in our README. This will help you understand the project better and make your contribution more effective.
- **Check out the issues**: Take a look at the existing issues for tasks that need help or improvements. Feel free to ask for clarifications if something isn’t clear.

### Making Contributions
- **Fork the repository**: Make sure to fork the repository and work from your copy.
- **Branching**: Create a new branch for each feature or fix, naming it something relevant to the task you're addressing.
- **Commit messages**: Keep your commit messages clear and informative, describing what has been done and why.

### Pull Requests
- **Open a pull request (PR)**: Once you’re ready to submit your changes, make a pull request to the main branch. Describe what your code does and link to any relevant issues.
- **Code review**: Wait for at least one code review. We might suggest some changes or improvements.
- **Integration**: Once approved, your PR will be merged into the main branch!

### Stay Involved
- **Feedback**: Don’t hesitate to leave feedback. We're always trying to improve and your opinions matter!
- **Ask questions**: Always feel free to ask questions if you’re unsure about something. We're here to help!

### Code of Conduct
- **Respectful communication**: Please be polite and respectful in your interactions with other community members. We strive to provide a welcoming environment for everyone.

Thank you for contributing to our project! We’re excited to see what you bring to the community.


## License

Released under [BSD 3-Clause](/LICENSE) by [@fvcl](https://github.com/fvcl).
